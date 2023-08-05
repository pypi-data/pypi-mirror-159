"""
Type annotations for kinesisvideo service type definitions.

[Open documentation](https://youtype.github.io/types_aiobotocore_docs/types_aiobotocore_kinesisvideo/type_defs/)

Usage::

    ```python
    from types_aiobotocore_kinesisvideo.type_defs import SingleMasterConfigurationTypeDef

    data: SingleMasterConfigurationTypeDef = {...}
    ```
"""
import sys
from datetime import datetime
from typing import Dict, List, Mapping, Sequence

from .literals import (
    APINameType,
    ChannelProtocolType,
    ChannelRoleType,
    StatusType,
    UpdateDataRetentionOperationType,
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
    "SingleMasterConfigurationTypeDef",
    "ChannelNameConditionTypeDef",
    "TagTypeDef",
    "ResponseMetadataTypeDef",
    "CreateStreamInputRequestTypeDef",
    "DeleteSignalingChannelInputRequestTypeDef",
    "DeleteStreamInputRequestTypeDef",
    "DescribeSignalingChannelInputRequestTypeDef",
    "DescribeStreamInputRequestTypeDef",
    "StreamInfoTypeDef",
    "GetDataEndpointInputRequestTypeDef",
    "SingleMasterChannelEndpointConfigurationTypeDef",
    "ResourceEndpointListItemTypeDef",
    "PaginatorConfigTypeDef",
    "StreamNameConditionTypeDef",
    "ListTagsForResourceInputRequestTypeDef",
    "ListTagsForStreamInputRequestTypeDef",
    "TagStreamInputRequestTypeDef",
    "UntagResourceInputRequestTypeDef",
    "UntagStreamInputRequestTypeDef",
    "UpdateDataRetentionInputRequestTypeDef",
    "UpdateStreamInputRequestTypeDef",
    "ChannelInfoTypeDef",
    "UpdateSignalingChannelInputRequestTypeDef",
    "ListSignalingChannelsInputRequestTypeDef",
    "CreateSignalingChannelInputRequestTypeDef",
    "TagResourceInputRequestTypeDef",
    "CreateSignalingChannelOutputTypeDef",
    "CreateStreamOutputTypeDef",
    "GetDataEndpointOutputTypeDef",
    "ListTagsForResourceOutputTypeDef",
    "ListTagsForStreamOutputTypeDef",
    "DescribeStreamOutputTypeDef",
    "ListStreamsOutputTypeDef",
    "GetSignalingChannelEndpointInputRequestTypeDef",
    "GetSignalingChannelEndpointOutputTypeDef",
    "ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef",
    "ListStreamsInputListStreamsPaginateTypeDef",
    "ListStreamsInputRequestTypeDef",
    "DescribeSignalingChannelOutputTypeDef",
    "ListSignalingChannelsOutputTypeDef",
)

SingleMasterConfigurationTypeDef = TypedDict(
    "SingleMasterConfigurationTypeDef",
    {
        "MessageTtlSeconds": int,
    },
    total=False,
)

