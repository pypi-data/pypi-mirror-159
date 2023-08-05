"""
Type annotations for chime-sdk-meetings service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_chime_sdk_meetings/type_defs/)

Usage::

    ```python
    from types_aiobotocore_chime_sdk_meetings.type_defs import AttendeeTypeDef

    data: AttendeeTypeDef = {...}
    ```
"""
import sys
from typing import Dict, List, Sequence

from .literals import (
    MeetingFeatureStatusType,
    TranscribeLanguageCodeType,
    TranscribeMedicalRegionType,
    TranscribeMedicalSpecialtyType,
    TranscribeMedicalTypeType,
    TranscribePartialResultsStabilityType,
    TranscribeRegionType,
    TranscribeVocabularyFilterMethodType,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal
if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "AttendeeTypeDef",
    "AudioFeaturesTypeDef",
    "CreateAttendeeRequestItemTypeDef",
    "CreateAttendeeErrorTypeDef",
    "ResponseMetadataTypeDef",
    "CreateAttendeeRequestRequestTypeDef",
    "NotificationsConfigurationTypeDef",
    "DeleteAttendeeRequestRequestTypeDef",
    "DeleteMeetingRequestRequestTypeDef",
    "EngineTranscribeMedicalSettingsTypeDef",
    "EngineTranscribeSettingsTypeDef",
    "GetAttendeeRequestRequestTypeDef",
    "GetMeetingRequestRequestTypeDef",
    "ListAttendeesRequestRequestTypeDef",
    "MediaPlacementTypeDef",
    "StopMeetingTranscriptionRequestRequestTypeDef",
    "MeetingFeaturesConfigurationTypeDef",
    "BatchCreateAttendeeRequestRequestTypeDef",
    "BatchCreateAttendeeResponseTypeDef",
    "CreateAttendeeResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "GetAttendeeResponseTypeDef",
    "ListAttendeesResponseTypeDef",
    "TranscriptionConfigurationTypeDef",
    "CreateMeetingRequestRequestTypeDef",
    "CreateMeetingWithAttendeesRequestRequestTypeDef",
    "MeetingTypeDef",
    "StartMeetingTranscriptionRequestRequestTypeDef",
    "CreateMeetingResponseTypeDef",
    "CreateMeetingWithAttendeesResponseTypeDef",
    "GetMeetingResponseTypeDef",
)

AttendeeTypeDef = TypedDict(
    "AttendeeTypeDef",
    {
        "ExternalUserId": str,
        "AttendeeId": str,
        "JoinToken": str,
    },
    total=False,
)

AudioFeaturesTypeDef = TypedDict(
    "AudioFeaturesTypeDef",
    {
        "EchoReduction": MeetingFeatureStatusType,
    },
    total=False,
)

CreateAttendeeRequestItemTypeDef = TypedDict(
    "CreateAttendeeRequestItemTypeDef",
    {
        "ExternalUserId": str,
    },
)

CreateAttendeeErrorTypeDef = TypedDict(
    "CreateAttendeeErrorTypeDef",
    {
        "ExternalUserId": str,
        "ErrorCode": str,
        "ErrorMessage": str,
    },
    total=False,
)

ResponseMetadataTypeDef = TypedDict(
    "ResponseMetadataTypeDef",
    {
        "RequestId": str,
        "HostId": str,
        "HTTPStatusCode": int,
        "HTTPHeaders": Dict[str, str],
        "RetryAttempts": int,
    },
)

CreateAttendeeRequestRequestTypeDef = TypedDict(
    "CreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "ExternalUserId": str,
    },
)

NotificationsConfigurationTypeDef = TypedDict(
    "NotificationsConfigurationTypeDef",
    {
        "LambdaFunctionArn": str,
        "SnsTopicArn": str,
        "SqsQueueArn": str,
    },
    total=False,
)

DeleteAttendeeRequestRequestTypeDef = TypedDict(
    "DeleteAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

DeleteMeetingRequestRequestTypeDef = TypedDict(
    "DeleteMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

_RequiredEngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "_RequiredEngineTranscribeMedicalSettingsTypeDef",
    {
        "LanguageCode": Literal["en-US"],
        "Specialty": TranscribeMedicalSpecialtyType,
        "Type": TranscribeMedicalTypeType,
    },
)
_OptionalEngineTranscribeMedicalSettingsTypeDef = TypedDict(
    "_OptionalEngineTranscribeMedicalSettingsTypeDef",
    {
        "VocabularyName": str,
        "Region": TranscribeMedicalRegionType,
        "ContentIdentificationType": Literal["PHI"],
    },
    total=False,
)

class EngineTranscribeMedicalSettingsTypeDef(
    _RequiredEngineTranscribeMedicalSettingsTypeDef, _OptionalEngineTranscribeMedicalSettingsTypeDef
):
    pass

EngineTranscribeSettingsTypeDef = TypedDict(
    "EngineTranscribeSettingsTypeDef",
    {
        "LanguageCode": TranscribeLanguageCodeType,
        "VocabularyFilterMethod": TranscribeVocabularyFilterMethodType,
        "VocabularyFilterName": str,
        "VocabularyName": str,
        "Region": TranscribeRegionType,
        "EnablePartialResultsStabilization": bool,
        "PartialResultsStability": TranscribePartialResultsStabilityType,
        "ContentIdentificationType": Literal["PII"],
        "ContentRedactionType": Literal["PII"],
        "PiiEntityTypes": str,
        "LanguageModelName": str,
        "IdentifyLanguage": bool,
        "LanguageOptions": str,
        "PreferredLanguage": TranscribeLanguageCodeType,
    },
    total=False,
)

GetAttendeeRequestRequestTypeDef = TypedDict(
    "GetAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "AttendeeId": str,
    },
)

