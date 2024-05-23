# This file was auto-generated by Fern from our API Definition.

import os
import typing

import httpx

from .annotations.client import AnnotationsClient, AsyncAnnotationsClient
from .core.api_error import ApiError
from .core.client_wrapper import AsyncClientWrapper, SyncClientWrapper
from .data.client import AsyncDataClient, DataClient
from .data_manager.client import AsyncDataManagerClient, DataManagerClient
from .environment import LabelStudioEnvironment
from .export.client import AsyncExportClient, ExportClient
from .files.client import AsyncFilesClient, FilesClient
from .invites.client import AsyncInvitesClient, InvitesClient
from .labels.client import AsyncLabelsClient, LabelsClient
from .machine_learning.client import AsyncMachineLearningClient, MachineLearningClient
from .organizations.client import AsyncOrganizationsClient, OrganizationsClient
from .predictions.client import AsyncPredictionsClient, PredictionsClient
from .projects.client import AsyncProjectsClient, ProjectsClient
from .storage.client import AsyncStorageClient, StorageClient
from .storage_azure.client import AsyncStorageAzureClient, StorageAzureClient
from .storage_gcs.client import AsyncStorageGcsClient, StorageGcsClient
from .storage_local.client import AsyncStorageLocalClient, StorageLocalClient
from .storage_redis.client import AsyncStorageRedisClient, StorageRedisClient
from .storage_s3.client import AsyncStorageS3Client, StorageS3Client
from .tasks.client import AsyncTasksClient, TasksClient
from .users.client import AsyncUsersClient, UsersClient
from .webhooks.client import AsyncWebhooksClient, WebhooksClient


