from typing import List, Tuple, cast
from freightcom_lib.quote_request import (
    Freightcom,
    QuoteRequestType,
    FromType,
    ToType,
    PackagesType,
    PackageType,
)
from freightcom_lib.quote_reply import QuoteType, SurchargeType
from karrio.core.utils import Element, Serializable, SF, NF, XP
from karrio.core.models import RateRequest, RateDetails, Message, ChargeDetails
from karrio.core.units import Packages, Options, Services
from karrio.providers.freightcom.utils import (
    Settings,
    standard_request_serializer,
    ceil,
)
from karrio.providers.freightcom.units import (
    ShippingService,
    FreightPackagingType,
    FreightClass,
    ShippingOption,
)
from karrio.providers.freightcom.error import parse_error_response


def parse_quote_reply(
    response: Element, settings: Settings
) -> Tuple[List[RateDetails], List[Message]]:
    estimates = response.xpath(".//*[local-name() = $name]", name="Quote")
    return (
        [_extract_rate(node, settings) for node in estimates],
        parse_error_response(response, settings),
    )


def _extract_rate(node: Element, settings: Settings) -> RateDetails:
    quote = XP.build(QuoteType, node)
    rate_provider, service, service_name = ShippingService.info(
        quote.serviceId, quote.carrierId, quote.serviceName, quote.carrierName
    )
    charges = [
        ("Base charge", quote.baseCharge),
        ("Fuel surcharge", quote.fuelSurcharge),
        *((surcharge.name, surcharge.amount) for surcharge in quote.Surcharge),
    ]

    return RateDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        currency=quote.currency,
        service=service,
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


def quote_request(payload: RateRequest, settings: Settings) -> Serializable[Freightcom]:
    packages = Packages(
        payload.parcels,
        package_option_type=ShippingOption,
        required=["weight", "height", "width", "length"],
    )
    options = ShippingOption.to_options(
        payload.options,
        package_options=packages.options,
    )
    packaging_type = FreightPackagingType[packages.package_type or "small_box"].value
    packaging = (
        "Pallet" if packaging_type in [FreightPackagingType.pallet.value] else "Package"
    )
    service = (
        Services(payload.services, ShippingService).first
        or ShippingService.freightcom_all
    )

    freight_class = next(
        (FreightClass[c].value for c in payload.options.keys() if c in FreightClass),
        None,
    )

    request = Freightcom(
        username=settings.username,
        password=settings.password,
        version="3.1.0",
        QuoteRequest=QuoteRequestType(
            saturdayPickupRequired=options.freightcom_saturday_pickup_required,
            homelandSecurity=options.freightcom_homeland_security,
            pierCharge=None,
            exhibitionConventionSite=options.freightcom_exhibition_convention_site,
            militaryBaseDelivery=options.freightcom_military_base_delivery,
            customsIn_bondFreight=options.freightcom_customs_in_bond_freight,
            limitedAccess=options.freightcom_limited_access,
            excessLength=options.freightcom_excess_length,
            tailgatePickup=options.freightcom_tailgate_pickup,
            residentialPickup=options.freightcom_residential_pickup,
            crossBorderFee=None,
            notifyRecipient=options.freightcom_notify_recipient,
            singleShipment=options.freightcom_single_shipment,
            tailgateDelivery=options.freightcom_tailgate_delivery,
            residentialDelivery=options.freightcom_residential_delivery,
            insuranceType=options.insurance is not None,
            scheduledShipDate=None,
            insideDelivery=options.freightcom_inside_delivery,
            isSaturdayService=options.freightcom_is_saturday_service,
            dangerousGoodsType=options.freightcom_dangerous_goods_type,
            serviceId=service.value,
            stackable=options.freightcom_stackable,
            From=FromType(
                id=None,
                company=payload.shipper.company_name or " ",
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
                company=payload.recipient.company_name or " ",
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
            COD=None,
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
        ),
    )

    return Serializable(request, standard_request_serializer)
