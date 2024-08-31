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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class CalculationResult(BaseModel):
    """
    CalculationResult
    """ # noqa: E501
    kg_co2e: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The calculated Amount of CO<sub>2</sub> in Kilogram.", alias="kgCO2e")
    type: Optional[StrictStr] = Field(default=None, description="The type of the calculation")
    activity: Optional[StrictStr] = Field(default=None, description="The activity of the calculation")
    specification: Optional[StrictStr] = Field(default=None, description="The specification of the calculation")
    detail: Optional[StrictStr] = Field(default=None, description="The detail of the calculation")
    value: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The value of the calculation")
    unit: Optional[StrictStr] = Field(default=None, description="The unit of the calculation")
    emission_factor_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the emission factor the calculation is based on")
    emission_factor_last_updated: Optional[StrictStr] = Field(default=None, description="ISO 8601 formatted timestamp of the latest update for the given emission factor")
    __properties: ClassVar[List[str]] = ["kgCO2e", "type", "activity", "specification", "detail", "value", "unit", "emission_factor_id", "emission_factor_last_updated"]

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
        """Create an instance of CalculationResult from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CalculationResult from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kgCO2e": obj.get("kgCO2e"),
            "type": obj.get("type"),
            "activity": obj.get("activity"),
            "specification": obj.get("specification"),
            "detail": obj.get("detail"),
            "value": obj.get("value"),
            "unit": obj.get("unit"),
            "emission_factor_id": obj.get("emission_factor_id"),
            "emission_factor_last_updated": obj.get("emission_factor_last_updated")
        })
        return _obj


