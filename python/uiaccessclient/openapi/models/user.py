# coding: utf-8

"""
    UniFi Access API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uiaccessclient.openapi.models.access_policy import AccessPolicy
from uiaccessclient.openapi.models.nfc_card_reference import NfcCardReference
from uiaccessclient.openapi.models.pin_code_reference import PinCodeReference
from uiaccessclient.openapi.models.user_status import UserStatus
from typing import Optional, Set
from typing_extensions import Self

class User(BaseModel):
    """
    User
    """ # noqa: E501
    id: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = None
    last_name: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = None
    alias: Optional[StrictStr] = None
    user_email: Optional[StrictStr] = None
    email_status: Optional[StrictStr] = None
    phone: Optional[StrictStr] = None
    employee_number: Optional[StrictStr] = None
    onboard_time: Optional[StrictStr] = None
    nfc_cards: Optional[List[NfcCardReference]] = None
    pin_code: Optional[PinCodeReference] = None
    access_policy_ids: Optional[List[StrictStr]] = None
    access_policies: Optional[List[AccessPolicy]] = None
    status: Optional[UserStatus] = UserStatus.ACTIVE
    __properties: ClassVar[List[str]] = ["id", "first_name", "last_name", "full_name", "alias", "user_email", "email_status", "phone", "employee_number", "onboard_time", "nfc_cards", "pin_code", "access_policy_ids", "access_policies", "status"]

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
        """Create an instance of User from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in nfc_cards (list)
        _items = []
        if self.nfc_cards:
            for _item_nfc_cards in self.nfc_cards:
                if _item_nfc_cards:
                    _items.append(_item_nfc_cards.to_dict())
            _dict['nfc_cards'] = _items
        # override the default output from pydantic by calling `to_dict()` of pin_code
        if self.pin_code:
            _dict['pin_code'] = self.pin_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in access_policies (list)
        _items = []
        if self.access_policies:
            for _item_access_policies in self.access_policies:
                if _item_access_policies:
                    _items.append(_item_access_policies.to_dict())
            _dict['access_policies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "first_name": obj.get("first_name"),
            "last_name": obj.get("last_name"),
            "full_name": obj.get("full_name"),
            "alias": obj.get("alias"),
            "user_email": obj.get("user_email"),
            "email_status": obj.get("email_status"),
            "phone": obj.get("phone"),
            "employee_number": obj.get("employee_number"),
            "onboard_time": obj.get("onboard_time"),
            "nfc_cards": [NfcCardReference.from_dict(_item) for _item in obj["nfc_cards"]] if obj.get("nfc_cards") is not None else None,
            "pin_code": PinCodeReference.from_dict(obj["pin_code"]) if obj.get("pin_code") is not None else None,
            "access_policy_ids": obj.get("access_policy_ids"),
            "access_policies": [AccessPolicy.from_dict(_item) for _item in obj["access_policies"]] if obj.get("access_policies") is not None else None,
            "status": obj.get("status") if obj.get("status") is not None else UserStatus.ACTIVE
        })
        return _obj


