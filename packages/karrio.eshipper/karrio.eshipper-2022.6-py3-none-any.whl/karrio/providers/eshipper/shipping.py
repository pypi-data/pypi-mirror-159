from typing import List, Tuple, cast
from eshipper_lib.shipping_request import (
    EShipper,
    ShippingRequestType,
    FromType,
    ToType,
    PackagesType,
    PackageType,
    PaymentType as RequestPaymentType,
    CODType,
    CODReturnAddressType,
    ContactType,
    ReferenceType,
    CustomsInvoiceType,
    ItemType,
    BillToType,
)
from eshipper_lib.shipping_reply import (
    ShippingReplyType,
    QuoteType,
    SurchargeType,
)
from karrio.core.utils import Element, Serializable, SF, NF, XP
from karrio.core.models import (
    Documents,
    ShipmentRequest,
    ShipmentDetails,
    RateDetails,
    Message,
    ChargeDetails,
    Address,
)
from karrio.core.units import Packages, Options
from karrio.providers.eshipper.utils import (
    Settings,
    standard_request_serializer,
    ceil,
)
from karrio.providers.eshipper.units import (
    ShippingService,
    PackagingType,
    FreightClass,
    ShippingOption,
    PaymentType,
)
from karrio.providers.eshipper.error import parse_error_response


def parse_shipping_reply(
    response: Element, settings: Settings
) -> Tuple[ShipmentDetails, List[Message]]:
    shipping_node = XP.find("ShippingReply", response, first=True)
    shipment = (
        _extract_shipment(shipping_node, settings)
        if shipping_node is not None
        else None
    )

    return shipment, parse_error_response(response, settings)


def _extract_shipment(node: Element, settings: Settings) -> ShipmentDetails:
    shipping = XP.build(ShippingReplyType, node)
    quote: QuoteType = shipping.Quote

    tracking_number = getattr(
        next(iter(shipping.Package), None), "trackingNumber", None
    )
    rate_provider, service, service_name = ShippingService.info(
        quote.serviceId, quote.carrierId, quote.serviceName, quote.carrierName
    )
    charges = [
        ("Base charge", quote.baseCharge),
        ("Fuel surcharge", quote.fuelSurcharge),
        *((surcharge.name, surcharge.amount) for surcharge in quote.Surcharge),
    ]

    return ShipmentDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        tracking_number=tracking_number,
        shipment_identifier=shipping.Order.id,
        selected_rate=(
            RateDetails(
                carrier_name=settings.carrier_name,
                carrier_id=settings.carrier_id,
                service=service,
                currency=quote.currency,
                total_charge=NF.decimal(quote.totalCharge),
                transit_days=quote.transitDays,
                extra_charges=[
                    ChargeDetails(
                        name=name,
                        currency="CAD",
                        amount=NF.decimal(amount),
                    )
                    for name, amount in charges
                    if amount
                ],
                meta=dict(rate_provider=rate_provider, service_name=service_name),
            )
            if quote is not None
            else None
        ),
        docs=Documents(label=shipping.Labels),
        meta=dict(
            rate_provider=rate_provider,
            service_name=service_name,
            tracking_url=shipping.TrackingURL,
        ),
    )


