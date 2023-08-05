"""
Type annotations for transcribe service client.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/)

Usage::

    ```python
    from aiobotocore.session import get_session
    from types_aiobotocore_transcribe.client import TranscribeServiceClient

    session = get_session()
    async with session.create_client("transcribe") as client:
        client: TranscribeServiceClient
    ```
"""
import sys
from typing import Any, Dict, Mapping, Sequence, Type

from aiobotocore.client import AioBaseClient
from botocore.client import ClientMeta

from .literals import (
    BaseModelNameType,
    CallAnalyticsJobStatusType,
    CLMLanguageCodeType,
    LanguageCodeType,
    MediaFormatType,
    ModelStatusType,
    TranscriptionJobStatusType,
    TypeType,
    VocabularyStateType,
)
from .type_defs import (
    CallAnalyticsJobSettingsTypeDef,
    ChannelDefinitionTypeDef,
    ContentRedactionTypeDef,
    CreateCallAnalyticsCategoryResponseTypeDef,
    CreateLanguageModelResponseTypeDef,
    CreateMedicalVocabularyResponseTypeDef,
    CreateVocabularyFilterResponseTypeDef,
    CreateVocabularyResponseTypeDef,
    DescribeLanguageModelResponseTypeDef,
    EmptyResponseMetadataTypeDef,
    GetCallAnalyticsCategoryResponseTypeDef,
    GetCallAnalyticsJobResponseTypeDef,
    GetMedicalTranscriptionJobResponseTypeDef,
    GetMedicalVocabularyResponseTypeDef,
    GetTranscriptionJobResponseTypeDef,
    GetVocabularyFilterResponseTypeDef,
    GetVocabularyResponseTypeDef,
    InputDataConfigTypeDef,
    JobExecutionSettingsTypeDef,
    LanguageIdSettingsTypeDef,
    ListCallAnalyticsCategoriesResponseTypeDef,
    ListCallAnalyticsJobsResponseTypeDef,
    ListLanguageModelsResponseTypeDef,
    ListMedicalTranscriptionJobsResponseTypeDef,
    ListMedicalVocabulariesResponseTypeDef,
    ListTagsForResourceResponseTypeDef,
    ListTranscriptionJobsResponseTypeDef,
    ListVocabulariesResponseTypeDef,
    ListVocabularyFiltersResponseTypeDef,
    MediaTypeDef,
    MedicalTranscriptionSettingTypeDef,
    ModelSettingsTypeDef,
    RuleTypeDef,
    SettingsTypeDef,
    StartCallAnalyticsJobResponseTypeDef,
    StartMedicalTranscriptionJobResponseTypeDef,
    StartTranscriptionJobResponseTypeDef,
    SubtitlesTypeDef,
    TagTypeDef,
    UpdateCallAnalyticsCategoryResponseTypeDef,
    UpdateMedicalVocabularyResponseTypeDef,
    UpdateVocabularyFilterResponseTypeDef,
    UpdateVocabularyResponseTypeDef,
)

if sys.version_info >= (3, 9):
    from typing import Literal
else:
    from typing_extensions import Literal


__all__ = ("TranscribeServiceClient",)


class BotocoreClientError(BaseException):
    MSG_TEMPLATE: str

    def __init__(self, error_response: Mapping[str, Any], operation_name: str) -> None:
        self.response: Dict[str, Any]
        self.operation_name: str


class Exceptions:
    BadRequestException: Type[BotocoreClientError]
    ClientError: Type[BotocoreClientError]
    ConflictException: Type[BotocoreClientError]
    InternalFailureException: Type[BotocoreClientError]
    LimitExceededException: Type[BotocoreClientError]
    NotFoundException: Type[BotocoreClientError]


