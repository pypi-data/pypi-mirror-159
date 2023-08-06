from typing import List, Tuple
from datetime import datetime
from usps_lib.rate_v4_response import PostageType, SpecialServiceType
from usps_lib.rate_v4_request import (
    RateV4Request,
    PackageType,
    SpecialServicesType,
    ShipDateType,
)
from karrio.core.errors import OriginNotServicedError, DestinationNotServicedError
from karrio.core.utils import Serializable, Element, NF, XP, DF
from karrio.core.models import RateDetails, RateRequest, Message, ChargeDetails
from karrio.core.units import Packages, Currency, Options, Services, Country

from karrio.providers.usps.units import (
    ShipmentService,
    ShippingOption,
    PackagingType,
    ServiceClassID,
    FirstClassMailType,
    SortLevelType,
)
from karrio.providers.usps.error import parse_error_response
from karrio.providers.usps.utils import Settings


def parse_rate_response(
    response: Element, settings: Settings
) -> Tuple[List[RateDetails], List[Message]]:
    rates: List[RateDetails] = [
        _extract_details(package, settings) for package in XP.find("Postage", response)
    ]
    return rates, parse_error_response(response, settings)


def _extract_details(postage_node: Element, settings: Settings) -> RateDetails:
    postage: PostageType = XP.to_object(PostageType, postage_node)

    service = ServiceClassID.map(str(postage.CLASSID))
    charges: List[SpecialServiceType] = getattr(
        postage.SpecialServices, "SpecialService", []
    )
    rate = NF.decimal(XP.find("Rate", postage_node, first=True).text)
    estimated_date = DF.date(
        getattr(XP.find("CommitmentDate", postage_node, first=True), "text", None)
    )
    transit = (
        (estimated_date.date() - datetime.now().date()).days
        if estimated_date is not None
        else None
    )

    return RateDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        service=service.name_or_key,
        total_charge=rate,
        currency=Currency.USD.name,
        transit_days=transit,
        extra_charges=[
            ChargeDetails(
                name=charge.ServiceName,
                amount=NF.decimal(charge.Price),
                currency=Currency.USD.name,
            )
            for charge in charges
        ],
        meta=dict(service_name=(service.name or postage.MailService)),
    )


def rate_request(
    payload: RateRequest, settings: Settings
) -> Serializable[RateV4Request]:
    """Create the appropriate USPS rate request depending on the destination

    :param payload: Karrio unified API rate request data
    :param settings: USPS connection and auth settings
    :return: a domestic or international USPS compatible request
    :raises: an OriginNotServicedError when origin country is not serviced by the carrier
    """

    if (
        payload.shipper.country_code is not None
        and payload.shipper.country_code != Country.US.name
    ):
        raise OriginNotServicedError(payload.shipper.country_code)

    if (
        payload.recipient.country_code is not None
        and payload.recipient.country_code != Country.US.name
    ):
        raise DestinationNotServicedError(payload.recipient.country_code)

    package = Packages(payload.parcels, package_option_type=ShippingOption).single
    container = PackagingType[package.packaging_type or "your_packaging"]
    options = ShippingOption.to_options(
        payload.options,
        package_options=package.options,
    )
    service = (
        Services(payload.services, ShipmentService).first or ShipmentService.usps_all
    )

    request = RateV4Request(
        USERID=settings.username,
        Revision="2",
        Package=[
            PackageType(
                ID=0,
                Service=service.value,
                FirstClassMailType=(
                    FirstClassMailType[container.name].value
                    if "first_class" in service.value
                    else None
                ),
                ZipOrigination=payload.shipper.postal_code,
                ZipDestination=payload.recipient.postal_code,
                Pounds=package.weight.LB,
                Ounces=package.weight.OZ,
                Container=container.value,
                Width=package.width.IN,
                Length=package.length.IN,
                Height=package.height.IN,
                Girth=package.girth.value,
                Value=options.declared_value,
                AmountToCollect=options.cash_on_delivery,
                SpecialServices=(
                    SpecialServicesType(
                        SpecialService=[code for _, code, value in options.as_list()]
                    )
                    if any(options.as_list())
                    else None
                ),
                Content=None,
                GroundOnly=options.usps_option_ground_only,
                SortBy=(
                    SortLevelType[container.name].value
                    if service.value in ["All", "Online"]
                    else None
                ),
                Machinable=(options.usps_option_machinable_item or False),
                ReturnLocations=options.usps_option_return_service_info,
                ReturnServiceInfo=options.usps_option_return_service_info,
                DropOffTime=("13:30" if options.shipment_date is not None else None),
                ShipDate=(
                    ShipDateType(valueOf_=DF.fdate(options.shipment_date))
                    if options.shipment_date is not None
                    else None
                ),
            )
        ],
    )

    return Serializable(request, XP.export)
