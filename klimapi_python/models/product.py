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

class Product(BaseModel):
    """
    A specific product element
    """ # noqa: E501
    product_id: StrictStr = Field(description="A unique identifier for the product")
    name: Optional[StrictStr] = Field(default=None, description="The name of the product")
    description: Optional[StrictStr] = Field(default=None, description="A description of the product")
    price: Union[StrictFloat, StrictInt] = Field(description="The price of the product")
    categories: Optional[List[StrictStr]] = Field(default=None, description="The categories of the product")
    tags: Optional[List[StrictStr]] = Field(default=None, description="The tags of the product")
    weight: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The weight of the product")
    weight_unit: Optional[StrictStr] = Field(default='kg', description="The weight unit of the product")
    made_in: Optional[StrictStr] = Field(default=None, description="The country of origin of the product")
    emission_factor: Optional[StrictStr] = Field(default=None, description="Already know the emissions of the given product? Then you can provide the emission factor here. Unit: **kg CO<sub>2</sub>e**")
    emission_multiplicator: Optional[StrictStr] = Field(default=None, description="Include the multiplicator of the given factor.")
    __properties: ClassVar[List[str]] = ["product_id", "name", "description", "price", "categories", "tags", "weight", "weight_unit", "made_in", "emission_factor", "emission_multiplicator"]

    @field_validator('weight_unit')
    def weight_unit_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['t', 'kg', 'g', 'lb', 'lbs', 'oz']):
            raise ValueError("must be one of enum values ('t', 'kg', 'g', 'lb', 'lbs', 'oz')")
        return value

    @field_validator('emission_multiplicator')
    def emission_multiplicator_validate_enum(cls, value):
        """Validates the enum"""
        if value is None:
            return value

        if value not in set(['price', 'amount', 'weight']):
            raise ValueError("must be one of enum values ('price', 'amount', 'weight')")
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
        """Create an instance of Product from a JSON string"""
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
        """Create an instance of Product from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "product_id": obj.get("product_id"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "price": obj.get("price"),
            "categories": obj.get("categories"),
            "tags": obj.get("tags"),
            "weight": obj.get("weight"),
            "weight_unit": obj.get("weight_unit") if obj.get("weight_unit") is not None else 'kg',
            "made_in": obj.get("made_in"),
            "emission_factor": obj.get("emission_factor"),
            "emission_multiplicator": obj.get("emission_multiplicator")
        })
        return _obj


