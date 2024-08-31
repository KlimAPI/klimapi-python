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

class HotelStayRoomPerNight(BaseModel):
    """
    HotelStayRoomPerNight
    """ # noqa: E501
    type: StrictStr
    activity: Optional[StrictStr] = 'average'
    value: Union[StrictFloat, StrictInt] = Field(description="The value in the given unit")
    unit: Optional[StrictStr] = Field(default='room_per_night', description="Need another unit? Contact us!")
    __properties: ClassVar[List[str]] = ["type", "activity", "value", "unit"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['hotel_stay']):
            raise ValueError("must be one of enum values ('hotel_stay')")
        return value

    @field_validator('activity')
    def activity_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['fr', 'de', 'in', 'id', 'cr', 'eg', 'uk', 'au', 'be', 'br', 'ca', 'cl', 'cn', 'co', 'it', 'jp', 'jo', 'kp', 'my', 'mv', 'mx', 'nl', 'om', 'ph', 'pt', 'qa', 'ru', 'sa', 'sg', 'za', 'es', 'ch', 'th', 'tr', 'ae', 'us', 'average']):
            raise ValueError("must be one of enum values ('fr', 'de', 'in', 'id', 'cr', 'eg', 'uk', 'au', 'be', 'br', 'ca', 'cl', 'cn', 'co', 'it', 'jp', 'jo', 'kp', 'my', 'mv', 'mx', 'nl', 'om', 'ph', 'pt', 'qa', 'ru', 'sa', 'sg', 'za', 'es', 'ch', 'th', 'tr', 'ae', 'us', 'average')")
        return value

    @field_validator('unit')
    def unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['room_per_night']):
            raise ValueError("must be one of enum values ('room_per_night')")
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
        """Create an instance of HotelStayRoomPerNight from a JSON string"""
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
        """Create an instance of HotelStayRoomPerNight from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "activity": obj.get("activity") if obj.get("activity") is not None else 'average',
            "value": obj.get("value"),
            "unit": obj.get("unit") if obj.get("unit") is not None else 'room_per_night'
        })
        return _obj


