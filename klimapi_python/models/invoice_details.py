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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from klimapi_python.models.invoice_details_address import InvoiceDetailsAddress
from klimapi_python.models.invoice_details_tax_id import InvoiceDetailsTaxId
from typing import Optional, Set
from typing_extensions import Self

class InvoiceDetails(BaseModel):
    """
    Required with **billing_type** = `invoice`
    """ # noqa: E501
    name: StrictStr = Field(description="The customer’s full name or business name")
    email: StrictStr = Field(description="The customer’s email address")
    address: InvoiceDetailsAddress
    tax_id: Optional[InvoiceDetailsTaxId] = None
    __properties: ClassVar[List[str]] = ["name", "email", "address", "tax_id"]

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
        """Create an instance of InvoiceDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of tax_id
        if self.tax_id:
            _dict['tax_id'] = self.tax_id.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "email": obj.get("email"),
            "address": InvoiceDetailsAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "tax_id": InvoiceDetailsTaxId.from_dict(obj["tax_id"]) if obj.get("tax_id") is not None else None
        })
        return _obj


