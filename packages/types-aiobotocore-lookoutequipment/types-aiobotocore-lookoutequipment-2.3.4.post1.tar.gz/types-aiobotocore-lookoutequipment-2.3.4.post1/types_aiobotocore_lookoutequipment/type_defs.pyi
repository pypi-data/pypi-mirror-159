"""
Type annotations for lookoutequipment service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_lookoutequipment/type_defs/)

Usage::

    ```python
    from types_aiobotocore_lookoutequipment.type_defs import DatasetSchemaTypeDef

    data: DatasetSchemaTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Sequence, Union

from .literals import (
    DatasetStatusType,
    DataUploadFrequencyType,
    InferenceExecutionStatusType,
    InferenceSchedulerStatusType,
    IngestionJobStatusType,
    ModelStatusType,
    TargetSamplingRateType,
)

if sys.version_info >= (3, 9):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

__all__ = (
    "DatasetSchemaTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "DataPreProcessingConfigurationTypeDef",
    "DatasetSummaryTypeDef",
    "DeleteDatasetRequestRequestTypeDef",
    "DeleteInferenceSchedulerRequestRequestTypeDef",
    "DeleteModelRequestRequestTypeDef",
    "DescribeDataIngestionJobRequestRequestTypeDef",
    "DescribeDatasetRequestRequestTypeDef",
    "DescribeInferenceSchedulerRequestRequestTypeDef",
    "DescribeModelRequestRequestTypeDef",
    "S3ObjectTypeDef",
    "InferenceInputNameConfigurationTypeDef",
    "InferenceS3InputConfigurationTypeDef",
    "InferenceS3OutputConfigurationTypeDef",
    "InferenceSchedulerSummaryTypeDef",
    "IngestionS3InputConfigurationTypeDef",
    "LabelsS3InputConfigurationTypeDef",
    "ListDataIngestionJobsRequestRequestTypeDef",
    "ListDatasetsRequestRequestTypeDef",
    "ListInferenceExecutionsRequestRequestTypeDef",
    "ListInferenceSchedulersRequestRequestTypeDef",
    "ListModelsRequestRequestTypeDef",
    "ModelSummaryTypeDef",
    "ListTagsForResourceRequestRequestTypeDef",
    "StartInferenceSchedulerRequestRequestTypeDef",
    "StopInferenceSchedulerRequestRequestTypeDef",
    "UntagResourceRequestRequestTypeDef",
    "CreateDatasetRequestRequestTypeDef",
    "TagResourceRequestRequestTypeDef",
    "CreateDatasetResponseTypeDef",
    "CreateInferenceSchedulerResponseTypeDef",
    "CreateModelResponseTypeDef",
    "EmptyResponseMetadataTypeDef",
    "ListTagsForResourceResponseTypeDef",
    "StartDataIngestionJobResponseTypeDef",
    "StartInferenceSchedulerResponseTypeDef",
    "StopInferenceSchedulerResponseTypeDef",
    "ListDatasetsResponseTypeDef",
    "InferenceInputConfigurationTypeDef",
    "InferenceOutputConfigurationTypeDef",
    "ListInferenceSchedulersResponseTypeDef",
    "IngestionInputConfigurationTypeDef",
    "LabelsInputConfigurationTypeDef",
    "ListModelsResponseTypeDef",
    "CreateInferenceSchedulerRequestRequestTypeDef",
    "DescribeInferenceSchedulerResponseTypeDef",
    "InferenceExecutionSummaryTypeDef",
    "UpdateInferenceSchedulerRequestRequestTypeDef",
    "DataIngestionJobSummaryTypeDef",
    "DescribeDataIngestionJobResponseTypeDef",
    "DescribeDatasetResponseTypeDef",
    "StartDataIngestionJobRequestRequestTypeDef",
    "CreateModelRequestRequestTypeDef",
    "DescribeModelResponseTypeDef",
    "ListInferenceExecutionsResponseTypeDef",
    "ListDataIngestionJobsResponseTypeDef",
)

DatasetSchemaTypeDef = TypedDict(
    "DatasetSchemaTypeDef",
    {
        "InlineDataSchema": str,
    },
    total=False,
)

TagTypeDef = TypedDict(
    "TagTypeDef",
    {
        "Key": str,
        "Value": str,
    },
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

DataPreProcessingConfigurationTypeDef = TypedDict(
    "DataPreProcessingConfigurationTypeDef",
    {
        "TargetSamplingRate": TargetSamplingRateType,
    },
    total=False,
)

DatasetSummaryTypeDef = TypedDict(
    "DatasetSummaryTypeDef",
    {
        "DatasetName": str,
        "DatasetArn": str,
        "Status": DatasetStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

DeleteDatasetRequestRequestTypeDef = TypedDict(
    "DeleteDatasetRequestRequestTypeDef",
    {
        "DatasetName": str,
    },
)

DeleteInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "DeleteInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

DeleteModelRequestRequestTypeDef = TypedDict(
    "DeleteModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)

DescribeDataIngestionJobRequestRequestTypeDef = TypedDict(
    "DescribeDataIngestionJobRequestRequestTypeDef",
    {
        "JobId": str,
    },
)

DescribeDatasetRequestRequestTypeDef = TypedDict(
    "DescribeDatasetRequestRequestTypeDef",
    {
        "DatasetName": str,
    },
)

DescribeInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "DescribeInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

DescribeModelRequestRequestTypeDef = TypedDict(
    "DescribeModelRequestRequestTypeDef",
    {
        "ModelName": str,
    },
)

S3ObjectTypeDef = TypedDict(
    "S3ObjectTypeDef",
    {
        "Bucket": str,
        "Key": str,
    },
)

InferenceInputNameConfigurationTypeDef = TypedDict(
    "InferenceInputNameConfigurationTypeDef",
    {
        "TimestampFormat": str,
        "ComponentTimestampDelimiter": str,
    },
    total=False,
)

_RequiredInferenceS3InputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalInferenceS3InputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceS3InputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class InferenceS3InputConfigurationTypeDef(
    _RequiredInferenceS3InputConfigurationTypeDef, _OptionalInferenceS3InputConfigurationTypeDef
):
    pass

_RequiredInferenceS3OutputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceS3OutputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalInferenceS3OutputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceS3OutputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class InferenceS3OutputConfigurationTypeDef(
    _RequiredInferenceS3OutputConfigurationTypeDef, _OptionalInferenceS3OutputConfigurationTypeDef
):
    pass

InferenceSchedulerSummaryTypeDef = TypedDict(
    "InferenceSchedulerSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
    },
    total=False,
)

_RequiredIngestionS3InputConfigurationTypeDef = TypedDict(
    "_RequiredIngestionS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalIngestionS3InputConfigurationTypeDef = TypedDict(
    "_OptionalIngestionS3InputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class IngestionS3InputConfigurationTypeDef(
    _RequiredIngestionS3InputConfigurationTypeDef, _OptionalIngestionS3InputConfigurationTypeDef
):
    pass

_RequiredLabelsS3InputConfigurationTypeDef = TypedDict(
    "_RequiredLabelsS3InputConfigurationTypeDef",
    {
        "Bucket": str,
    },
)
_OptionalLabelsS3InputConfigurationTypeDef = TypedDict(
    "_OptionalLabelsS3InputConfigurationTypeDef",
    {
        "Prefix": str,
    },
    total=False,
)

class LabelsS3InputConfigurationTypeDef(
    _RequiredLabelsS3InputConfigurationTypeDef, _OptionalLabelsS3InputConfigurationTypeDef
):
    pass

ListDataIngestionJobsRequestRequestTypeDef = TypedDict(
    "ListDataIngestionJobsRequestRequestTypeDef",
    {
        "DatasetName": str,
        "NextToken": str,
        "MaxResults": int,
        "Status": IngestionJobStatusType,
    },
    total=False,
)

ListDatasetsRequestRequestTypeDef = TypedDict(
    "ListDatasetsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DatasetNameBeginsWith": str,
    },
    total=False,
)

_RequiredListInferenceExecutionsRequestRequestTypeDef = TypedDict(
    "_RequiredListInferenceExecutionsRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)
_OptionalListInferenceExecutionsRequestRequestTypeDef = TypedDict(
    "_OptionalListInferenceExecutionsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "DataStartTimeAfter": Union[datetime, str],
        "DataEndTimeBefore": Union[datetime, str],
        "Status": InferenceExecutionStatusType,
    },
    total=False,
)

class ListInferenceExecutionsRequestRequestTypeDef(
    _RequiredListInferenceExecutionsRequestRequestTypeDef,
    _OptionalListInferenceExecutionsRequestRequestTypeDef,
):
    pass

ListInferenceSchedulersRequestRequestTypeDef = TypedDict(
    "ListInferenceSchedulersRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "InferenceSchedulerNameBeginsWith": str,
        "ModelName": str,
    },
    total=False,
)

ListModelsRequestRequestTypeDef = TypedDict(
    "ListModelsRequestRequestTypeDef",
    {
        "NextToken": str,
        "MaxResults": int,
        "Status": ModelStatusType,
        "ModelNameBeginsWith": str,
        "DatasetNameBeginsWith": str,
    },
    total=False,
)

ModelSummaryTypeDef = TypedDict(
    "ModelSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "DatasetName": str,
        "DatasetArn": str,
        "Status": ModelStatusType,
        "CreatedAt": datetime,
    },
    total=False,
)

ListTagsForResourceRequestRequestTypeDef = TypedDict(
    "ListTagsForResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
    },
)

StartInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "StartInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

StopInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "StopInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)

UntagResourceRequestRequestTypeDef = TypedDict(
    "UntagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "TagKeys": Sequence[str],
    },
)

_RequiredCreateDatasetRequestRequestTypeDef = TypedDict(
    "_RequiredCreateDatasetRequestRequestTypeDef",
    {
        "DatasetName": str,
        "DatasetSchema": DatasetSchemaTypeDef,
        "ClientToken": str,
    },
)
_OptionalCreateDatasetRequestRequestTypeDef = TypedDict(
    "_OptionalCreateDatasetRequestRequestTypeDef",
    {
        "ServerSideKmsKeyId": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateDatasetRequestRequestTypeDef(
    _RequiredCreateDatasetRequestRequestTypeDef, _OptionalCreateDatasetRequestRequestTypeDef
):
    pass

TagResourceRequestRequestTypeDef = TypedDict(
    "TagResourceRequestRequestTypeDef",
    {
        "ResourceArn": str,
        "Tags": Sequence[TagTypeDef],
    },
)

CreateDatasetResponseTypeDef = TypedDict(
    "CreateDatasetResponseTypeDef",
    {
        "DatasetName": str,
        "DatasetArn": str,
        "Status": DatasetStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateInferenceSchedulerResponseTypeDef = TypedDict(
    "CreateInferenceSchedulerResponseTypeDef",
    {
        "InferenceSchedulerArn": str,
        "InferenceSchedulerName": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateModelResponseTypeDef = TypedDict(
    "CreateModelResponseTypeDef",
    {
        "ModelArn": str,
        "Status": ModelStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

EmptyResponseMetadataTypeDef = TypedDict(
    "EmptyResponseMetadataTypeDef",
    {
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceResponseTypeDef = TypedDict(
    "ListTagsForResourceResponseTypeDef",
    {
        "Tags": List[TagTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartDataIngestionJobResponseTypeDef = TypedDict(
    "StartDataIngestionJobResponseTypeDef",
    {
        "JobId": str,
        "Status": IngestionJobStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartInferenceSchedulerResponseTypeDef = TypedDict(
    "StartInferenceSchedulerResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StopInferenceSchedulerResponseTypeDef = TypedDict(
    "StopInferenceSchedulerResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDatasetsResponseTypeDef = TypedDict(
    "ListDatasetsResponseTypeDef",
    {
        "NextToken": str,
        "DatasetSummaries": List[DatasetSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

InferenceInputConfigurationTypeDef = TypedDict(
    "InferenceInputConfigurationTypeDef",
    {
        "S3InputConfiguration": InferenceS3InputConfigurationTypeDef,
        "InputTimeZoneOffset": str,
        "InferenceInputNameConfiguration": InferenceInputNameConfigurationTypeDef,
    },
    total=False,
)

_RequiredInferenceOutputConfigurationTypeDef = TypedDict(
    "_RequiredInferenceOutputConfigurationTypeDef",
    {
        "S3OutputConfiguration": InferenceS3OutputConfigurationTypeDef,
    },
)
_OptionalInferenceOutputConfigurationTypeDef = TypedDict(
    "_OptionalInferenceOutputConfigurationTypeDef",
    {
        "KmsKeyId": str,
    },
    total=False,
)

class InferenceOutputConfigurationTypeDef(
    _RequiredInferenceOutputConfigurationTypeDef, _OptionalInferenceOutputConfigurationTypeDef
):
    pass

ListInferenceSchedulersResponseTypeDef = TypedDict(
    "ListInferenceSchedulersResponseTypeDef",
    {
        "NextToken": str,
        "InferenceSchedulerSummaries": List[InferenceSchedulerSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

IngestionInputConfigurationTypeDef = TypedDict(
    "IngestionInputConfigurationTypeDef",
    {
        "S3InputConfiguration": IngestionS3InputConfigurationTypeDef,
    },
)

LabelsInputConfigurationTypeDef = TypedDict(
    "LabelsInputConfigurationTypeDef",
    {
        "S3InputConfiguration": LabelsS3InputConfigurationTypeDef,
    },
)

ListModelsResponseTypeDef = TypedDict(
    "ListModelsResponseTypeDef",
    {
        "NextToken": str,
        "ModelSummaries": List[ModelSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredCreateInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "_RequiredCreateInferenceSchedulerRequestRequestTypeDef",
    {
        "ModelName": str,
        "InferenceSchedulerName": str,
        "DataUploadFrequency": DataUploadFrequencyType,
        "DataInputConfiguration": InferenceInputConfigurationTypeDef,
        "DataOutputConfiguration": InferenceOutputConfigurationTypeDef,
        "RoleArn": str,
        "ClientToken": str,
    },
)
_OptionalCreateInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "_OptionalCreateInferenceSchedulerRequestRequestTypeDef",
    {
        "DataDelayOffsetInMinutes": int,
        "ServerSideKmsKeyId": str,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateInferenceSchedulerRequestRequestTypeDef(
    _RequiredCreateInferenceSchedulerRequestRequestTypeDef,
    _OptionalCreateInferenceSchedulerRequestRequestTypeDef,
):
    pass

DescribeInferenceSchedulerResponseTypeDef = TypedDict(
    "DescribeInferenceSchedulerResponseTypeDef",
    {
        "ModelArn": str,
        "ModelName": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "Status": InferenceSchedulerStatusType,
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
        "CreatedAt": datetime,
        "UpdatedAt": datetime,
        "DataInputConfiguration": InferenceInputConfigurationTypeDef,
        "DataOutputConfiguration": InferenceOutputConfigurationTypeDef,
        "RoleArn": str,
        "ServerSideKmsKeyId": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

InferenceExecutionSummaryTypeDef = TypedDict(
    "InferenceExecutionSummaryTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "InferenceSchedulerName": str,
        "InferenceSchedulerArn": str,
        "ScheduledStartTime": datetime,
        "DataStartTime": datetime,
        "DataEndTime": datetime,
        "DataInputConfiguration": InferenceInputConfigurationTypeDef,
        "DataOutputConfiguration": InferenceOutputConfigurationTypeDef,
        "CustomerResultObject": S3ObjectTypeDef,
        "Status": InferenceExecutionStatusType,
        "FailedReason": str,
    },
    total=False,
)

_RequiredUpdateInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "_RequiredUpdateInferenceSchedulerRequestRequestTypeDef",
    {
        "InferenceSchedulerName": str,
    },
)
_OptionalUpdateInferenceSchedulerRequestRequestTypeDef = TypedDict(
    "_OptionalUpdateInferenceSchedulerRequestRequestTypeDef",
    {
        "DataDelayOffsetInMinutes": int,
        "DataUploadFrequency": DataUploadFrequencyType,
        "DataInputConfiguration": InferenceInputConfigurationTypeDef,
        "DataOutputConfiguration": InferenceOutputConfigurationTypeDef,
        "RoleArn": str,
    },
    total=False,
)

class UpdateInferenceSchedulerRequestRequestTypeDef(
    _RequiredUpdateInferenceSchedulerRequestRequestTypeDef,
    _OptionalUpdateInferenceSchedulerRequestRequestTypeDef,
):
    pass

DataIngestionJobSummaryTypeDef = TypedDict(
    "DataIngestionJobSummaryTypeDef",
    {
        "JobId": str,
        "DatasetName": str,
        "DatasetArn": str,
        "IngestionInputConfiguration": IngestionInputConfigurationTypeDef,
        "Status": IngestionJobStatusType,
    },
    total=False,
)

DescribeDataIngestionJobResponseTypeDef = TypedDict(
    "DescribeDataIngestionJobResponseTypeDef",
    {
        "JobId": str,
        "DatasetArn": str,
        "IngestionInputConfiguration": IngestionInputConfigurationTypeDef,
        "RoleArn": str,
        "CreatedAt": datetime,
        "Status": IngestionJobStatusType,
        "FailedReason": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeDatasetResponseTypeDef = TypedDict(
    "DescribeDatasetResponseTypeDef",
    {
        "DatasetName": str,
        "DatasetArn": str,
        "CreatedAt": datetime,
        "LastUpdatedAt": datetime,
        "Status": DatasetStatusType,
        "Schema": str,
        "ServerSideKmsKeyId": str,
        "IngestionInputConfiguration": IngestionInputConfigurationTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

StartDataIngestionJobRequestRequestTypeDef = TypedDict(
    "StartDataIngestionJobRequestRequestTypeDef",
    {
        "DatasetName": str,
        "IngestionInputConfiguration": IngestionInputConfigurationTypeDef,
        "RoleArn": str,
        "ClientToken": str,
    },
)

_RequiredCreateModelRequestRequestTypeDef = TypedDict(
    "_RequiredCreateModelRequestRequestTypeDef",
    {
        "ModelName": str,
        "DatasetName": str,
        "ClientToken": str,
    },
)
_OptionalCreateModelRequestRequestTypeDef = TypedDict(
    "_OptionalCreateModelRequestRequestTypeDef",
    {
        "DatasetSchema": DatasetSchemaTypeDef,
        "LabelsInputConfiguration": LabelsInputConfigurationTypeDef,
        "TrainingDataStartTime": Union[datetime, str],
        "TrainingDataEndTime": Union[datetime, str],
        "EvaluationDataStartTime": Union[datetime, str],
        "EvaluationDataEndTime": Union[datetime, str],
        "RoleArn": str,
        "DataPreProcessingConfiguration": DataPreProcessingConfigurationTypeDef,
        "ServerSideKmsKeyId": str,
        "Tags": Sequence[TagTypeDef],
        "OffCondition": str,
    },
    total=False,
)

class CreateModelRequestRequestTypeDef(
    _RequiredCreateModelRequestRequestTypeDef, _OptionalCreateModelRequestRequestTypeDef
):
    pass

DescribeModelResponseTypeDef = TypedDict(
    "DescribeModelResponseTypeDef",
    {
        "ModelName": str,
        "ModelArn": str,
        "DatasetName": str,
        "DatasetArn": str,
        "Schema": str,
        "LabelsInputConfiguration": LabelsInputConfigurationTypeDef,
        "TrainingDataStartTime": datetime,
        "TrainingDataEndTime": datetime,
        "EvaluationDataStartTime": datetime,
        "EvaluationDataEndTime": datetime,
        "RoleArn": str,
        "DataPreProcessingConfiguration": DataPreProcessingConfigurationTypeDef,
        "Status": ModelStatusType,
        "TrainingExecutionStartTime": datetime,
        "TrainingExecutionEndTime": datetime,
        "FailedReason": str,
        "ModelMetrics": str,
        "LastUpdatedTime": datetime,
        "CreatedAt": datetime,
        "ServerSideKmsKeyId": str,
        "OffCondition": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListInferenceExecutionsResponseTypeDef = TypedDict(
    "ListInferenceExecutionsResponseTypeDef",
    {
        "NextToken": str,
        "InferenceExecutionSummaries": List[InferenceExecutionSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListDataIngestionJobsResponseTypeDef = TypedDict(
    "ListDataIngestionJobsResponseTypeDef",
    {
        "NextToken": str,
        "DataIngestionJobSummaries": List[DataIngestionJobSummaryTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
