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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from klimapi_python.models.pending_by_calculation_request_calculation_options_inner import PendingByCalculationRequestCalculationOptionsInner
from typing import Optional, Set
from typing_extensions import Self

class LinkByCalculationRequest(BaseModel):
    """
    LinkByCalculationRequest
    """ # noqa: E501
    calculation_options: List[PendingByCalculationRequestCalculationOptionsInner] = Field(description="An Array of [Calculation Options](https://klimapi.com/resources/factors). See the full list of supported options [here](https://klimapi.com/resources/factors).")
    change_allowed: Optional[StrictBool] = Field(default=False, description="Choose if the customer should be allowed to change the amount.")
    success_url: StrictStr = Field(description="The URL the customer is redirected to after the successful compensation.")
    cancel_url: StrictStr = Field(description="The URL the customer is redirected to after a failed or aborted compensation.")
    order_count: Optional[Annotated[int, Field(le=3, strict=True, ge=1)]] = Field(default=1, description="The amount of pending Orders you want to receive. This is especially useful if you want to offer your customers several different projects for their compensation.")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Add additional queryable information to the order as key-value pairs")
    fractional_digits: Optional[Annotated[int, Field(strict=True, ge=0)]] = Field(default=2, description="Normally, the calculation results are rounded to the nearest whole number. Specify here how many decimal places you would like to receive in addition. This only applies to calculation results, compensations are always made in whole kilograms")
    payment_type: Optional[StrictStr] = Field(default='default', description="With `default` we will automatically provide payment methods based on the customers location, use `invoice` to enable payment by invoice for the given link. Please note that `invoice` bank transfer is only available if **X-CURRENCY** is set to `EUR`. The invoice can always be paid by card.")
    __properties: ClassVar[List[str]] = ["calculation_options", "change_allowed", "success_url", "cancel_url", "order_count", "metadata", "fractional_digits", "payment_type"]

    @field_validator('payment_type')
    def payment_type_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['default', 'invoice']):
            raise ValueError("must be one of enum values ('default', 'invoice')")
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
        """Create an instance of LinkByCalculationRequest from a JSON string"""
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
        """Create an instance of LinkByCalculationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "calculation_options": [PendingByCalculationRequestCalculationOptionsInner.from_dict(_item) for _item in obj["calculation_options"]] if obj.get("calculation_options") is not None else None,
            "change_allowed": obj.get("change_allowed") if obj.get("change_allowed") is not None else False,
            "success_url": obj.get("success_url"),
            "cancel_url": obj.get("cancel_url"),
            "order_count": obj.get("order_count") if obj.get("order_count") is not None else 1,
            "metadata": obj.get("metadata"),
            "fractional_digits": obj.get("fractional_digits") if obj.get("fractional_digits") is not None else 2,
            "payment_type": obj.get("payment_type") if obj.get("payment_type") is not None else 'default'
        })
        return _obj