ChannelNameConditionTypeDef = TypedDict(
    "ChannelNameConditionTypeDef",
    {
        "ComparisonOperator": Literal["BEGINS_WITH"],
        "ComparisonValue": str,
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

_RequiredCreateStreamInputRequestTypeDef = TypedDict(
    "_RequiredCreateStreamInputRequestTypeDef",
    {
        "StreamName": str,
    },
)
_OptionalCreateStreamInputRequestTypeDef = TypedDict(
    "_OptionalCreateStreamInputRequestTypeDef",
    {
        "DeviceName": str,
        "MediaType": str,
        "KmsKeyId": str,
        "DataRetentionInHours": int,
        "Tags": Mapping[str, str],
    },
    total=False,
)

class CreateStreamInputRequestTypeDef(
    _RequiredCreateStreamInputRequestTypeDef, _OptionalCreateStreamInputRequestTypeDef
):
    pass

_RequiredDeleteSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredDeleteSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalDeleteSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalDeleteSignalingChannelInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class DeleteSignalingChannelInputRequestTypeDef(
    _RequiredDeleteSignalingChannelInputRequestTypeDef,
    _OptionalDeleteSignalingChannelInputRequestTypeDef,
):
    pass

_RequiredDeleteStreamInputRequestTypeDef = TypedDict(
    "_RequiredDeleteStreamInputRequestTypeDef",
    {
        "StreamARN": str,
    },
)
_OptionalDeleteStreamInputRequestTypeDef = TypedDict(
    "_OptionalDeleteStreamInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
    total=False,
)

class DeleteStreamInputRequestTypeDef(
    _RequiredDeleteStreamInputRequestTypeDef, _OptionalDeleteStreamInputRequestTypeDef
):
    pass

DescribeSignalingChannelInputRequestTypeDef = TypedDict(
    "DescribeSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
    },
    total=False,
)

DescribeStreamInputRequestTypeDef = TypedDict(
    "DescribeStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

StreamInfoTypeDef = TypedDict(
    "StreamInfoTypeDef",
    {
        "DeviceName": str,
        "StreamName": str,
        "StreamARN": str,
        "MediaType": str,
        "KmsKeyId": str,
        "Version": str,
        "Status": StatusType,
        "CreationTime": datetime,
        "DataRetentionInHours": int,
    },
    total=False,
)

_RequiredGetDataEndpointInputRequestTypeDef = TypedDict(
    "_RequiredGetDataEndpointInputRequestTypeDef",
    {
        "APIName": APINameType,
    },
)
_OptionalGetDataEndpointInputRequestTypeDef = TypedDict(
    "_OptionalGetDataEndpointInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class GetDataEndpointInputRequestTypeDef(
    _RequiredGetDataEndpointInputRequestTypeDef, _OptionalGetDataEndpointInputRequestTypeDef
):
    pass

SingleMasterChannelEndpointConfigurationTypeDef = TypedDict(
    "SingleMasterChannelEndpointConfigurationTypeDef",
    {
        "Protocols": Sequence[ChannelProtocolType],
        "Role": ChannelRoleType,
    },
    total=False,
)

ResourceEndpointListItemTypeDef = TypedDict(
    "ResourceEndpointListItemTypeDef",
    {
        "Protocol": ChannelProtocolType,
        "ResourceEndpoint": str,
    },
    total=False,
)

PaginatorConfigTypeDef = TypedDict(
    "PaginatorConfigTypeDef",
    {
        "MaxItems": int,
        "PageSize": int,
        "StartingToken": str,
    },
    total=False,
)

StreamNameConditionTypeDef = TypedDict(
    "StreamNameConditionTypeDef",
    {
        "ComparisonOperator": Literal["BEGINS_WITH"],
        "ComparisonValue": str,
    },
    total=False,
)

_RequiredListTagsForResourceInputRequestTypeDef = TypedDict(
    "_RequiredListTagsForResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
    },
)
_OptionalListTagsForResourceInputRequestTypeDef = TypedDict(
    "_OptionalListTagsForResourceInputRequestTypeDef",
    {
        "NextToken": str,
    },
    total=False,
)

class ListTagsForResourceInputRequestTypeDef(
    _RequiredListTagsForResourceInputRequestTypeDef, _OptionalListTagsForResourceInputRequestTypeDef
):
    pass

ListTagsForStreamInputRequestTypeDef = TypedDict(
    "ListTagsForStreamInputRequestTypeDef",
    {
        "NextToken": str,
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

_RequiredTagStreamInputRequestTypeDef = TypedDict(
    "_RequiredTagStreamInputRequestTypeDef",
    {
        "Tags": Mapping[str, str],
    },
)
_OptionalTagStreamInputRequestTypeDef = TypedDict(
    "_OptionalTagStreamInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

class TagStreamInputRequestTypeDef(
    _RequiredTagStreamInputRequestTypeDef, _OptionalTagStreamInputRequestTypeDef
):
    pass

UntagResourceInputRequestTypeDef = TypedDict(
    "UntagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "TagKeyList": Sequence[str],
    },
)

_RequiredUntagStreamInputRequestTypeDef = TypedDict(
    "_RequiredUntagStreamInputRequestTypeDef",
    {
        "TagKeyList": Sequence[str],
    },
)
_OptionalUntagStreamInputRequestTypeDef = TypedDict(
    "_OptionalUntagStreamInputRequestTypeDef",
    {
        "StreamARN": str,
        "StreamName": str,
    },
    total=False,
)

class UntagStreamInputRequestTypeDef(
    _RequiredUntagStreamInputRequestTypeDef, _OptionalUntagStreamInputRequestTypeDef
):
    pass

_RequiredUpdateDataRetentionInputRequestTypeDef = TypedDict(
    "_RequiredUpdateDataRetentionInputRequestTypeDef",
    {
        "CurrentVersion": str,
        "Operation": UpdateDataRetentionOperationType,
        "DataRetentionChangeInHours": int,
    },
)
_OptionalUpdateDataRetentionInputRequestTypeDef = TypedDict(
    "_OptionalUpdateDataRetentionInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
    },
    total=False,
)

class UpdateDataRetentionInputRequestTypeDef(
    _RequiredUpdateDataRetentionInputRequestTypeDef, _OptionalUpdateDataRetentionInputRequestTypeDef
):
    pass

_RequiredUpdateStreamInputRequestTypeDef = TypedDict(
    "_RequiredUpdateStreamInputRequestTypeDef",
    {
        "CurrentVersion": str,
    },
)
_OptionalUpdateStreamInputRequestTypeDef = TypedDict(
    "_OptionalUpdateStreamInputRequestTypeDef",
    {
        "StreamName": str,
        "StreamARN": str,
        "DeviceName": str,
        "MediaType": str,
    },
    total=False,
)

class UpdateStreamInputRequestTypeDef(
    _RequiredUpdateStreamInputRequestTypeDef, _OptionalUpdateStreamInputRequestTypeDef
):
    pass

ChannelInfoTypeDef = TypedDict(
    "ChannelInfoTypeDef",
    {
        "ChannelName": str,
        "ChannelARN": str,
        "ChannelType": Literal["SINGLE_MASTER"],
        "ChannelStatus": StatusType,
        "CreationTime": datetime,
        "SingleMasterConfiguration": SingleMasterConfigurationTypeDef,
        "Version": str,
    },
    total=False,
)

_RequiredUpdateSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredUpdateSignalingChannelInputRequestTypeDef",
    {
        "ChannelARN": str,
        "CurrentVersion": str,
    },
)
_OptionalUpdateSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalUpdateSignalingChannelInputRequestTypeDef",
    {
        "SingleMasterConfiguration": SingleMasterConfigurationTypeDef,
    },
    total=False,
)

