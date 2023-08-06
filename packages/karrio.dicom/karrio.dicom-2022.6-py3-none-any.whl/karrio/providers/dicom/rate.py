from typing import Tuple, List
from dicom_lib.rates import (
    RateRequest as DicomRateRequest,
    Address,
    Parcel,
    Surcharge,
    Rate,
    RateResponse,
)
from karrio.core.units import Packages, Services
from karrio.core.utils import Serializable, DP, NF
from karrio.core.models import ChargeDetails, RateRequest, RateDetails, Message

from karrio.providers.dicom.units import (
    UnitOfMeasurement,
    ParcelType,
    Service,
    ShippingOption,
    PaymentType,
)
from karrio.providers.dicom.error import parse_error_response
from karrio.providers.dicom.utils import Settings


def parse_rate_response(
    response: dict, settings: Settings
) -> Tuple[List[RateDetails], List[Message]]:
    errors = parse_error_response(response, settings)
    rate_response = (
        DP.to_object(RateResponse, response) if "rates" in response else RateResponse()
    )
    details = [
        _extract_details(rate, rate_response, settings)
        for rate in (rate_response.rates or [])
    ]

    return details, errors


def _extract_details(
    rate: Rate, response: RateResponse, settings: Settings
) -> RateDetails:
    charges = [
        ("Base Charge", rate.basicCharge),
        ("Discount", rate.discountAmount),
        ("Taxes", rate.taxes),
        *((charge.name, charge.amount) for charge in rate.surcharges),
    ]

    return RateDetails(
        carrier_id=settings.carrier_id,
        carrier_name=settings.carrier_name,
        currency="CAD",
        transit_days=response.delay,
        service=Service(rate.rateType),
        total_charge=NF.decimal(rate.total),
        extra_charges=[
            ChargeDetails(
                currency="CAD",
                name=name,
                amount=NF.decimal(charge),
            )
            for name, charge in charges
            if charge
        ],
        meta=dict(accountType=rate.accountType),
    )


def rate_request(
    payload: RateRequest, settings: Settings
) -> Serializable[DicomRateRequest]:
    packages = Packages(payload.parcels)
    service = (
        Services(payload.services, Service).first or Service.dicom_ground_delivery
    ).value
    options = ShippingOption.to_options(
        payload.options, package_options=packages.options
    )

    request = DicomRateRequest(
        category="Parcel",
        paymentType=PaymentType.prepaid.value,
        deliveryType=service,
        unitOfMeasurement=UnitOfMeasurement.KC.value,
        sender=Address(
            postalCode=payload.shipper.postal_code,
            provinceCode=payload.shipper.state_code,
            countryCode=payload.shipper.country_code,
            name=(payload.shipper.company_name or payload.shipper.person_name),
        ),
        consignee=Address(
            postalCode=payload.recipient.postal_code,
            provinceCode=payload.recipient.state_code,
            countryCode=payload.recipient.country_code,
            name=(payload.recipient.company_name or payload.recipient.person_name),
        ),
        parcels=[
            Parcel(
                quantity=1,
                parcelType=ParcelType[package.packaging_type or "dicom_box"].value,
                id=None,
                weight=package.weight.KG,
                length=package.height.CM,
                depth=package.length.CM,
                width=package.width.CM,
                note=None,
                status=None,
                FCA_Class=None,
                hazmat=None,
                requestReturnLabel=None,
                returnWaybill=None,
            )
            for package in packages
        ],
        billing=settings.billing_account,
        promoCodes=None,
        surcharges=[
            Surcharge(
                type=code,
                value=value,
            )
            for _, code, value in options.as_list()
        ],
        appointment=None,
    )

    return Serializable(request, DP.to_dict)
