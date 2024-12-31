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

from pydantic import BaseModel, ConfigDict
from typing import Any, ClassVar, Dict, List, Optional
from uiaccessclient.models.system_log_actor import SystemLogActor
from uiaccessclient.models.system_log_authentication import SystemLogAuthentication
from uiaccessclient.models.system_log_event import SystemLogEvent
from uiaccessclient.models.system_log_target import SystemLogTarget
from typing import Optional, Set
from typing_extensions import Self

class SystemLogSystemLogSource(BaseModel):
    """
    SystemLogSystemLogSource
    """ # noqa: E501
    actor: Optional[SystemLogActor] = None
    event: Optional[SystemLogEvent] = None
    authentication: Optional[SystemLogAuthentication] = None
    target: Optional[List[SystemLogTarget]] = None
    __properties: ClassVar[List[str]] = ["actor", "event", "authentication", "target"]

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
        """Create an instance of SystemLogSystemLogSource from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of actor
        if self.actor:
            _dict['actor'] = self.actor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of event
        if self.event:
            _dict['event'] = self.event.to_dict()
        # override the default output from pydantic by calling `to_dict()` of authentication
        if self.authentication:
            _dict['authentication'] = self.authentication.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in target (list)
        _items = []
        if self.target:
            for _item_target in self.target:
                if _item_target:
                    _items.append(_item_target.to_dict())
            _dict['target'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SystemLogSystemLogSource from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "actor": SystemLogActor.from_dict(obj["actor"]) if obj.get("actor") is not None else None,
            "event": SystemLogEvent.from_dict(obj["event"]) if obj.get("event") is not None else None,
            "authentication": SystemLogAuthentication.from_dict(obj["authentication"]) if obj.get("authentication") is not None else None,
            "target": [SystemLogTarget.from_dict(_item) for _item in obj["target"]] if obj.get("target") is not None else None
        })
        return _obj


