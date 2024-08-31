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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class TravelLandAverageDepartureAndDestination(BaseModel):
    """
    TravelLandAverageDepartureAndDestination
    """ # noqa: E501
    type: StrictStr
    departure: StrictStr = Field(description="City, Postal Address, Train Station or IATA Code of the departure address")
    destination: StrictStr = Field(description="City, Postal Address, Train Station or IATA Code of the destination address")
    return_trip: Optional[StrictBool] = Field(default=True, description="Decide if the trip is one way or return")
    passengers: Optional[StrictInt] = Field(default=1, description="The total of passengers travelling this route")
    __properties: ClassVar[List[str]] = ["type", "departure", "destination", "return_trip", "passengers"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['travel-land']):
            raise ValueError("must be one of enum values ('travel-land')")
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
        """Create an instance of TravelLandAverageDepartureAndDestination from a JSON string"""
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
        """Create an instance of TravelLandAverageDepartureAndDestination from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "departure": obj.get("departure"),
            "destination": obj.get("destination"),
            "return_trip": obj.get("return_trip") if obj.get("return_trip") is not None else True,
            "passengers": obj.get("passengers") if obj.get("passengers") is not None else 1
        })
        return _obj


