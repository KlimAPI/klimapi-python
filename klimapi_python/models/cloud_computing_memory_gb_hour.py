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

class CloudComputingMemoryGbHour(BaseModel):
    """
    CloudComputingMemoryGbHour
    """ # noqa: E501
    type: StrictStr
    activity: Optional[StrictStr] = 'memory'
    specification: Optional[StrictStr] = 'average'
    detail: Optional[StrictStr] = Field(default='average', description=" **Hint:** Some specifications only support certain details.")
    value: Union[StrictFloat, StrictInt] = Field(description="The value in the given unit")
    unit: Optional[StrictStr] = Field(default='gb-hour', description="Need another unit? Contact us!")
    __properties: ClassVar[List[str]] = ["type", "activity", "specification", "detail", "value", "unit"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['cloud_computing']):
            raise ValueError("must be one of enum values ('cloud_computing')")
        return value

    @field_validator('specification')
    def specification_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['aws', 'azure', 'gcp', 'average']):
            raise ValueError("must be one of enum values ('aws', 'azure', 'gcp', 'average')")
        return value

    @field_validator('detail')
    def detail_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-north-1', 'eu-south-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-west-1', 'us-west-2', 'average', 'central-india', 'central-us', 'east-asia', 'east-us-2', 'east-us-3', 'east-us', 'north-central-us', 'north-europe', 'south-central-us', 'south-india', 'southeast-asia', 'uk-south', 'uk-west', 'west-central-us', 'west-europe', 'west-india', 'west-us-2', 'west-us-3', 'west-us', 'asia-east-1', 'asia-east-2', 'asia-northeast-1', 'asia-northeast-2', 'asia-northeast-3', 'asia-south-1', 'asia-southeast-1', 'asia-southeast-2', 'australia-southeast-1', 'europe-north-1', 'europe-west-1', 'europe-west-2', 'europe-west-3', 'europe-west-4', 'europe-west-6', 'northamerica-northeast-1', 'southamerica-east-1', 'us-central-1', 'us-east-4', 'us-west-3', 'us-west-4']):
            raise ValueError("must be one of enum values ('af-south-1', 'ap-east-1', 'ap-northeast-1', 'ap-northeast-2', 'ap-northeast-3', 'ap-south-1', 'ap-southeast-1', 'ap-southeast-2', 'ca-central-1', 'cn-north-1', 'cn-northwest-1', 'eu-central-1', 'eu-north-1', 'eu-south-1', 'eu-west-1', 'eu-west-2', 'eu-west-3', 'me-south-1', 'sa-east-1', 'us-east-1', 'us-east-2', 'us-gov-east-1', 'us-gov-west-1', 'us-west-1', 'us-west-2', 'average', 'central-india', 'central-us', 'east-asia', 'east-us-2', 'east-us-3', 'east-us', 'north-central-us', 'north-europe', 'south-central-us', 'south-india', 'southeast-asia', 'uk-south', 'uk-west', 'west-central-us', 'west-europe', 'west-india', 'west-us-2', 'west-us-3', 'west-us', 'asia-east-1', 'asia-east-2', 'asia-northeast-1', 'asia-northeast-2', 'asia-northeast-3', 'asia-south-1', 'asia-southeast-1', 'asia-southeast-2', 'australia-southeast-1', 'europe-north-1', 'europe-west-1', 'europe-west-2', 'europe-west-3', 'europe-west-4', 'europe-west-6', 'northamerica-northeast-1', 'southamerica-east-1', 'us-central-1', 'us-east-4', 'us-west-3', 'us-west-4')")
        return value

    @field_validator('unit')
    def unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['gb-hour']):
            raise ValueError("must be one of enum values ('gb-hour')")
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
        """Create an instance of CloudComputingMemoryGbHour from a JSON string"""
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
        """Create an instance of CloudComputingMemoryGbHour from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "activity": obj.get("activity") if obj.get("activity") is not None else 'memory',
            "specification": obj.get("specification") if obj.get("specification") is not None else 'average',
            "detail": obj.get("detail") if obj.get("detail") is not None else 'average',
            "value": obj.get("value"),
            "unit": obj.get("unit") if obj.get("unit") is not None else 'gb-hour'
        })
        return _obj


