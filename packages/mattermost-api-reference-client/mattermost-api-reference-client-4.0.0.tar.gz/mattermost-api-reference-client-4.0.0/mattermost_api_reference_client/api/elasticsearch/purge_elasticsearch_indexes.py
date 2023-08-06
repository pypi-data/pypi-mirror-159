from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/elasticsearch/purge_indexes".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

        return response_200
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Purge all Elasticsearch indexes

     Deletes all Elasticsearch indexes and their contents. After calling this endpoint, it is
    necessary to schedule a new Elasticsearch indexing job to repopulate the indexes.
    __Minimum server version__: 4.1
    ##### Permissions
    Must have `manage_system` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Purge all Elasticsearch indexes

     Deletes all Elasticsearch indexes and their contents. After calling this endpoint, it is
    necessary to schedule a new Elasticsearch indexing job to repopulate the indexes.
    __Minimum server version__: 4.1
    ##### Permissions
    Must have `manage_system` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Purge all Elasticsearch indexes

     Deletes all Elasticsearch indexes and their contents. After calling this endpoint, it is
    necessary to schedule a new Elasticsearch indexing job to repopulate the indexes.
    __Minimum server version__: 4.1
    ##### Permissions
    Must have `manage_system` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Purge all Elasticsearch indexes

     Deletes all Elasticsearch indexes and their contents. After calling this endpoint, it is
    necessary to schedule a new Elasticsearch indexing job to repopulate the indexes.
    __Minimum server version__: 4.1
    ##### Permissions
    Must have `manage_system` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
