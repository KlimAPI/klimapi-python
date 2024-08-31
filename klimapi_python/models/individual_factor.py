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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class IndividualFactor(BaseModel):
    """
    IndividualFactor
    """ # noqa: E501
    type: StrictStr
    activity: StrictStr = Field(description="Describe the individual factor")
    specification: StrictStr = Field(description="Specify the individual factor")
    unit: StrictStr = Field(description="Describe the unit used by the multiplier")
    amount: Annotated[int, Field(strict=True, ge=1)] = Field(description="The amount of kg CO*2*e you want to add to the calculation.")
    multiplier: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=1, description="Multiplier for the given amount")
    __properties: ClassVar[List[str]] = ["type", "activity", "specification", "unit", "amount", "multiplier"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['individual_factor']):
            raise ValueError("must be one of enum values ('individual_factor')")
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
        """Create an instance of IndividualFactor from a JSON string"""
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
        """Create an instance of IndividualFactor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "activity": obj.get("activity"),
            "specification": obj.get("specification"),
            "unit": obj.get("unit"),
            "amount": obj.get("amount"),
            "multiplier": obj.get("multiplier") if obj.get("multiplier") is not None else 1
        })
        return _obj


