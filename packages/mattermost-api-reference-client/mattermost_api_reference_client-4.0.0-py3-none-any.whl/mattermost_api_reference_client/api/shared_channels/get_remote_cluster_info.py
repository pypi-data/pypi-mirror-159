from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.remote_cluster_info import RemoteClusterInfo
from ...types import Response


def _get_kwargs(
    remote_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/sharedchannels/remote_info/{remote_id}".format(client.base_url, remote_id=remote_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RemoteClusterInfo]]:
    if response.status_code == 200:
        response_200 = RemoteClusterInfo.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RemoteClusterInfo]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    remote_id: str,
    *,
    client: Client,
) -> Response[Union[Any, RemoteClusterInfo]]:
    """Get remote cluster info by ID for user.

     Get remote cluster info based on remoteId.

    __Minimum server version__: 5.50

    ##### Permissions
    Must be authenticated and user must belong to at least one channel shared with the remote cluster.

    Args:
        remote_id (str):

    Returns:
        Response[Union[Any, RemoteClusterInfo]]
    """

    kwargs = _get_kwargs(
        remote_id=remote_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    remote_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, RemoteClusterInfo]]:
    """Get remote cluster info by ID for user.

     Get remote cluster info based on remoteId.

    __Minimum server version__: 5.50

    ##### Permissions
    Must be authenticated and user must belong to at least one channel shared with the remote cluster.

    Args:
        remote_id (str):

    Returns:
        Response[Union[Any, RemoteClusterInfo]]
    """

    return sync_detailed(
        remote_id=remote_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    remote_id: str,
    *,
    client: Client,
) -> Response[Union[Any, RemoteClusterInfo]]:
    """Get remote cluster info by ID for user.

     Get remote cluster info based on remoteId.

    __Minimum server version__: 5.50

    ##### Permissions
    Must be authenticated and user must belong to at least one channel shared with the remote cluster.

    Args:
        remote_id (str):

    Returns:
        Response[Union[Any, RemoteClusterInfo]]
    """

    kwargs = _get_kwargs(
        remote_id=remote_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    remote_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, RemoteClusterInfo]]:
    """Get remote cluster info by ID for user.

     Get remote cluster info based on remoteId.

    __Minimum server version__: 5.50

    ##### Permissions
    Must be authenticated and user must belong to at least one channel shared with the remote cluster.

    Args:
        remote_id (str):

    Returns:
        Response[Union[Any, RemoteClusterInfo]]
    """

    return (
        await asyncio_detailed(
            remote_id=remote_id,
            client=client,
        )
    ).parsed
