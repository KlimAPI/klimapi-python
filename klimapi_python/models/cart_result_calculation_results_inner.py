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

class CartResultCalculationResultsInner(BaseModel):
    """
    CartResultCalculationResultsInner
    """ # noqa: E501
    product_id: Optional[StrictStr] = Field(default=None, description="A unique identifier for the product")
    source: Optional[StrictStr] = Field(default=None, description="The source of the calculation")
    kg_co2e: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The amount of kg CO<sub>2</sub>e calculated for the given product.", alias="kgCO2e")
    __properties: ClassVar[List[str]] = ["product_id", "source", "kgCO2e"]

    @field_validator('source')
    def source_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['factor', 'custom', 'fallback']):
            raise ValueError("must be one of enum values ('factor', 'custom', 'fallback')")
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
        """Create an instance of CartResultCalculationResultsInner from a JSON string"""
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
        """Create an instance of CartResultCalculationResultsInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "product_id": obj.get("product_id"),
            "source": obj.get("source"),
            "kgCO2e": obj.get("kgCO2e")
        })
        return _obj