GetMeetingRequestRequestTypeDef = TypedDict(
    "GetMeetingRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

_RequiredListAttendeesRequestRequestTypeDef = TypedDict(
    "_RequiredListAttendeesRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)
_OptionalListAttendeesRequestRequestTypeDef = TypedDict(
    "_OptionalListAttendeesRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
    },
    total=False,
)

class ListAttendeesRequestRequestTypeDef(
    _RequiredListAttendeesRequestRequestTypeDef, _OptionalListAttendeesRequestRequestTypeDef
):
    pass

MediaPlacementTypeDef = TypedDict(
    "MediaPlacementTypeDef",
    {
        "AudioHostUrl": str,
        "AudioFallbackUrl": str,
        "SignalingUrl": str,
        "TurnControlUrl": str,
        "ScreenDataUrl": str,
        "ScreenViewingUrl": str,
        "ScreenSharingUrl": str,
        "EventIngestionUrl": str,
    },
    total=False,
)

StopMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StopMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
    },
)

MeetingFeaturesConfigurationTypeDef = TypedDict(
    "MeetingFeaturesConfigurationTypeDef",
    {
        "Audio": AudioFeaturesTypeDef,
    },
    total=False,
)

BatchCreateAttendeeRequestRequestTypeDef = TypedDict(
    "BatchCreateAttendeeRequestRequestTypeDef",
    {
        "MeetingId": str,
        "Attendees": Sequence[CreateAttendeeRequestItemTypeDef],
    },
)

BatchCreateAttendeeResponseTypeDef = TypedDict(
    "BatchCreateAttendeeResponseTypeDef",
    {
        "Attendees": List[AttendeeTypeDef],
        "Errors": List[CreateAttendeeErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateAttendeeResponseTypeDef = TypedDict(
    "CreateAttendeeResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetAttendeeResponseTypeDef = TypedDict(
    "GetAttendeeResponseTypeDef",
    {
        "Attendee": AttendeeTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListAttendeesResponseTypeDef = TypedDict(
    "ListAttendeesResponseTypeDef",
    {
        "Attendees": List[AttendeeTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

TranscriptionConfigurationTypeDef = TypedDict(
    "TranscriptionConfigurationTypeDef",
    {
        "EngineTranscribeSettings": EngineTranscribeSettingsTypeDef,
        "EngineTranscribeMedicalSettings": EngineTranscribeMedicalSettingsTypeDef,
    },
    total=False,
)

_RequiredCreateMeetingRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
    },
)
_OptionalCreateMeetingRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingRequestRequestTypeDef",
    {
        "MeetingHostId": str,
        "NotificationsConfiguration": NotificationsConfigurationTypeDef,
        "MeetingFeatures": MeetingFeaturesConfigurationTypeDef,
    },
    total=False,
)

class CreateMeetingRequestRequestTypeDef(
    _RequiredCreateMeetingRequestRequestTypeDef, _OptionalCreateMeetingRequestRequestTypeDef
):
    pass

_RequiredCreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "_RequiredCreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "ClientRequestToken": str,
        "MediaRegion": str,
        "ExternalMeetingId": str,
        "Attendees": Sequence[CreateAttendeeRequestItemTypeDef],
    },
)
_OptionalCreateMeetingWithAttendeesRequestRequestTypeDef = TypedDict(
    "_OptionalCreateMeetingWithAttendeesRequestRequestTypeDef",
    {
        "MeetingHostId": str,
        "MeetingFeatures": MeetingFeaturesConfigurationTypeDef,
        "NotificationsConfiguration": NotificationsConfigurationTypeDef,
    },
    total=False,
)

class CreateMeetingWithAttendeesRequestRequestTypeDef(
    _RequiredCreateMeetingWithAttendeesRequestRequestTypeDef,
    _OptionalCreateMeetingWithAttendeesRequestRequestTypeDef,
):
    pass

MeetingTypeDef = TypedDict(
    "MeetingTypeDef",
    {
        "MeetingId": str,
        "MeetingHostId": str,
        "ExternalMeetingId": str,
        "MediaRegion": str,
        "MediaPlacement": MediaPlacementTypeDef,
        "MeetingFeatures": MeetingFeaturesConfigurationTypeDef,
    },
    total=False,
)

StartMeetingTranscriptionRequestRequestTypeDef = TypedDict(
    "StartMeetingTranscriptionRequestRequestTypeDef",
    {
        "MeetingId": str,
        "TranscriptionConfiguration": TranscriptionConfigurationTypeDef,
    },
)

CreateMeetingResponseTypeDef = TypedDict(
    "CreateMeetingResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateMeetingWithAttendeesResponseTypeDef = TypedDict(
    "CreateMeetingWithAttendeesResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "Attendees": List[AttendeeTypeDef],
        "Errors": List[CreateAttendeeErrorTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetMeetingResponseTypeDef = TypedDict(
    "GetMeetingResponseTypeDef",
    {
        "Meeting": MeetingTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
