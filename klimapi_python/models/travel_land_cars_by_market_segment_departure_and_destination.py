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
from typing import Optional, Set
from typing_extensions import Self

class TravelLandCarsByMarketSegmentDepartureAndDestination(BaseModel):
    """
    TravelLandCarsByMarketSegmentDepartureAndDestination
    """ # noqa: E501
    type: StrictStr
    activity: Optional[StrictStr] = 'cars_by_market_segment'
    specification: Optional[StrictStr] = 'average'
    detail: Optional[StrictStr] = Field(default='average', description=" **Hint:** Some specifications only support certain details.")
    departure: StrictStr = Field(description="City, Postal Address, Train Station or IATA Code of the departure address")
    destination: StrictStr = Field(description="City, Postal Address, Train Station or IATA Code of the destination address")
    return_trip: Optional[StrictBool] = Field(default=True, description="Decide if the trip is one way or return")
    __properties: ClassVar[List[str]] = ["type", "activity", "specification", "detail", "departure", "destination", "return_trip"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['travel-land']):
            raise ValueError("must be one of enum values ('travel-land')")
        return value

    @field_validator('specification')
    def specification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['mini', 'supermini', 'lower_medium', 'upper_medium', 'executive', 'luxury', 'sports', 'dual_purpose_4x4', 'mpv', 'average']):
            raise ValueError("must be one of enum values ('mini', 'supermini', 'lower_medium', 'upper_medium', 'executive', 'luxury', 'sports', 'dual_purpose_4x4', 'mpv', 'average')")
        return value

    @field_validator('detail')
    def detail_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['diesel', 'petrol', 'battery_electric_vehicle', 'average', 'plug-in_hybrid_electric_vehicle']):
            raise ValueError("must be one of enum values ('diesel', 'petrol', 'battery_electric_vehicle', 'average', 'plug-in_hybrid_electric_vehicle')")
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
        """Create an instance of TravelLandCarsByMarketSegmentDepartureAndDestination from a JSON string"""
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
        """Create an instance of TravelLandCarsByMarketSegmentDepartureAndDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "activity": obj.get("activity") if obj.get("activity") is not None else 'cars_by_market_segment',
            "specification": obj.get("specification") if obj.get("specification") is not None else 'average',
            "detail": obj.get("detail") if obj.get("detail") is not None else 'average',
            "departure": obj.get("departure"),
            "destination": obj.get("destination"),
            "return_trip": obj.get("return_trip") if obj.get("return_trip") is not None else True
        })
        return _obj


