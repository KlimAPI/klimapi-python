# coding: utf-8

"""
    KlimAPI - Calculation & Compensation API

    This API offers you the possibility to calculate and offset emissions, create checkout links, get statistics and much more.

    API Version: v2
    Contact: tech@klimapi.com

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from klimapi_python.models.project import Project
from typing import Optional, Set
from typing_extensions import Self

class PendingOrder(BaseModel):
    """
    PendingOrder
    """ # noqa: E501
    order_id: Optional[StrictStr] = None
    status: Optional[StrictStr] = Field(default=None, description="The status of the order")
    price: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total of the compensation in your given currency **excl. VAT**.")
    currency: Optional[StrictStr] = None
    kg_co2e: Optional[StrictInt] = Field(default=None, description="The amount of kg CO<sub>2</sub>e.", alias="kgCO2e")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Add additional queryable information to the order as key-value pairs")
    project: Optional[Project] = None
    __properties: ClassVar[List[str]] = ["order_id", "status", "price", "currency", "kgCO2e", "metadata", "project"]

    @field_validator('status')
    def status_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['offer', 'payment_pending', 'offset_pending', 'processed', 'refunded']):
            raise ValueError("must be one of enum values ('offer', 'payment_pending', 'offset_pending', 'processed', 'refunded')")
        return value

    @field_validator('currency')
    def currency_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['EUR', 'USD', 'GBP', 'CHF', 'CAD', 'NOK', 'SEK', 'DKK', 'INR', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BWP', 'BZD', 'COP', 'CRC', 'CVE', 'CZK', 'DOP', 'DZD', 'EGP', 'ETB', 'FJD', 'FKP', 'GEL', 'GIP', 'GMD', 'GTQ', 'GYD', 'HKD', 'HNL', 'HTG', 'HUF', 'IDR', 'ILS', 'ISK', 'JMD', 'KES', 'KGS', 'KHR', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'MAD', 'MDL', 'MKD', 'MMK', 'MNT', 'MOP', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NPR', 'NZD', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'QAR', 'RON', 'RSD', 'SBD', 'SCR', 'SGD', 'SHP', 'SLE', 'SOS', 'SRD', 'STD', 'SZL', 'THB', 'TJS', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UYU', 'UZS', 'WST', 'XCD', 'YER', 'ZAR', 'ZMW']):
            raise ValueError("must be one of enum values ('EUR', 'USD', 'GBP', 'CHF', 'CAD', 'NOK', 'SEK', 'DKK', 'INR', 'ALL', 'AMD', 'ANG', 'AOA', 'ARS', 'AUD', 'AWG', 'AZN', 'BAM', 'BBD', 'BDT', 'BGN', 'BMD', 'BND', 'BOB', 'BRL', 'BSD', 'BWP', 'BZD', 'COP', 'CRC', 'CVE', 'CZK', 'DOP', 'DZD', 'EGP', 'ETB', 'FJD', 'FKP', 'GEL', 'GIP', 'GMD', 'GTQ', 'GYD', 'HKD', 'HNL', 'HTG', 'HUF', 'IDR', 'ILS', 'ISK', 'JMD', 'KES', 'KGS', 'KHR', 'KYD', 'KZT', 'LAK', 'LBP', 'LKR', 'LRD', 'LSL', 'MAD', 'MDL', 'MKD', 'MMK', 'MNT', 'MOP', 'MUR', 'MVR', 'MWK', 'MXN', 'MYR', 'MZN', 'NAD', 'NGN', 'NIO', 'NPR', 'NZD', 'PAB', 'PEN', 'PGK', 'PHP', 'PKR', 'PLN', 'QAR', 'RON', 'RSD', 'SBD', 'SCR', 'SGD', 'SHP', 'SLE', 'SOS', 'SRD', 'STD', 'SZL', 'THB', 'TJS', 'TOP', 'TRY', 'TTD', 'TWD', 'TZS', 'UAH', 'UYU', 'UZS', 'WST', 'XCD', 'YER', 'ZAR', 'ZMW')")
        return value

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of PendingOrder from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of project
        if self.project:
            _dict['project'] = self.project.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PendingOrder from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "order_id": obj.get("order_id"),
            "status": obj.get("status"),
            "price": obj.get("price"),
            "currency": obj.get("currency"),
            "kgCO2e": obj.get("kgCO2e"),
            "metadata": obj.get("metadata"),
            "project": Project.from_dict(obj["project"]) if obj.get("project") is not None else None
        })
        return _obj