class LabelStudio:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : LabelStudioEnvironment
        The environment to use for requests from the client. from .environment import LabelStudioEnvironment



        Defaults to LabelStudioEnvironment.DEFAULT



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.Client]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from label_studio_sdk.client import LabelStudio

    client = LabelStudio(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: LabelStudioEnvironment = LabelStudioEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("LABEL_STUDIO_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.Client] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        if api_key is None:
            raise ApiError(
                body="The client must be instantiated be either passing in api_key or setting LABEL_STUDIO_API_KEY"
            )
        self._client_wrapper = SyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.Client(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.Client(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.annotations = AnnotationsClient(client_wrapper=self._client_wrapper)
        self.users = UsersClient(client_wrapper=self._client_wrapper)
        self.data_manager = DataManagerClient(client_wrapper=self._client_wrapper)
        self.files = FilesClient(client_wrapper=self._client_wrapper)
        self.invites = InvitesClient(client_wrapper=self._client_wrapper)
        self.labels = LabelsClient(client_wrapper=self._client_wrapper)
        self.machine_learning = MachineLearningClient(client_wrapper=self._client_wrapper)
        self.organizations = OrganizationsClient(client_wrapper=self._client_wrapper)
        self.predictions = PredictionsClient(client_wrapper=self._client_wrapper)
        self.projects = ProjectsClient(client_wrapper=self._client_wrapper)
        self.export = ExportClient(client_wrapper=self._client_wrapper)
        self.storage = StorageClient(client_wrapper=self._client_wrapper)
        self.storage_azure = StorageAzureClient(client_wrapper=self._client_wrapper)
        self.storage_gcs = StorageGcsClient(client_wrapper=self._client_wrapper)
        self.storage_local = StorageLocalClient(client_wrapper=self._client_wrapper)
        self.storage_redis = StorageRedisClient(client_wrapper=self._client_wrapper)
        self.storage_s3 = StorageS3Client(client_wrapper=self._client_wrapper)
        self.tasks = TasksClient(client_wrapper=self._client_wrapper)
        self.webhooks = WebhooksClient(client_wrapper=self._client_wrapper)
        self.data = DataClient(client_wrapper=self._client_wrapper)


class AsyncLabelStudio:
    """
    Use this class to access the different functions within the SDK. You can instantiate any number of clients with different configuration that will propagate to these functions.

    Parameters
    ----------
    base_url : typing.Optional[str]
        The base url to use for requests from the client.

    environment : LabelStudioEnvironment
        The environment to use for requests from the client. from .environment import LabelStudioEnvironment



        Defaults to LabelStudioEnvironment.DEFAULT



    api_key : typing.Optional[str]
    timeout : typing.Optional[float]
        The timeout to be used, in seconds, for requests by default the timeout is 60 seconds, unless a custom httpx client is used, in which case a default is not set.

    follow_redirects : typing.Optional[bool]
        Whether the default httpx client follows redirects or not, this is irrelevant if a custom httpx client is passed in.

    httpx_client : typing.Optional[httpx.AsyncClient]
        The httpx client to use for making requests, a preconfigured client is used by default, however this is useful should you want to pass in any custom httpx configuration.

    Examples
    --------
    from label_studio_sdk.client import AsyncLabelStudio

    client = AsyncLabelStudio(
        api_key="YOUR_API_KEY",
    )
    """

    def __init__(
        self,
        *,
        base_url: typing.Optional[str] = None,
        environment: LabelStudioEnvironment = LabelStudioEnvironment.DEFAULT,
        api_key: typing.Optional[str] = os.getenv("LABEL_STUDIO_API_KEY"),
        timeout: typing.Optional[float] = None,
        follow_redirects: typing.Optional[bool] = True,
        httpx_client: typing.Optional[httpx.AsyncClient] = None
    ):
        _defaulted_timeout = timeout if timeout is not None else 60 if httpx_client is None else None
        if api_key is None:
            raise ApiError(
                body="The client must be instantiated be either passing in api_key or setting LABEL_STUDIO_API_KEY"
            )
        self._client_wrapper = AsyncClientWrapper(
            base_url=_get_base_url(base_url=base_url, environment=environment),
            api_key=api_key,
            httpx_client=httpx_client
            if httpx_client is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout, follow_redirects=follow_redirects)
            if follow_redirects is not None
            else httpx.AsyncClient(timeout=_defaulted_timeout),
            timeout=_defaulted_timeout,
        )
        self.annotations = AsyncAnnotationsClient(client_wrapper=self._client_wrapper)
        self.users = AsyncUsersClient(client_wrapper=self._client_wrapper)
        self.data_manager = AsyncDataManagerClient(client_wrapper=self._client_wrapper)
        self.files = AsyncFilesClient(client_wrapper=self._client_wrapper)
        self.invites = AsyncInvitesClient(client_wrapper=self._client_wrapper)
        self.labels = AsyncLabelsClient(client_wrapper=self._client_wrapper)
        self.machine_learning = AsyncMachineLearningClient(client_wrapper=self._client_wrapper)
        self.organizations = AsyncOrganizationsClient(client_wrapper=self._client_wrapper)
        self.predictions = AsyncPredictionsClient(client_wrapper=self._client_wrapper)
        self.projects = AsyncProjectsClient(client_wrapper=self._client_wrapper)
        self.export = AsyncExportClient(client_wrapper=self._client_wrapper)
        self.storage = AsyncStorageClient(client_wrapper=self._client_wrapper)
        self.storage_azure = AsyncStorageAzureClient(client_wrapper=self._client_wrapper)
        self.storage_gcs = AsyncStorageGcsClient(client_wrapper=self._client_wrapper)
        self.storage_local = AsyncStorageLocalClient(client_wrapper=self._client_wrapper)
        self.storage_redis = AsyncStorageRedisClient(client_wrapper=self._client_wrapper)
        self.storage_s3 = AsyncStorageS3Client(client_wrapper=self._client_wrapper)
        self.tasks = AsyncTasksClient(client_wrapper=self._client_wrapper)
        self.webhooks = AsyncWebhooksClient(client_wrapper=self._client_wrapper)
        self.data = AsyncDataClient(client_wrapper=self._client_wrapper)


def _get_base_url(*, base_url: typing.Optional[str] = None, environment: LabelStudioEnvironment) -> str:
    if base_url is not None:
        return base_url
    elif environment is not None:
        return environment.value
    else:
        raise Exception("Please pass in either base_url or environment to construct the client")
