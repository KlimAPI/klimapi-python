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

from pydantic import BaseModel, ConfigDict, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class Project(BaseModel):
    """
    Project
    """ # noqa: E501
    id: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    summary: Optional[StrictStr] = None
    status: Optional[StrictStr] = None
    category_id: Optional[StrictInt] = None
    certification_authority_id: Optional[StrictInt] = None
    country: Optional[StrictStr] = None
    description: Optional[StrictStr] = None
    goals: Optional[StrictStr] = None
    images: Optional[List[StrictStr]] = None
    benefits: Optional[List[StrictInt]] = None
    __properties: ClassVar[List[str]] = ["id", "title", "summary", "status", "category_id", "certification_authority_id", "country", "description", "goals", "images", "benefits"]

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
        """Create an instance of Project from a JSON string"""
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
        """Create an instance of Project from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "title": obj.get("title"),
            "summary": obj.get("summary"),
            "status": obj.get("status"),
            "category_id": obj.get("category_id"),
            "certification_authority_id": obj.get("certification_authority_id"),
            "country": obj.get("country"),
            "description": obj.get("description"),
            "goals": obj.get("goals"),
            "images": obj.get("images"),
            "benefits": obj.get("benefits")
        })
        return _obj

