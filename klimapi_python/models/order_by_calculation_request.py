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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from klimapi_python.models.pending_by_calculation_request_calculation_options_inner import PendingByCalculationRequestCalculationOptionsInner
from typing import Optional, Set
from typing_extensions import Self

class OrderByCalculationRequest(BaseModel):
    """
    OrderByCalculationRequest
    """ # noqa: E501
    calculation_options: List[PendingByCalculationRequestCalculationOptionsInner] = Field(description="An Array of [Calculation Options](https://klimapi.com/resources/factors). See the full list of supported options [here](https://klimapi.com/resources/factors).")
    recipient_name: Optional[StrictStr] = Field(default=None, description="The name which should be associated with the compensation")
    recipient_email: Optional[StrictStr] = Field(default=None, description="If a valid e-mail address is provided, we will send the certificate to this address")
    send_at: Optional[datetime] = Field(default=None, description="Timestamp of when the certificate should be send to the customer in ISO 8601 format (UTC). Defaults to the current timestamp.")
    price_limit: Optional[Union[Annotated[float, Field(strict=True, ge=0.5)], Annotated[int, Field(strict=True, ge=1)]]] = Field(default=None, description="Set an optional price limit. if the order would exceed the limit a error will be thrown. Set the limit in the given currency.")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Add additional queryable information to the order as key-value pairs")
    fractional_digits: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=2, description="Normally, the calculation results are rounded to the nearest whole number. Specify here how many decimal places you would like to receive in addition. This only applies to calculation results, compensations are always made in whole kilograms")
    __properties: ClassVar[List[str]] = ["calculation_options", "recipient_name", "recipient_email", "send_at", "price_limit", "metadata", "fractional_digits"]

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
        """Create an instance of OrderByCalculationRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in calculation_options (list)
        _items = []
        if self.calculation_options:
            for _item in self.calculation_options:
                if _item:
                    _items.append(_item.to_dict())
            _dict['calculation_options'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of OrderByCalculationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "calculation_options": [PendingByCalculationRequestCalculationOptionsInner.from_dict(_item) for _item in obj["calculation_options"]] if obj.get("calculation_options") is not None else None,
            "recipient_name": obj.get("recipient_name"),
            "recipient_email": obj.get("recipient_email"),
            "send_at": obj.get("send_at"),
            "price_limit": obj.get("price_limit"),
            "metadata": obj.get("metadata"),
            "fractional_digits": obj.get("fractional_digits") if obj.get("fractional_digits") is not None else 2
        })
        return _obj