class TranscribeServiceClient(AioBaseClient):
    """
    [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client)
    [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/)
    """

    meta: ClientMeta

    @property
    def exceptions(self) -> Exceptions:
        """
        TranscribeServiceClient exceptions.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.exceptions)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#exceptions)
        """

    def can_paginate(self, operation_name: str) -> bool:
        """
        Check if an operation can be paginated.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.can_paginate)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#can_paginate)
        """

    async def create_call_analytics_category(
        self, *, CategoryName: str, Rules: Sequence[RuleTypeDef]
    ) -> CreateCallAnalyticsCategoryResponseTypeDef:
        """
        Creates a call analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_call_analytics_category)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#create_call_analytics_category)
        """

    async def create_language_model(
        self,
        *,
        LanguageCode: CLMLanguageCodeType,
        BaseModelName: BaseModelNameType,
        ModelName: str,
        InputDataConfig: InputDataConfigTypeDef,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateLanguageModelResponseTypeDef:
        """
        Creates a new custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_language_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#create_language_model)
        """

    async def create_medical_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        VocabularyFileUri: str,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateMedicalVocabularyResponseTypeDef:
        """
        Creates a new custom medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_medical_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#create_medical_vocabulary)
        """

    async def create_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        Phrases: Sequence[str] = ...,
        VocabularyFileUri: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateVocabularyResponseTypeDef:
        """
        Creates a new custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#create_vocabulary)
        """

    async def create_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        LanguageCode: LanguageCodeType,
        Words: Sequence[str] = ...,
        VocabularyFilterFileUri: str = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> CreateVocabularyFilterResponseTypeDef:
        """
        Creates a new vocabulary filter that you can use to filter words from your
        transcription output.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.create_vocabulary_filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#create_vocabulary_filter)
        """

    async def delete_call_analytics_category(self, *, CategoryName: str) -> Dict[str, Any]:
        """
        Deletes a call analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_call_analytics_category)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#delete_call_analytics_category)
        """

    async def delete_call_analytics_job(self, *, CallAnalyticsJobName: str) -> Dict[str, Any]:
        """
        Deletes a call analytics job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_call_analytics_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#delete_call_analytics_job)
        """

    async def delete_language_model(self, *, ModelName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a custom language model.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_language_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#delete_language_model)
        """

    async def delete_medical_transcription_job(
        self, *, MedicalTranscriptionJobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a medical transcription job, along with any related information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_medical_transcription_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#delete_medical_transcription_job)
        """

    async def delete_medical_vocabulary(
        self, *, VocabularyName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a custom medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_medical_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#delete_medical_vocabulary)
        """

    async def delete_transcription_job(
        self, *, TranscriptionJobName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a transcription job, along with any related information.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_transcription_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#delete_transcription_job)
        """

    async def delete_vocabulary(self, *, VocabularyName: str) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a custom vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#delete_vocabulary)
        """

    async def delete_vocabulary_filter(
        self, *, VocabularyFilterName: str
    ) -> EmptyResponseMetadataTypeDef:
        """
        Deletes a vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.delete_vocabulary_filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#delete_vocabulary_filter)
        """

    async def describe_language_model(
        self, *, ModelName: str
    ) -> DescribeLanguageModelResponseTypeDef:
        """
        Provides information about a specific custom language model in your Amazon Web
        Services account.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.describe_language_model)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#describe_language_model)
        """

    async def generate_presigned_url(
        self,
        ClientMethod: str,
        Params: Mapping[str, Any] = ...,
        ExpiresIn: int = 3600,
        HttpMethod: str = ...,
    ) -> str:
        """
        Generate a presigned url given a client, its method, and arguments.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.generate_presigned_url)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#generate_presigned_url)
        """

    async def get_call_analytics_category(
        self, *, CategoryName: str
    ) -> GetCallAnalyticsCategoryResponseTypeDef:
        """
        Retrieves information about a call analytics category.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_call_analytics_category)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#get_call_analytics_category)
        """

    async def get_call_analytics_job(
        self, *, CallAnalyticsJobName: str
    ) -> GetCallAnalyticsJobResponseTypeDef:
        """
        Retrieves information about a call analytics job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_call_analytics_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#get_call_analytics_job)
        """

    async def get_medical_transcription_job(
        self, *, MedicalTranscriptionJobName: str
    ) -> GetMedicalTranscriptionJobResponseTypeDef:
        """
        Retrieves information about a medical transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_medical_transcription_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#get_medical_transcription_job)
        """

    async def get_medical_vocabulary(
        self, *, VocabularyName: str
    ) -> GetMedicalVocabularyResponseTypeDef:
        """
        Retrieves information about a medical vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_medical_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#get_medical_vocabulary)
        """

    async def get_transcription_job(
        self, *, TranscriptionJobName: str
    ) -> GetTranscriptionJobResponseTypeDef:
        """
        Returns information about a transcription job.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_transcription_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#get_transcription_job)
        """

    async def get_vocabulary(self, *, VocabularyName: str) -> GetVocabularyResponseTypeDef:
        """
        Gets information about a vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#get_vocabulary)
        """

    async def get_vocabulary_filter(
        self, *, VocabularyFilterName: str
    ) -> GetVocabularyFilterResponseTypeDef:
        """
        Returns information about a vocabulary filter.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.get_vocabulary_filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#get_vocabulary_filter)
        """

    async def list_call_analytics_categories(
        self, *, NextToken: str = ..., MaxResults: int = ...
    ) -> ListCallAnalyticsCategoriesResponseTypeDef:
        """
        Provides more information about the call analytics categories that you've
        created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_call_analytics_categories)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_call_analytics_categories)
        """

    async def list_call_analytics_jobs(
        self,
        *,
        Status: CallAnalyticsJobStatusType = ...,
        JobNameContains: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListCallAnalyticsJobsResponseTypeDef:
        """
        List call analytics jobs with a specified status or substring that matches their
        names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_call_analytics_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_call_analytics_jobs)
        """

    async def list_language_models(
        self,
        *,
        StatusEquals: ModelStatusType = ...,
        NameContains: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListLanguageModelsResponseTypeDef:
        """
        Provides more information about the custom language models you've created.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_language_models)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_language_models)
        """

    async def list_medical_transcription_jobs(
        self,
        *,
        Status: TranscriptionJobStatusType = ...,
        JobNameContains: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListMedicalTranscriptionJobsResponseTypeDef:
        """
        Lists medical transcription jobs with a specified status or substring that
        matches their names.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_medical_transcription_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_medical_transcription_jobs)
        """

    async def list_medical_vocabularies(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        StateEquals: VocabularyStateType = ...,
        NameContains: str = ...
    ) -> ListMedicalVocabulariesResponseTypeDef:
        """
        Returns a list of vocabularies that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_medical_vocabularies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_medical_vocabularies)
        """

    async def list_tags_for_resource(
        self, *, ResourceArn: str
    ) -> ListTagsForResourceResponseTypeDef:
        """
        Lists all tags associated with a given transcription job, vocabulary, or
        resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_tags_for_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_tags_for_resource)
        """

    async def list_transcription_jobs(
        self,
        *,
        Status: TranscriptionJobStatusType = ...,
        JobNameContains: str = ...,
        NextToken: str = ...,
        MaxResults: int = ...
    ) -> ListTranscriptionJobsResponseTypeDef:
        """
        Lists transcription jobs with the specified status.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_transcription_jobs)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_transcription_jobs)
        """

    async def list_vocabularies(
        self,
        *,
        NextToken: str = ...,
        MaxResults: int = ...,
        StateEquals: VocabularyStateType = ...,
        NameContains: str = ...
    ) -> ListVocabulariesResponseTypeDef:
        """
        Returns a list of vocabularies that match the specified criteria.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_vocabularies)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_vocabularies)
        """

    async def list_vocabulary_filters(
        self, *, NextToken: str = ..., MaxResults: int = ..., NameContains: str = ...
    ) -> ListVocabularyFiltersResponseTypeDef:
        """
        Gets information about vocabulary filters.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.list_vocabulary_filters)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#list_vocabulary_filters)
        """

    async def start_call_analytics_job(
        self,
        *,
        CallAnalyticsJobName: str,
        Media: MediaTypeDef,
        DataAccessRoleArn: str,
        OutputLocation: str = ...,
        OutputEncryptionKMSKeyId: str = ...,
        Settings: CallAnalyticsJobSettingsTypeDef = ...,
        ChannelDefinitions: Sequence[ChannelDefinitionTypeDef] = ...
    ) -> StartCallAnalyticsJobResponseTypeDef:
        """
        Starts an asynchronous analytics job that not only transcribes the audio
        recording of a caller and agent, but also returns additional insights.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.start_call_analytics_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#start_call_analytics_job)
        """

    async def start_medical_transcription_job(
        self,
        *,
        MedicalTranscriptionJobName: str,
        LanguageCode: LanguageCodeType,
        Media: MediaTypeDef,
        OutputBucketName: str,
        Specialty: Literal["PRIMARYCARE"],
        Type: TypeType,
        MediaSampleRateHertz: int = ...,
        MediaFormat: MediaFormatType = ...,
        OutputKey: str = ...,
        OutputEncryptionKMSKeyId: str = ...,
        KMSEncryptionContext: Mapping[str, str] = ...,
        Settings: MedicalTranscriptionSettingTypeDef = ...,
        ContentIdentificationType: Literal["PHI"] = ...,
        Tags: Sequence[TagTypeDef] = ...
    ) -> StartMedicalTranscriptionJobResponseTypeDef:
        """
        Starts a batch job to transcribe medical speech to text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.start_medical_transcription_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#start_medical_transcription_job)
        """

    async def start_transcription_job(
        self,
        *,
        TranscriptionJobName: str,
        Media: MediaTypeDef,
        LanguageCode: LanguageCodeType = ...,
        MediaSampleRateHertz: int = ...,
        MediaFormat: MediaFormatType = ...,
        OutputBucketName: str = ...,
        OutputKey: str = ...,
        OutputEncryptionKMSKeyId: str = ...,
        KMSEncryptionContext: Mapping[str, str] = ...,
        Settings: SettingsTypeDef = ...,
        ModelSettings: ModelSettingsTypeDef = ...,
        JobExecutionSettings: JobExecutionSettingsTypeDef = ...,
        ContentRedaction: ContentRedactionTypeDef = ...,
        IdentifyLanguage: bool = ...,
        LanguageOptions: Sequence[LanguageCodeType] = ...,
        Subtitles: SubtitlesTypeDef = ...,
        Tags: Sequence[TagTypeDef] = ...,
        LanguageIdSettings: Mapping[LanguageCodeType, LanguageIdSettingsTypeDef] = ...
    ) -> StartTranscriptionJobResponseTypeDef:
        """
        Starts an asynchronous job to transcribe speech to text.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.start_transcription_job)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#start_transcription_job)
        """

    async def tag_resource(self, *, ResourceArn: str, Tags: Sequence[TagTypeDef]) -> Dict[str, Any]:
        """
        Tags an Amazon Transcribe resource with the given list of tags.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.tag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#tag_resource)
        """

    async def untag_resource(self, *, ResourceArn: str, TagKeys: Sequence[str]) -> Dict[str, Any]:
        """
        Removes specified tags from a specified Amazon Transcribe resource.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.untag_resource)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#untag_resource)
        """

    async def update_call_analytics_category(
        self, *, CategoryName: str, Rules: Sequence[RuleTypeDef]
    ) -> UpdateCallAnalyticsCategoryResponseTypeDef:
        """
        Updates the call analytics category with new values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.update_call_analytics_category)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#update_call_analytics_category)
        """

    async def update_medical_vocabulary(
        self, *, VocabularyName: str, LanguageCode: LanguageCodeType, VocabularyFileUri: str = ...
    ) -> UpdateMedicalVocabularyResponseTypeDef:
        """
        Updates a vocabulary with new values that you provide in a different text file
        from the one you used to create the vocabulary.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.update_medical_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#update_medical_vocabulary)
        """

    async def update_vocabulary(
        self,
        *,
        VocabularyName: str,
        LanguageCode: LanguageCodeType,
        Phrases: Sequence[str] = ...,
        VocabularyFileUri: str = ...
    ) -> UpdateVocabularyResponseTypeDef:
        """
        Updates an existing vocabulary with new values.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#update_vocabulary)
        """

    async def update_vocabulary_filter(
        self,
        *,
        VocabularyFilterName: str,
        Words: Sequence[str] = ...,
        VocabularyFilterFileUri: str = ...
    ) -> UpdateVocabularyFilterResponseTypeDef:
        """
        Updates a vocabulary filter with a new list of filtered words.

        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client.update_vocabulary_filter)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/#update_vocabulary_filter)
        """

    async def __aenter__(self) -> "TranscribeServiceClient":
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/)
        """

    async def __aexit__(self, exc_type: Any, exc_val: Any, exc_tb: Any) -> Any:
        """
        [Show boto3 documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/transcribe.html#TranscribeService.Client)
        [Show types-aiobotocore documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_transcribe/client/)
        """
