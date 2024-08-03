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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from klimapi_python.models.get_orders_request_filters import GetOrdersRequestFilters
from typing import Optional, Set
from typing_extensions import Self

class GetOrdersRequest(BaseModel):
    """
    GetOrdersRequest
    """ # noqa: E501
    operator: Optional[StrictStr] = Field(default='AND', description="The operator to combine the filters with")
    filters: Optional[GetOrdersRequestFilters] = None
    limit: Optional[Annotated[int, Field(le=100, strict=True, ge=1)]] = Field(default=10, description="The maximum amount of orders you want to receive")
    skip: Optional[StrictInt] = Field(default=0, description="The amount of orders you want to skip")
    __properties: ClassVar[List[str]] = ["operator", "filters", "limit", "skip"]

    @field_validator('operator')
    def operator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['AND', 'OR']):
            raise ValueError("must be one of enum values ('AND', 'OR')")
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
        """Create an instance of GetOrdersRequest from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of filters
        if self.filters:
            _dict['filters'] = self.filters.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of GetOrdersRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "operator": obj.get("operator") if obj.get("operator") is not None else 'AND',
            "filters": GetOrdersRequestFilters.from_dict(obj["filters"]) if obj.get("filters") is not None else None,
            "limit": obj.get("limit") if obj.get("limit") is not None else 10,
            "skip": obj.get("skip") if obj.get("skip") is not None else 0
        })
        return _obj