def shipping_request(
    payload: ShipmentRequest, settings: Settings
) -> Serializable[EShipper]:
    packages = Packages(
        payload.parcels,
        package_option_type=ShippingOption,
        required=["weight", "height", "width", "length"],
    )
    options = ShippingOption.to_options(
        payload.options,
        package_options=packages.options,
    )

    service = ShippingService.map(payload.service).value_or_key
    packaging_type = PackagingType[packages.package_type or "eshipper_boxes"].value
    packaging = (
        "Pallet" if packaging_type in [PackagingType.pallet.value] else "Package"
    )
    freight_class = (
        FreightClass[payload.options["freight_class"]].value
        if payload.options.get("freight_class") in FreightClass
        else None
    )
    payment_type = (
        PaymentType[payload.payment.paid_by].value if payload.payment else None
    )
    item = next(
        iter(payload.customs.commodities if payload.customs is not None else []), None
    )
    payer: Address = (
        {
            PaymentType.sender: payload.shipper,
            PaymentType.recipient: payload.recipient,
            PaymentType.third_party: payload.recipient,
        }.get(PaymentType[payload.payment.paid_by])
        if payload.payment
        else None
    )

    request = EShipper(
        username=settings.username,
        password=settings.password,
        version="3.0.0",
        ShippingRequest=ShippingRequestType(
            saturdayPickupRequired=options.eshipper_saturday_pickup_required,
            homelandSecurity=options.eshipper_homeland_security,
            pierCharge=None,
            exhibitionConventionSite=options.eshipper_exhibition_convention_site,
            militaryBaseDelivery=options.eshipper_military_base_delivery,
            customsIn_bondFreight=options.eshipper_customs_in_bond_freight,
            limitedAccess=options.eshipper_limited_access,
            excessLength=options.eshipper_excess_length,
            tailgatePickup=options.eshipper_tailgate_pickup,
            residentialPickup=options.eshipper_residential_pickup,
            crossBorderFee=None,
            notifyRecipient=options.eshipper_notify_recipient,
            singleShipment=options.eshipper_single_shipment,
            tailgateDelivery=options.eshipper_tailgate_delivery,
            residentialDelivery=options.eshipper_residential_delivery,
            insuranceType=options.insurance is not None,
            scheduledShipDate=None,
            insideDelivery=options.eshipper_inside_delivery,
            isSaturdayService=options.eshipper_is_saturday_service,
            dangerousGoodsType=options.eshipper_dangerous_goods_type,
            serviceId=service,
            stackable=options.eshipper_stackable,
            From=FromType(
                id=None,
                company=payload.shipper.company_name,
                instructions=None,
                email=payload.shipper.email,
                attention=payload.shipper.person_name,
                phone=payload.shipper.phone_number,
                tailgateRequired=None,
                residential=payload.shipper.residential,
                address1=SF.concat_str(payload.shipper.address_line1, join=True),
                address2=SF.concat_str(payload.shipper.address_line2, join=True),
                city=payload.shipper.city,
                state=payload.shipper.state_code,
                zip=payload.shipper.postal_code,
                country=payload.shipper.country_code,
            ),
            To=ToType(
                id=None,
                company=payload.recipient.company_name,
                notifyRecipient=None,
                instructions=None,
                email=payload.recipient.email,
                attention=payload.recipient.person_name,
                phone=payload.recipient.phone_number,
                tailgateRequired=None,
                residential=payload.recipient.residential,
                address1=SF.concat_str(payload.recipient.address_line1, join=True),
                address2=SF.concat_str(payload.recipient.address_line2, join=True),
                city=payload.recipient.city,
                state=payload.recipient.state_code,
                zip=payload.recipient.postal_code,
                country=payload.recipient.country_code,
            ),
            COD=(
                CODType(
                    paymentType=PaymentType.recipient.value,
                    CODReturnAddress=CODReturnAddressType(
                        codCompany=payload.recipient.company_name,
                        codName=payload.recipient.person_name,
                        codAddress1=SF.concat_str(
                            payload.recipient.address_line1, join=True
                        ),
                        codCity=payload.recipient.city,
                        codStateCode=payload.recipient.state_code,
                        codZip=payload.recipient.postal_code,
                        codCountry=payload.recipient.country_code,
                    ),
                )
                if options.cash_on_delivery is not None
                else None
            ),
            Packages=PackagesType(
                Package=[
                    PackageType(
                        length=ceil(package.length.IN),
                        width=ceil(package.width.IN),
                        height=ceil(package.height.IN),
                        weight=ceil(package.weight.LB),
                        type_=packaging_type,
                        freightClass=freight_class,
                        nmfcCode=None,
                        insuranceAmount=package.options.insurance,
                        codAmount=package.options.cash_on_delivery,
                        description=package.parcel.description,
                    )
                    for package in packages
                ],
                type_=packaging,
            ),
            Payment=(
                RequestPaymentType(type_=payment_type)
                if payload.payment is not None
                else None
            ),
            Reference=(
                [ReferenceType(name="REF", code=payload.reference)]
                if payload.reference != ""
                else None
            ),
            CustomsInvoice=(
                CustomsInvoiceType(
                    BillTo=BillToType(
                        company=payer.company_name,
                        name=payer.person_name,
                        address1=SF.concat_str(payer.address_line1, join=True),
                        city=payer.city,
                        state=payer.state_code,
                        zip=payer.postal_code,
                        country=payer.country_code,
                    ),
                    Contact=ContactType(
                        name=payer.person_name, phone=payer.phone_number
                    ),
                    Item=ItemType(
                        code=item.sku,
                        description=item.description,
                        originCountry=item.origin_country,
                        quantity=item.quantity,
                        unitPrice=item.value_amount,
                    ),
                )
                if all([payload.customs, payer])
                else None
            ),
        ),
    )

    return Serializable(request, standard_request_serializer)