class UpdateSignalingChannelInputRequestTypeDef(
    _RequiredUpdateSignalingChannelInputRequestTypeDef,
    _OptionalUpdateSignalingChannelInputRequestTypeDef,
):
    pass

ListSignalingChannelsInputRequestTypeDef = TypedDict(
    "ListSignalingChannelsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "ChannelNameCondition": ChannelNameConditionTypeDef,
    },
    total=False,
)

_RequiredCreateSignalingChannelInputRequestTypeDef = TypedDict(
    "_RequiredCreateSignalingChannelInputRequestTypeDef",
    {
        "ChannelName": str,
    },
)
_OptionalCreateSignalingChannelInputRequestTypeDef = TypedDict(
    "_OptionalCreateSignalingChannelInputRequestTypeDef",
    {
        "ChannelType": Literal["SINGLE_MASTER"],
        "SingleMasterConfiguration": SingleMasterConfigurationTypeDef,
        "Tags": Sequence[TagTypeDef],
    },
    total=False,
)

class CreateSignalingChannelInputRequestTypeDef(
    _RequiredCreateSignalingChannelInputRequestTypeDef,
    _OptionalCreateSignalingChannelInputRequestTypeDef,
):
    pass

TagResourceInputRequestTypeDef = TypedDict(
    "TagResourceInputRequestTypeDef",
    {
        "ResourceARN": str,
        "Tags": Sequence[TagTypeDef],
    },
)

