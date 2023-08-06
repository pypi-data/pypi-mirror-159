from typing import Tuple, List
from datetime import datetime
from usps_lib.intl_rate_v2_request import (
    IntlRateV2Request,
    PackageType,
    ExtraServicesType,
    GXGType,
)
from usps_lib.intl_rate_v2_response import ServiceType

from karrio.core.errors import OriginNotServicedError, DestinationNotServicedError
from karrio.core.utils import Serializable, Element, NF, XP, DF
from karrio.core.models import RateDetails, Message, RateRequest, ChargeDetails
from karrio.core.units import (
    Packages,
    Country,
    Weight,
    WeightUnit,
    Services,
    Options,
    Currency,
    CompleteAddress,
)

from karrio.providers.usps_international.units import (
    ShippingService,
    ShippingOption,
    PackagingType,
    ServiceClassID,
)
from karrio.providers.usps_international.error import parse_error_response
from karrio.providers.usps_international import Settings


def parse_rate_response(
    response: Element, settings: Settings
) -> Tuple[List[RateDetails], List[Message]]:
    quotes: List[RateDetails] = [
        _extract_details(package, settings) for package in XP.find("Service", response)
    ]
    return quotes, parse_error_response(response, settings)


def _extract_details(postage_node: Element, settings: Settings) -> RateDetails:
    postage: ServiceType = XP.to_object(ServiceType, postage_node)
    service = ServiceClassID.map(str(postage.ID))
    delivery_date = DF.date(postage.GuaranteeAvailability, "%m/%d/%Y")
    transit = (
        (delivery_date.date() - datetime.now().date()).days
        if delivery_date is not None
        else None
    )

    charges = [
        ("Base charge", postage.Postage),
        *((s.ServiceName, s.Price) for s in postage.ExtraServices.ExtraService),
    ]

    return RateDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        service=service.name_or_key,
        total_charge=NF.decimal(postage.Postage),
        currency=Currency.USD.name,
        transit_days=transit,
        extra_charges=[
            ChargeDetails(
                name=name,
                amount=NF.decimal(amount),
                currency=Currency.USD.name,
            )
            for name, amount in charges
            if amount
        ],
        meta=dict(service_name=service.name or postage.SvcDescription),
    )


def rate_request(
    payload: RateRequest, settings: Settings
) -> Serializable[IntlRateV2Request]:
    """Create the appropriate USPS International rate request depending on the destination

    :param payload: Karrio unified API rate request data
    :param settings: USPS International connection and auth settings
    :return: a domestic or international USPS International compatible request
    :raises:
        - OriginNotServicedError when origin country is not serviced by the carrier
        - DestinationNotServicedError when destination country is US
    """

    if (
        payload.shipper.country_code is not None
        and payload.shipper.country_code != Country.US.name
    ):
        raise OriginNotServicedError(payload.shipper.country_code)

    if payload.recipient.country_code == Country.US.name:
        raise DestinationNotServicedError(payload.recipient.country_code)

    recipient = CompleteAddress(payload.recipient)
    services = Services(payload.services, ShippingService)
    package = Packages(
        payload.parcels,
        package_option_type=ShippingOption,
        max_weight=Weight(70, WeightUnit.LB),
    ).single
    options = ShippingOption.to_options(
        payload.options,
        package_options=package.options,
    )

    commercial = next(("Y" for svc in services if "commercial" in svc.name), "N")
    commercial_plus = next(("Y" for svc in services if "plus" in svc.name), "N")

    request = IntlRateV2Request(
        USERID=settings.username,
        Revision="2",
        Package=[
            PackageType(
                ID=0,
                Pounds=package.weight.LB,
                Ounces=package.weight.OZ,
                Machinable=options.usps_option_machinable_item or False,
                MailType=PackagingType[package.packaging_type or "package"].value,
                GXG=(
                    GXGType(POBoxFlag="N", GiftFlag="N")
                    if any(
                        "global_express_guaranteed" in s.name for s in payload.services
                    )
                    else None
                ),
                ValueOfContents=(options.declared_value or ""),
                Country=recipient.country_name,
                Width=package.width.IN,
                Length=package.length.IN,
                Height=package.height.IN,
                Girth=(
                    package.girth.value if package.packaging_type == "tube" else None
                ),
                OriginZip=payload.shipper.postal_code,
                CommercialFlag=commercial,
                CommercialPlusFlag=commercial_plus,
                AcceptanceDateTime=DF.fdatetime(
                    (options.shipment_date or datetime.today()),
                    output_format="%Y-%m-%dT%H:%M:%S",
                ),
                DestinationPostalCode=recipient.postal_code,
                ExtraServices=(
                    ExtraServicesType(
                        ExtraService=[code for _, code, value in options.as_list()]
                    )
                    if any(options.as_list())
                    else None
                ),
                Content=None,
            )
        ],
    )

    return Serializable(request, XP.export)
