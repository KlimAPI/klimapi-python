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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class InvoiceDetailsTaxId(BaseModel):
    """
    The customer’s tax ID.
    """ # noqa: E501
    type: StrictStr = Field(description="Type of the tax ID")
    value: StrictStr = Field(description="Value of the tax ID")
    __properties: ClassVar[List[str]] = ["type", "value"]

    @field_validator('type')
    def type_validate_enum(cls, value):
        """Validates the enum"""
        if value not in set(['eu_vat', 'gb_vat', 'us_ein', 'ad_nrt', 'ae_trn', 'ar_cuit', 'au_abn', 'au_arn', 'bg_uic', 'bh_vat', 'bo_tin', 'br_cnpj', 'br_cpf', 'ca_bn', 'ca_gst_hst', 'ca_pst_bc', 'ca_pst_mb', 'ca_pst_sk', 'ca_qst', 'ch_uid', 'ch_vat', 'cl_tin', 'co_nit', 'cr_tin', 'de_stn', 'do_rcn', 'ec_ruc', 'eg_tin', 'es_cif', 'eu_oss_vat', 'ge_vat', 'hu_tin', 'id_npwp', 'il_vat', 'in_gst', 'is_vat', 'jp_cn', 'jp_rn', 'jp_trn', 'ke_pin', 'kr_brn', 'kz_bin', 'li_uid', 'mx_rfc', 'my_frp', 'my_itn', 'my_sst', 'ng_tin', 'no_vat', 'no_voec', 'nz_gst', 'om_vat', 'pe_ruc', 'ph_tin', 'ro_tin', 'rs_pib', 'ru_kpp', 'sa_vat', 'sg_gst', 'sg_uen', 'si_tin', 'sv_nit', 'th_vat', 'tr_tin', 'tw_vat', 'ua_vat', 'uy_ruc', 've_rif', 'vn_tin', 'za_vat']):
            raise ValueError("must be one of enum values ('eu_vat', 'gb_vat', 'us_ein', 'ad_nrt', 'ae_trn', 'ar_cuit', 'au_abn', 'au_arn', 'bg_uic', 'bh_vat', 'bo_tin', 'br_cnpj', 'br_cpf', 'ca_bn', 'ca_gst_hst', 'ca_pst_bc', 'ca_pst_mb', 'ca_pst_sk', 'ca_qst', 'ch_uid', 'ch_vat', 'cl_tin', 'co_nit', 'cr_tin', 'de_stn', 'do_rcn', 'ec_ruc', 'eg_tin', 'es_cif', 'eu_oss_vat', 'ge_vat', 'hu_tin', 'id_npwp', 'il_vat', 'in_gst', 'is_vat', 'jp_cn', 'jp_rn', 'jp_trn', 'ke_pin', 'kr_brn', 'kz_bin', 'li_uid', 'mx_rfc', 'my_frp', 'my_itn', 'my_sst', 'ng_tin', 'no_vat', 'no_voec', 'nz_gst', 'om_vat', 'pe_ruc', 'ph_tin', 'ro_tin', 'rs_pib', 'ru_kpp', 'sa_vat', 'sg_gst', 'sg_uen', 'si_tin', 'sv_nit', 'th_vat', 'tr_tin', 'tw_vat', 'ua_vat', 'uy_ruc', 've_rif', 'vn_tin', 'za_vat')")
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
        """Create an instance of InvoiceDetailsTaxId from a JSON string"""
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
        """Create an instance of InvoiceDetailsTaxId from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "type": obj.get("type"),
            "value": obj.get("value")
        })
        return _obj


