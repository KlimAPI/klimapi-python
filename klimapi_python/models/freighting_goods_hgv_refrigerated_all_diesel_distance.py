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
from typing import Optional, Set
from typing_extensions import Self

class FreightingGoodsHgvRefrigeratedAllDieselDistance(BaseModel):
    """
    FreightingGoodsHgvRefrigeratedAllDieselDistance
    """ # noqa: E501
    type: StrictStr
    activity: Optional[StrictStr] = 'hgv_refrigerated_all_diesel'
    specification: Optional[StrictStr] = 'average'
    detail: Optional[StrictStr] = 'average'
    value: Union[StrictFloat, StrictInt] = Field(description="The value in the given unit")
    unit: Optional[StrictStr] = Field(default='kilometers', description="Need a more specific unit? See the **[full list of supported units (Section 6)](https://convert.js.org/types/_unitsbymeasureraw)**.")
    __properties: ClassVar[List[str]] = ["type", "activity", "specification", "detail", "value", "unit"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['freighting_goods']):
            raise ValueError("must be one of enum values ('freighting_goods')")
        return value

    @field_validator('specification')
    def specification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['rigid_>3.5-7.5_tons', 'rigid_>7.5_tons-17_tons', 'rigid_>17_tons', 'all_rigids', 'articulated_>3.5-33t', 'articulated_>33t', 'all_artics', 'all_hgvs', 'average']):
            raise ValueError("must be one of enum values ('rigid_>3.5-7.5_tons', 'rigid_>7.5_tons-17_tons', 'rigid_>17_tons', 'all_rigids', 'articulated_>3.5-33t', 'articulated_>33t', 'all_artics', 'all_hgvs', 'average')")
        return value

    @field_validator('detail')
    def detail_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['50%_load', '100%_load', '0%_load', 'average']):
            raise ValueError("must be one of enum values ('50%_load', '100%_load', '0%_load', 'average')")
        return value

    @field_validator('unit')
    def unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kilometers', 'meters', 'centimeters', 'millimeters', 'inches', 'feet', 'yards', 'miles', 'nautical miles']):
            raise ValueError("must be one of enum values ('kilometers', 'meters', 'centimeters', 'millimeters', 'inches', 'feet', 'yards', 'miles', 'nautical miles')")
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
        """Create an instance of FreightingGoodsHgvRefrigeratedAllDieselDistance from a JSON string"""
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
        """Create an instance of FreightingGoodsHgvRefrigeratedAllDieselDistance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "activity": obj.get("activity") if obj.get("activity") is not None else 'hgv_refrigerated_all_diesel',
            "specification": obj.get("specification") if obj.get("specification") is not None else 'average',
            "detail": obj.get("detail") if obj.get("detail") is not None else 'average',
            "value": obj.get("value"),
            "unit": obj.get("unit") if obj.get("unit") is not None else 'kilometers'
        })
        return _obj


