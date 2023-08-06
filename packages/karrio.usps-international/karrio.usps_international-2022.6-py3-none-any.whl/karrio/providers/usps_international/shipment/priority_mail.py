import time
from typing import Tuple, List
from usps_lib.evs_priority_mail_intl_response import eVSPriorityMailIntlResponse
from usps_lib.evs_priority_mail_intl_request import (
    eVSPriorityMailIntlRequest,
    ImageParametersType,
    ShippingContentsType,
    ItemDetailType,
    ExtraServicesType,
)
from karrio.core.utils import Serializable, Element, XP, DF, Location
from karrio.core.units import (
    CustomsInfo,
    Packages,
    Options,
    Weight,
    WeightUnit,
    CompleteAddress,
)
from karrio.core.models import (
    Documents,
    ShipmentRequest,
    ShipmentDetails,
    Message,
    Address,
    Customs,
)
from karrio.providers.usps_international.units import (
    LabelFormat,
    ShippingOption,
    ContentType,
)
from karrio.providers.usps_international.error import parse_error_response
from karrio.providers.usps_international.utils import Settings


def parse_shipment_response(
    response: Element, settings: Settings
) -> Tuple[ShipmentDetails, List[Message]]:
    errors = parse_error_response(response, settings)
    details = _extract_details(response, settings)

    return details, errors


def _extract_details(response: Element, settings: Settings) -> ShipmentDetails:
    shipment = XP.to_object(eVSPriorityMailIntlResponse, response)

    return ShipmentDetails(
        carrier_name=settings.carrier_name,
        carrier_id=settings.carrier_id,
        tracking_number=shipment.BarcodeNumber,
        shipment_identifier=shipment.BarcodeNumber,
        docs=Documents(label=shipment.LabelImage),
    )


def shipment_request(
    payload: ShipmentRequest, settings: Settings
) -> Serializable[eVSPriorityMailIntlRequest]:
    package = Packages(
        payload.parcels,
        package_option_type=ShippingOption,
        max_weight=Weight(70, WeightUnit.LB),
    ).single
    options = ShippingOption.to_options(
        payload.options,
        package_options=package.options,
    )

    label_format = LabelFormat[payload.label_type or "usps_6_x_4_label"].value
    insurance = ShippingOption.insurance_from(options, "priority_mail")
    customs = CustomsInfo(payload.customs or Customs(commodities=[]))
    redirect_address = CompleteAddress.map(
        Address(**(options.usps_option_redirect_non_delivery or {}))
    )

    request = eVSPriorityMailIntlRequest(
        USERID=settings.username,
        Option=None,
        Revision=2,
        ImageParameters=ImageParametersType(ImageParameter=label_format),
        FromFirstName=customs.signer or payload.shipper.person_name or "N/A",
        FromMiddleInitial=None,
        FromLastName=payload.shipper.person_name,
        FromFirm=payload.shipper.company_name or "N/A",
        FromAddress1=payload.shipper.address_line2,
        FromAddress2=payload.shipper.address_line1,
        FromUrbanization=None,
        FromCity=payload.shipper.city,
        FromState=Location(payload.shipper.state_code, country="US").as_state_name,
        FromZip5=Location(payload.shipper.postal_code).as_zip5,
        FromZip4=Location(payload.shipper.postal_code).as_zip4 or "",
        FromPhone=payload.shipper.phone_number,
        FromCustomsReference=None,
        ToName=None,
        ToFirstName=payload.recipient.person_name,
        ToLastName=None,
        ToFirm=payload.recipient.company_name or "N/A",
        ToAddress1=payload.recipient.address_line2,
        ToAddress2=payload.recipient.address_line1,
        ToAddress3=None,
        ToCity=payload.recipient.city,
        ToProvince=Location(
            payload.recipient.state_code, country=payload.recipient.country_code
        ).as_state_name,
        ToCountry=Location(payload.recipient.country_code).as_country_name,
        ToPostalCode=payload.recipient.postal_code,
        ToPOBoxFlag=None,
        ToPhone=payload.recipient.phone_number,
        ToFax=None,
        ToEmail=payload.recipient.email,
        ImportersReferenceNumber=None,
        NonDeliveryOption=ShippingOption.non_delivery_from(options),
        RedirectName=redirect_address.person_name,
        RedirectEmail=redirect_address.email,
        RedirectSMS=redirect_address.phone_number,
        RedirectAddress=redirect_address.address_line,
        RedirectCity=redirect_address.city,
        RedirectState=redirect_address.state_code,
        RedirectZipCode=redirect_address.postal_code,
        RedirectZip4=Location(redirect_address.postal_code).as_zip4 or "",
        Container=None,
        ShippingContents=ShippingContentsType(
            ItemDetail=[
                ItemDetailType(
                    Description=item.description,
                    Quantity=item.quantity,
                    Value=item.value_amount,
                    NetPounds=Weight(
                        item.weight, WeightUnit[item.weight_unit or "LB"]
                    ).LB,
                    NetOunces=Weight(
                        item.weight, WeightUnit[item.weight_unit or "LB"]
                    ).OZ,
                    HSTariffNumber=item.hs_code or item.sku,
                    CountryOfOrigin=Location(item.origin_country).as_country_name,
                )
                for item in customs.commodities
            ]
        ),
        Insured=("N" if insurance is None else "Y"),
        InsuredAmount=insurance,
        GrossPounds=package.weight.LB,
        GrossOunces=package.weight.OZ,
        ContentType=ContentType[customs.content_type or "other"].value,
        ContentTypeOther=customs.content_description or "N/A",
        Agreement=("N" if customs.certify else "Y"),
        Comments=customs.content_description,
        LicenseNumber=customs.license_number,
        CertificateNumber=customs.certificate_number,
        InvoiceNumber=customs.invoice,
        ImageType="PDF",
        ImageLayout="ALLINONEFILE",
        CustomerRefNo=None,
        CustomerRefNo2=None,
        POZipCode=None,
        LabelDate=DF.fdatetime(
            (options.shipment_date or time.strftime("%Y-%m-%d")),
            current_format="%Y-%m-%d",
            output_format="%m/%d/%Y",
        ),
        EMCAAccount=None,
        HoldForManifest=None,
        EELPFC=customs.eel_pfc,
        PriceOptions=None,
        Length=package.length.IN,
        Width=package.width.IN,
        Height=package.height.IN,
        Girth=(package.girth.value if package.packaging_type == "tube" else None),
        ExtraServices=(
            ExtraServicesType(
                ExtraService=[code for _, code, value in options.as_list()]
            )
            if any(options.as_list())
            else None
        ),
        ActionCode=None,
        OptOutOfSPE=None,
        PermitNumber=None,
        AccountZipCode=None,
        ImportersReferenceType=None,
        ImportersTelephoneNumber=None,
        ImportersFaxNumber=None,
        ImportersEmail=None,
        Machinable=(options.usps_option_machinable_item or False),
        DestinationRateIndicator="I",
        MID=settings.mailer_id,
        LogisticsManagerMID=settings.logistics_manager_mailer_id,
        CRID=settings.customer_registration_id,
        VendorCode=None,
        VendorProductVersionNumber=None,
        ChargebackCode=None,
    )

    return Serializable(request, XP.export)
