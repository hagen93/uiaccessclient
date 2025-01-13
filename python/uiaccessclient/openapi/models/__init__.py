# coding: utf-8

# flake8: noqa
"""
    UniFi Access API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from uiaccessclient.openapi.models.access_policies_response import AccessPoliciesResponse
from uiaccessclient.openapi.models.access_policy import AccessPolicy
from uiaccessclient.openapi.models.access_policy_day_schedule import AccessPolicyDaySchedule
from uiaccessclient.openapi.models.access_policy_holiday import AccessPolicyHoliday
from uiaccessclient.openapi.models.access_policy_holiday_group import AccessPolicyHolidayGroup
from uiaccessclient.openapi.models.access_policy_holiday_group_response import AccessPolicyHolidayGroupResponse
from uiaccessclient.openapi.models.access_policy_holiday_group_summary import AccessPolicyHolidayGroupSummary
from uiaccessclient.openapi.models.access_policy_holiday_group_summary_response import AccessPolicyHolidayGroupSummaryResponse
from uiaccessclient.openapi.models.access_policy_holiday_schedule import AccessPolicyHolidaySchedule
from uiaccessclient.openapi.models.access_policy_response import AccessPolicyResponse
from uiaccessclient.openapi.models.access_policy_schedule import AccessPolicySchedule
from uiaccessclient.openapi.models.access_policy_schedule_response import AccessPolicyScheduleResponse
from uiaccessclient.openapi.models.access_policy_schedules_response import AccessPolicySchedulesResponse
from uiaccessclient.openapi.models.access_policy_week_schedule import AccessPolicyWeekSchedule
from uiaccessclient.openapi.models.assign_uni_fi_identity_user_group_resources_request import AssignUniFiIdentityUserGroupResourcesRequest
from uiaccessclient.openapi.models.assign_uni_fi_identity_user_resources_request import AssignUniFiIdentityUserResourcesRequest
from uiaccessclient.openapi.models.assign_user_access_policy_request import AssignUserAccessPolicyRequest
from uiaccessclient.openapi.models.assign_user_group_access_policy_request import AssignUserGroupAccessPolicyRequest
from uiaccessclient.openapi.models.assign_user_nfc_card_request import AssignUserNfcCardRequest
from uiaccessclient.openapi.models.assign_user_pin_code_request import AssignUserPinCodeRequest
from uiaccessclient.openapi.models.assign_user_to_user_group_request import AssignUserToUserGroupRequest
from uiaccessclient.openapi.models.assign_visitor_pin_code_request import AssignVisitorPinCodeRequest
from uiaccessclient.openapi.models.create_access_policy_holiday_group_request import CreateAccessPolicyHolidayGroupRequest
from uiaccessclient.openapi.models.create_access_policy_request import CreateAccessPolicyRequest
from uiaccessclient.openapi.models.create_access_policy_schedule_request import CreateAccessPolicyScheduleRequest
from uiaccessclient.openapi.models.create_door_group_request import CreateDoorGroupRequest
from uiaccessclient.openapi.models.create_user_group_request import CreateUserGroupRequest
from uiaccessclient.openapi.models.create_user_request import CreateUserRequest
from uiaccessclient.openapi.models.create_visitor_request import CreateVisitorRequest
from uiaccessclient.openapi.models.device import Device
from uiaccessclient.openapi.models.devices_response import DevicesResponse
from uiaccessclient.openapi.models.door import Door
from uiaccessclient.openapi.models.door_emergency_status import DoorEmergencyStatus
from uiaccessclient.openapi.models.door_emergency_status_response import DoorEmergencyStatusResponse
from uiaccessclient.openapi.models.door_locking_rule import DoorLockingRule
from uiaccessclient.openapi.models.door_locking_rule_response import DoorLockingRuleResponse
from uiaccessclient.openapi.models.door_response import DoorResponse
from uiaccessclient.openapi.models.door_status_response import DoorStatusResponse
from uiaccessclient.openapi.models.doors_response import DoorsResponse
from uiaccessclient.openapi.models.enroll_nfc_card_request import EnrollNfcCardRequest
from uiaccessclient.openapi.models.error_response import ErrorResponse
from uiaccessclient.openapi.models.export_system_logs_request import ExportSystemLogsRequest
from uiaccessclient.openapi.models.fetch_resources_in_system_logs_response import FetchResourcesInSystemLogsResponse
from uiaccessclient.openapi.models.fetch_system_logs_request import FetchSystemLogsRequest
from uiaccessclient.openapi.models.fetch_system_logs_response import FetchSystemLogsResponse
from uiaccessclient.openapi.models.nfc_card import NfcCard
from uiaccessclient.openapi.models.nfc_card_reference import NfcCardReference
from uiaccessclient.openapi.models.nfc_card_response import NfcCardResponse
from uiaccessclient.openapi.models.nfc_card_session import NfcCardSession
from uiaccessclient.openapi.models.nfc_card_session_response import NfcCardSessionResponse
from uiaccessclient.openapi.models.nfc_card_token import NfcCardToken
from uiaccessclient.openapi.models.nfc_card_token_response import NfcCardTokenResponse
from uiaccessclient.openapi.models.nfc_card_user import NfcCardUser
from uiaccessclient.openapi.models.nfc_cards_response import NfcCardsResponse
from uiaccessclient.openapi.models.pin_code import PinCode
from uiaccessclient.openapi.models.pin_code_reference import PinCodeReference
from uiaccessclient.openapi.models.pin_code_response import PinCodeResponse
from uiaccessclient.openapi.models.resource import Resource
from uiaccessclient.openapi.models.resources_in_system_log import ResourcesInSystemLog
from uiaccessclient.openapi.models.send_uni_fi_identity_invitations_request import SendUniFiIdentityInvitationsRequest
from uiaccessclient.openapi.models.set_door_emergency_status_request import SetDoorEmergencyStatusRequest
from uiaccessclient.openapi.models.set_temporary_door_locking_rule_request import SetTemporaryDoorLockingRuleRequest
from uiaccessclient.openapi.models.space_resource import SpaceResource
from uiaccessclient.openapi.models.space_resource_response import SpaceResourceResponse
from uiaccessclient.openapi.models.space_resource_topology import SpaceResourceTopology
from uiaccessclient.openapi.models.space_resources_response import SpaceResourcesResponse
from uiaccessclient.openapi.models.success_response import SuccessResponse
from uiaccessclient.openapi.models.system_log import SystemLog
from uiaccessclient.openapi.models.system_log_source import SystemLogSource
from uiaccessclient.openapi.models.system_log_source_actor import SystemLogSourceActor
from uiaccessclient.openapi.models.system_log_source_authentication import SystemLogSourceAuthentication
from uiaccessclient.openapi.models.system_log_source_event import SystemLogSourceEvent
from uiaccessclient.openapi.models.system_logs import SystemLogs
from uiaccessclient.openapi.models.unassign_user_from_user_group_request import UnassignUserFromUserGroupRequest
from uiaccessclient.openapi.models.unassign_visitor_nfc_card_request import UnassignVisitorNfcCardRequest
from uiaccessclient.openapi.models.uni_fi_identity_data import UniFiIdentityData
from uiaccessclient.openapi.models.uni_fi_identity_invitation import UniFiIdentityInvitation
from uiaccessclient.openapi.models.uni_fi_identity_invitation_status import UniFiIdentityInvitationStatus
from uiaccessclient.openapi.models.uni_fi_identity_invitation_status_response import UniFiIdentityInvitationStatusResponse
from uiaccessclient.openapi.models.uni_fi_identity_resource_id import UniFiIdentityResourceId
from uiaccessclient.openapi.models.uni_fi_identity_resource_list import UniFiIdentityResourceList
from uiaccessclient.openapi.models.uni_fi_identity_resource_list_resources_inner import UniFiIdentityResourceListResourcesInner
from uiaccessclient.openapi.models.uni_fi_identity_resources_response import UniFiIdentityResourcesResponse
from uiaccessclient.openapi.models.update_access_policy_holiday_group_request import UpdateAccessPolicyHolidayGroupRequest
from uiaccessclient.openapi.models.update_access_policy_request import UpdateAccessPolicyRequest
from uiaccessclient.openapi.models.update_access_policy_schedule_request import UpdateAccessPolicyScheduleRequest
from uiaccessclient.openapi.models.update_door_group_request import UpdateDoorGroupRequest
from uiaccessclient.openapi.models.update_user_group_request import UpdateUserGroupRequest
from uiaccessclient.openapi.models.update_user_request import UpdateUserRequest
from uiaccessclient.openapi.models.update_visitor_request import UpdateVisitorRequest
from uiaccessclient.openapi.models.user import User
from uiaccessclient.openapi.models.user_group import UserGroup
from uiaccessclient.openapi.models.user_group_response import UserGroupResponse
from uiaccessclient.openapi.models.user_groups_response import UserGroupsResponse
from uiaccessclient.openapi.models.user_response import UserResponse
from uiaccessclient.openapi.models.user_status import UserStatus
from uiaccessclient.openapi.models.users_response import UsersResponse
from uiaccessclient.openapi.models.visitor import Visitor
from uiaccessclient.openapi.models.visitor_response import VisitorResponse
from uiaccessclient.openapi.models.visitors_response import VisitorsResponse
