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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from klimapi_python.models.cart_result_calculation_results_inner import CartResultCalculationResultsInner
from klimapi_python.models.cart_result_settings import CartResultSettings
from klimapi_python.models.pending_order import PendingOrder
from typing import Optional, Set
from typing_extensions import Self

class CartResult(BaseModel):
    """
    CartResult
    """ # noqa: E501
    kg_co2e: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of kg CO<sub>2</sub>e calculated.", alias="kgCO2e")
    settings: Optional[CartResultSettings] = None
    calculation_results: Optional[List[CartResultCalculationResultsInner]] = Field(default=None, description="The calculation results")
    orders: Optional[List[PendingOrder]] = None
    __properties: ClassVar[List[str]] = ["kgCO2e", "settings", "calculation_results", "orders"]

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
        """Create an instance of CartResult from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of settings
        if self.settings:
            _dict['settings'] = self.settings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in calculation_results (list)
        _items = []
        if self.calculation_results:
            for _item in self.calculation_results:
                if _item:
                    _items.append(_item.to_dict())
            _dict['calculation_results'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in orders (list)
        _items = []
        if self.orders:
            for _item in self.orders:
                if _item:
                    _items.append(_item.to_dict())
            _dict['orders'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CartResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kgCO2e": obj.get("kgCO2e"),
            "settings": CartResultSettings.from_dict(obj["settings"]) if obj.get("settings") is not None else None,
            "calculation_results": [CartResultCalculationResultsInner.from_dict(_item) for _item in obj["calculation_results"]] if obj.get("calculation_results") is not None else None,
            "orders": [PendingOrder.from_dict(_item) for _item in obj["orders"]] if obj.get("orders") is not None else None
        })
        return _obj


