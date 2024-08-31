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

class WasteDisposalPlasticWeight(BaseModel):
    """
    WasteDisposalPlasticWeight
    """ # noqa: E501
    type: StrictStr
    activity: Optional[StrictStr] = 'plastic'
    specification: Optional[StrictStr] = 'average'
    detail: Optional[StrictStr] = 'average'
    value: Union[StrictFloat, StrictInt] = Field(description="The value in the given unit")
    unit: Optional[StrictStr] = Field(default='metric tons', description="Need a more specific unit? See the **[full list of supported units (Section 5)](https://convert.js.org/types/_unitsbymeasureraw)**.")
    __properties: ClassVar[List[str]] = ["type", "activity", "specification", "detail", "value", "unit"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['waste_disposal']):
            raise ValueError("must be one of enum values ('waste_disposal')")
        return value

    @field_validator('specification')
    def specification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['plastics:average_plastics', 'plastics:average_plastic_film', 'plastics:average_plastic_rigid', 'plastics:hdpe_incl._forming', 'plastics:ldpe_and_lldpe_incl._forming', 'plastics:pet_incl._forming', 'plastics:pp_incl._forming', 'plastics:ps_incl._forming', 'plastics:pvc_incl._forming', 'average']):
            raise ValueError("must be one of enum values ('plastics:average_plastics', 'plastics:average_plastic_film', 'plastics:average_plastic_rigid', 'plastics:hdpe_incl._forming', 'plastics:ldpe_and_lldpe_incl._forming', 'plastics:pet_incl._forming', 'plastics:pp_incl._forming', 'plastics:ps_incl._forming', 'plastics:pvc_incl._forming', 'average')")
        return value

    @field_validator('detail')
    def detail_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['open-loop', 'closed-loop', 'combustion', 'landfill', 'average']):
            raise ValueError("must be one of enum values ('open-loop', 'closed-loop', 'combustion', 'landfill', 'average')")
        return value

    @field_validator('unit')
    def unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['kilograms', 'grams', 'metric tons', 'imperial tons', 'pounds', 'ounces']):
            raise ValueError("must be one of enum values ('kilograms', 'grams', 'metric tons', 'imperial tons', 'pounds', 'ounces')")
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
        """Create an instance of WasteDisposalPlasticWeight from a JSON string"""
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
        """Create an instance of WasteDisposalPlasticWeight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "activity": obj.get("activity") if obj.get("activity") is not None else 'plastic',
            "specification": obj.get("specification") if obj.get("specification") is not None else 'average',
            "detail": obj.get("detail") if obj.get("detail") is not None else 'average',
            "value": obj.get("value"),
            "unit": obj.get("unit") if obj.get("unit") is not None else 'metric tons'
        })
        return _obj


