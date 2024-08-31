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

class FreightingGoodsCargoShipWeightAndDistance(BaseModel):
    """
    FreightingGoodsCargoShipWeightAndDistance
    """ # noqa: E501
    type: StrictStr
    activity: Optional[StrictStr] = 'cargo_ship'
    specification: Optional[StrictStr] = 'average'
    detail: Optional[StrictStr] = Field(default='average', description=" **Hint:** Some specifications only support certain details.")
    value: Union[StrictFloat, StrictInt] = Field(description="The value in the given unit")
    unit: Optional[StrictStr] = Field(default='metric tons.kilometers', description="Distance a specific weight traveled in the given unit.    **Example:** 10 metric tons travel 50 kilometers. So the right `value` would be **500** and the `unit` would be **metric tons.kilometers**.    Need a more specific unit? See the **[full list of supported units (Sections 5 and 6)](https://convert.js.org/types/_unitsbymeasureraw)**.")
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

        if value not in set(['bulk_carrier', 'general_cargo', 'container_ship', 'vehicle_transport', 'roro-ferry', 'large_ropax_ferry', 'refrigerated_cargo', 'average']):
            raise ValueError("must be one of enum values ('bulk_carrier', 'general_cargo', 'container_ship', 'vehicle_transport', 'roro-ferry', 'large_ropax_ferry', 'refrigerated_cargo', 'average')")
        return value

    @field_validator('detail')
    def detail_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['200,000+_dwt', '100,000–199,999_dwt', '60,000–99,999_dwt', '35,000–59,999_dwt', '10,000–34,999_dwt', '0–9999_dwt', 'average', '10,000+_dwt', '5000–9999_dwt', '0–4999_dwt', '10,000+_dwt_100+_teu', '5000–9999_dwt_100+_teu', '0–4999_dwt_100+_teu', '8000+_teu', '5000–7999_teu', '3000–4999_teu', '2000–2999_teu', '1000–1999_teu', '0–999_teu', '4000+_ceu', '0–3999_ceu', '2000+_lm', '0–1999_lm', '_all_dwt']):
            raise ValueError("must be one of enum values ('200,000+_dwt', '100,000–199,999_dwt', '60,000–99,999_dwt', '35,000–59,999_dwt', '10,000–34,999_dwt', '0–9999_dwt', 'average', '10,000+_dwt', '5000–9999_dwt', '0–4999_dwt', '10,000+_dwt_100+_teu', '5000–9999_dwt_100+_teu', '0–4999_dwt_100+_teu', '8000+_teu', '5000–7999_teu', '3000–4999_teu', '2000–2999_teu', '1000–1999_teu', '0–999_teu', '4000+_ceu', '0–3999_ceu', '2000+_lm', '0–1999_lm', '_all_dwt')")
        return value

    @field_validator('unit')
    def unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['metric tons.kilometers', 'metric tons.meters', 'metric tons.miles', 'kilograms.kilometers', 'kilograms.meters', 'kilograms.miles']):
            raise ValueError("must be one of enum values ('metric tons.kilometers', 'metric tons.meters', 'metric tons.miles', 'kilograms.kilometers', 'kilograms.meters', 'kilograms.miles')")
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
        """Create an instance of FreightingGoodsCargoShipWeightAndDistance from a JSON string"""
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
        """Create an instance of FreightingGoodsCargoShipWeightAndDistance from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "activity": obj.get("activity") if obj.get("activity") is not None else 'cargo_ship',
            "specification": obj.get("specification") if obj.get("specification") is not None else 'average',
            "detail": obj.get("detail") if obj.get("detail") is not None else 'average',
            "value": obj.get("value"),
            "unit": obj.get("unit") if obj.get("unit") is not None else 'metric tons.kilometers'
        })
        return _obj

