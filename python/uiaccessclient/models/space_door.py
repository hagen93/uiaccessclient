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
from typing import Optional, Set
from typing_extensions import Self

class SpaceDoor(BaseModel):
    """
    SpaceDoor
    """ # noqa: E501
    id: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    full_name: Optional[StrictStr] = Field(default=None, alias="fullName")
    floor_id: Optional[StrictStr] = Field(default=None, alias="floorId")
    type: Optional[StrictStr] = None
    is_bind_hub: Optional[StrictStr] = Field(default=None, alias="isBindHub")
    door_lock_relay_status: Optional[StrictStr] = Field(default=None, description="used for remote opening if it's bound.  Door lock status. enum door_lock_relay_status {lock,unlock}", alias="doorLockRelayStatus")
    door_position_status: Optional[StrictStr] = Field(default=None, alias="doorPositionStatus")
    __properties: ClassVar[List[str]] = ["id", "name", "fullName", "floorId", "type", "isBindHub", "doorLockRelayStatus", "doorPositionStatus"]

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
        """Create an instance of SpaceDoor from a JSON string"""
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
        """Create an instance of SpaceDoor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "fullName": obj.get("fullName"),
            "floorId": obj.get("floorId"),
            "type": obj.get("type"),
            "isBindHub": obj.get("isBindHub"),
            "doorLockRelayStatus": obj.get("doorLockRelayStatus"),
            "doorPositionStatus": obj.get("doorPositionStatus")
        })
        return _obj


