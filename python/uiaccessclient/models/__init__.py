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
from uiaccessclient.models.access_policy_access_policies_response import AccessPolicyAccessPoliciesResponse
from uiaccessclient.models.access_policy_access_policy import AccessPolicyAccessPolicy
from uiaccessclient.models.access_policy_access_policy_response import AccessPolicyAccessPolicyResponse
from uiaccessclient.models.access_policy_create_access_policy_request import AccessPolicyCreateAccessPolicyRequest
from uiaccessclient.models.access_policy_create_holiday_group_request import AccessPolicyCreateHolidayGroupRequest
from uiaccessclient.models.access_policy_create_schedule_request import AccessPolicyCreateScheduleRequest
from uiaccessclient.models.access_policy_day_schedule import AccessPolicyDaySchedule
from uiaccessclient.models.access_policy_holiday import AccessPolicyHoliday
from uiaccessclient.models.access_policy_holiday_group import AccessPolicyHolidayGroup
from uiaccessclient.models.access_policy_holiday_group_response import AccessPolicyHolidayGroupResponse
from uiaccessclient.models.access_policy_holiday_group_summary import AccessPolicyHolidayGroupSummary
from uiaccessclient.models.access_policy_holiday_group_summary_response import AccessPolicyHolidayGroupSummaryResponse
from uiaccessclient.models.access_policy_holiday_schedule import AccessPolicyHolidaySchedule
from uiaccessclient.models.access_policy_schedule import AccessPolicySchedule
from uiaccessclient.models.access_policy_schedule_response import AccessPolicyScheduleResponse
from uiaccessclient.models.access_policy_schedules_response import AccessPolicySchedulesResponse
from uiaccessclient.models.access_policy_update_access_policy_request import AccessPolicyUpdateAccessPolicyRequest
from uiaccessclient.models.access_policy_update_holiday_group_request import AccessPolicyUpdateHolidayGroupRequest
from uiaccessclient.models.access_policy_update_schedule_request import AccessPolicyUpdateScheduleRequest
from uiaccessclient.models.access_policy_week_schedule import AccessPolicyWeekSchedule
from uiaccessclient.models.credential_enroll_nfc_card_request import CredentialEnrollNfcCardRequest
from uiaccessclient.models.credential_nfc_card import CredentialNfcCard
from uiaccessclient.models.credential_nfc_card_response import CredentialNfcCardResponse
from uiaccessclient.models.credential_nfc_card_session import CredentialNfcCardSession
from uiaccessclient.models.credential_nfc_card_session_response import CredentialNfcCardSessionResponse
from uiaccessclient.models.credential_nfc_card_token import CredentialNfcCardToken
from uiaccessclient.models.credential_nfc_card_token_response import CredentialNfcCardTokenResponse
from uiaccessclient.models.credential_nfc_cards_response import CredentialNfcCardsResponse
from uiaccessclient.models.credential_pin_code import CredentialPINCode
from uiaccessclient.models.credential_pin_code_response import CredentialPINCodeResponse
from uiaccessclient.models.credential_user import CredentialUser
from uiaccessclient.models.device_device import DeviceDevice
from uiaccessclient.models.device_devices_response import DeviceDevicesResponse
from uiaccessclient.models.shared_nfc_card import SharedNFCCard
from uiaccessclient.models.shared_pin_code import SharedPINCode
from uiaccessclient.models.shared_resource import SharedResource
from uiaccessclient.models.shared_status_code_response import SharedStatusCodeResponse
from uiaccessclient.models.space_create_door_group_request import SpaceCreateDoorGroupRequest
from uiaccessclient.models.space_door import SpaceDoor
from uiaccessclient.models.space_door_emergency_status import SpaceDoorEmergencyStatus
from uiaccessclient.models.space_door_emergency_status_response import SpaceDoorEmergencyStatusResponse
from uiaccessclient.models.space_door_locking_rule import SpaceDoorLockingRule
from uiaccessclient.models.space_door_locking_rule_response import SpaceDoorLockingRuleResponse
from uiaccessclient.models.space_door_response import SpaceDoorResponse
from uiaccessclient.models.space_door_status_response import SpaceDoorStatusResponse
from uiaccessclient.models.space_doors_response import SpaceDoorsResponse
from uiaccessclient.models.space_resource import SpaceResource
from uiaccessclient.models.space_resource_response import SpaceResourceResponse
from uiaccessclient.models.space_resource_topology import SpaceResourceTopology
from uiaccessclient.models.space_resources_response import SpaceResourcesResponse
from uiaccessclient.models.space_set_door_emergency_status_request import SpaceSetDoorEmergencyStatusRequest
from uiaccessclient.models.space_set_temporary_door_locking_rule_request import SpaceSetTemporaryDoorLockingRuleRequest
from uiaccessclient.models.space_update_door_group_request import SpaceUpdateDoorGroupRequest
from uiaccessclient.models.system_log_actor import SystemLogActor
from uiaccessclient.models.system_log_authentication import SystemLogAuthentication
from uiaccessclient.models.system_log_event import SystemLogEvent
from uiaccessclient.models.system_log_export_system_logs_request import SystemLogExportSystemLogsRequest
from uiaccessclient.models.system_log_export_system_logs_response import SystemLogExportSystemLogsResponse
from uiaccessclient.models.system_log_fetch_resources_in_system_logs_response import SystemLogFetchResourcesInSystemLogsResponse
from uiaccessclient.models.system_log_fetch_static_resources_in_system_logs_response import SystemLogFetchStaticResourcesInSystemLogsResponse
from uiaccessclient.models.system_log_fetch_system_logs_response import SystemLogFetchSystemLogsResponse
from uiaccessclient.models.system_log_resources_in_system_log import SystemLogResourcesInSystemLog
from uiaccessclient.models.system_log_system_log import SystemLogSystemLog
from uiaccessclient.models.system_log_system_log_source import SystemLogSystemLogSource
from uiaccessclient.models.system_log_system_logs import SystemLogSystemLogs
from uiaccessclient.models.system_log_target import SystemLogTarget
from uiaccessclient.models.uni_fi_identity_assign_user_group_resources_request import UniFiIdentityAssignUserGroupResourcesRequest
from uiaccessclient.models.uni_fi_identity_assign_user_resources_request import UniFiIdentityAssignUserResourcesRequest
from uiaccessclient.models.uni_fi_identity_data import UniFiIdentityData
from uiaccessclient.models.uni_fi_identity_invitation import UniFiIdentityInvitation
from uiaccessclient.models.uni_fi_identity_invitation_status import UniFiIdentityInvitationStatus
from uiaccessclient.models.uni_fi_identity_invitation_status_response import UniFiIdentityInvitationStatusResponse
from uiaccessclient.models.uni_fi_identity_resource import UniFiIdentityResource
from uiaccessclient.models.uni_fi_identity_resource_id import UniFiIdentityResourceId
from uiaccessclient.models.uni_fi_identity_resource_list import UniFiIdentityResourceList
from uiaccessclient.models.uni_fi_identity_resources_response import UniFiIdentityResourcesResponse
from uiaccessclient.models.uni_fi_identity_send_unifi_identity_invitations_request import UniFiIdentitySendUnifiIdentityInvitationsRequest
from uiaccessclient.models.user_assign_user_access_policy_request import UserAssignUserAccessPolicyRequest
from uiaccessclient.models.user_assign_user_group_access_policy_request import UserAssignUserGroupAccessPolicyRequest
from uiaccessclient.models.user_assign_user_nfc_card_request import UserAssignUserNfcCardRequest
from uiaccessclient.models.user_assign_user_pin_code_request import UserAssignUserPinCodeRequest
from uiaccessclient.models.user_assign_user_to_user_group_request import UserAssignUserToUserGroupRequest
from uiaccessclient.models.user_create_user_group_request import UserCreateUserGroupRequest
from uiaccessclient.models.user_create_user_request import UserCreateUserRequest
from uiaccessclient.models.user_status import UserStatus
from uiaccessclient.models.user_unassign_user_from_user_group_request import UserUnassignUserFromUserGroupRequest
from uiaccessclient.models.user_update_user_group_request import UserUpdateUserGroupRequest
from uiaccessclient.models.user_update_user_request import UserUpdateUserRequest
from uiaccessclient.models.user_user import UserUser
from uiaccessclient.models.user_user_group import UserUserGroup
from uiaccessclient.models.user_user_group_response import UserUserGroupResponse
from uiaccessclient.models.user_user_groups_response import UserUserGroupsResponse
from uiaccessclient.models.user_user_response import UserUserResponse
from uiaccessclient.models.user_users_response import UserUsersResponse
from uiaccessclient.models.visitor_assign_visitor_pin_code_request import VisitorAssignVisitorPinCodeRequest
from uiaccessclient.models.visitor_create_visitor_request import VisitorCreateVisitorRequest
from uiaccessclient.models.visitor_status import VisitorStatus
from uiaccessclient.models.visitor_unassign_visitor_nfc_card_request import VisitorUnassignVisitorNfcCardRequest
from uiaccessclient.models.visitor_update_visitor_request import VisitorUpdateVisitorRequest
from uiaccessclient.models.visitor_visitor import VisitorVisitor
from uiaccessclient.models.visitor_visitor_response import VisitorVisitorResponse
from uiaccessclient.models.visitor_visitors_response import VisitorVisitorsResponse