CreateSignalingChannelOutputTypeDef = TypedDict(
    "CreateSignalingChannelOutputTypeDef",
    {
        "ChannelARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

CreateStreamOutputTypeDef = TypedDict(
    "CreateStreamOutputTypeDef",
    {
        "StreamARN": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

GetDataEndpointOutputTypeDef = TypedDict(
    "GetDataEndpointOutputTypeDef",
    {
        "DataEndpoint": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForResourceOutputTypeDef = TypedDict(
    "ListTagsForResourceOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListTagsForStreamOutputTypeDef = TypedDict(
    "ListTagsForStreamOutputTypeDef",
    {
        "NextToken": str,
        "Tags": Dict[str, str],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

DescribeStreamOutputTypeDef = TypedDict(
    "DescribeStreamOutputTypeDef",
    {
        "StreamInfo": StreamInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListStreamsOutputTypeDef = TypedDict(
    "ListStreamsOutputTypeDef",
    {
        "StreamInfoList": List[StreamInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

_RequiredGetSignalingChannelEndpointInputRequestTypeDef = TypedDict(
    "_RequiredGetSignalingChannelEndpointInputRequestTypeDef",
    {
        "ChannelARN": str,
    },
)
_OptionalGetSignalingChannelEndpointInputRequestTypeDef = TypedDict(
    "_OptionalGetSignalingChannelEndpointInputRequestTypeDef",
    {
        "SingleMasterChannelEndpointConfiguration": SingleMasterChannelEndpointConfigurationTypeDef,
    },
    total=False,
)

class GetSignalingChannelEndpointInputRequestTypeDef(
    _RequiredGetSignalingChannelEndpointInputRequestTypeDef,
    _OptionalGetSignalingChannelEndpointInputRequestTypeDef,
):
    pass

GetSignalingChannelEndpointOutputTypeDef = TypedDict(
    "GetSignalingChannelEndpointOutputTypeDef",
    {
        "ResourceEndpointList": List[ResourceEndpointListItemTypeDef],
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef = TypedDict(
    "ListSignalingChannelsInputListSignalingChannelsPaginateTypeDef",
    {
        "ChannelNameCondition": ChannelNameConditionTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListStreamsInputListStreamsPaginateTypeDef = TypedDict(
    "ListStreamsInputListStreamsPaginateTypeDef",
    {
        "StreamNameCondition": StreamNameConditionTypeDef,
        "PaginationConfig": PaginatorConfigTypeDef,
    },
    total=False,
)

ListStreamsInputRequestTypeDef = TypedDict(
    "ListStreamsInputRequestTypeDef",
    {
        "MaxResults": int,
        "NextToken": str,
        "StreamNameCondition": StreamNameConditionTypeDef,
    },
    total=False,
)

DescribeSignalingChannelOutputTypeDef = TypedDict(
    "DescribeSignalingChannelOutputTypeDef",
    {
        "ChannelInfo": ChannelInfoTypeDef,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)

ListSignalingChannelsOutputTypeDef = TypedDict(
    "ListSignalingChannelsOutputTypeDef",
    {
        "ChannelInfoList": List[ChannelInfoTypeDef],
        "NextToken": str,
        "ResponseMetadata": ResponseMetadataTypeDef,
    },
)
