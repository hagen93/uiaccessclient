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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from uiaccessclient.models.access_policy_access_policy import AccessPolicyAccessPolicy
from uiaccessclient.models.shared_nfc_card import SharedNFCCard
from uiaccessclient.models.shared_pin_code import SharedPINCode
from uiaccessclient.models.user_status import UserStatus
from typing import Optional, Set
from typing_extensions import Self

class UserUser(BaseModel):
    """
    UserUser
    """ # noqa: E501
    id: Optional[StrictStr] = None
    first_name: Optional[StrictStr] = Field(default=None, alias="firstName")
    last_name: Optional[StrictStr] = Field(default=None, alias="lastName")
    full_name: Optional[StrictStr] = Field(default=None, alias="fullName")
    alias: Optional[StrictStr] = None
    user_email: Optional[StrictStr] = Field(default=None, alias="userEmail")
    email_status: Optional[StrictStr] = Field(default=None, alias="emailStatus")
    phone: Optional[StrictStr] = None
    employee_number: Optional[StrictStr] = Field(default=None, alias="employeeNumber")
    onboard_time: Optional[StrictStr] = Field(default=None, alias="onboardTime")
    nfc_cards: Optional[List[SharedNFCCard]] = Field(default=None, alias="nfcCards")
    pin_code: Optional[SharedPINCode] = Field(default=None, alias="pinCode")
    access_policy_ids: Optional[List[StrictStr]] = Field(default=None, alias="accessPolicyIds")
    access_policies: Optional[List[AccessPolicyAccessPolicy]] = Field(default=None, alias="accessPolicies")
    status: Optional[UserStatus] = UserStatus.ACTIVE
    __properties: ClassVar[List[str]] = ["id", "firstName", "lastName", "fullName", "alias", "userEmail", "emailStatus", "phone", "employeeNumber", "onboardTime", "nfcCards", "pinCode", "accessPolicyIds", "accessPolicies", "status"]

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
        """Create an instance of UserUser from a JSON string"""
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
            _dict['nfcCards'] = _items
        # override the default output from pydantic by calling `to_dict()` of pin_code
        if self.pin_code:
            _dict['pinCode'] = self.pin_code.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in access_policies (list)
        _items = []
        if self.access_policies:
            for _item_access_policies in self.access_policies:
                if _item_access_policies:
                    _items.append(_item_access_policies.to_dict())
            _dict['accessPolicies'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserUser from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "firstName": obj.get("firstName"),
            "lastName": obj.get("lastName"),
            "fullName": obj.get("fullName"),
            "alias": obj.get("alias"),
            "userEmail": obj.get("userEmail"),
            "emailStatus": obj.get("emailStatus"),
            "phone": obj.get("phone"),
            "employeeNumber": obj.get("employeeNumber"),
            "onboardTime": obj.get("onboardTime"),
            "nfcCards": [SharedNFCCard.from_dict(_item) for _item in obj["nfcCards"]] if obj.get("nfcCards") is not None else None,
            "pinCode": SharedPINCode.from_dict(obj["pinCode"]) if obj.get("pinCode") is not None else None,
            "accessPolicyIds": obj.get("accessPolicyIds"),
            "accessPolicies": [AccessPolicyAccessPolicy.from_dict(_item) for _item in obj["accessPolicies"]] if obj.get("accessPolicies") is not None else None,
            "status": obj.get("status") if obj.get("status") is not None else UserStatus.ACTIVE
        })
        return _obj


