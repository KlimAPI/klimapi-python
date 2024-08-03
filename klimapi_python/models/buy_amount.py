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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class BuyAmount(BaseModel):
    """
    BuyAmount
    """ # noqa: E501
    kg_co2e: StrictInt = Field(description="The amount of kg CO<sub>2</sub>e the compensation should provide", alias="kgCO2e")
    recipient_name: StrictStr = Field(description="The name which should be associated with the compensation")
    recipient_email: Optional[StrictStr] = Field(default=None, description="If a valid e-mail address is provided, we will send the certificate to this address")
    send_at: Optional[datetime] = Field(default=None, description="Timestamp of when the certificate should be send to the customer in ISO 8601 format (UTC). Defaults to the current timestamp.")
    price_limit: Optional[Union[Annotated[float, Field(strict=True, ge=0.5)], Annotated[int, Field(strict=True, ge=1)]]] = Field(default=None, description="Set an optional price limit. if the order would exceed the limit a error will be thrown. Set the limit in the given currency.")
    metadata: Optional[Dict[str, StrictStr]] = Field(default=None, description="Add additional queryable information to the order as key-value pairs")
    __properties: ClassVar[List[str]] = ["kgCO2e", "recipient_name", "recipient_email", "send_at", "price_limit", "metadata"]

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
        """Create an instance of BuyAmount from a JSON string"""
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
        """Create an instance of BuyAmount from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "kgCO2e": obj.get("kgCO2e"),
            "recipient_name": obj.get("recipient_name"),
            "recipient_email": obj.get("recipient_email"),
            "send_at": obj.get("send_at"),
            "price_limit": obj.get("price_limit"),
            "metadata": obj.get("metadata")
        })
        return _obj

