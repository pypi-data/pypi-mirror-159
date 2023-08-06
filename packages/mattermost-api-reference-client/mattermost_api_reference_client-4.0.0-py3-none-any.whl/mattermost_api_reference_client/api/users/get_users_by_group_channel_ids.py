from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_users_by_group_channel_ids_response_200 import GetUsersByGroupChannelIdsResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: List[str],
) -> Dict[str, Any]:
    url = "{}/users/group_channels".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetUsersByGroupChannelIdsResponse200]]:
    if response.status_code == 200:
        response_200 = GetUsersByGroupChannelIdsResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetUsersByGroupChannelIdsResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: List[str],
) -> Response[Union[Any, GetUsersByGroupChannelIdsResponse200]]:
    """Get users by group channels ids

     Get an object containing a key per group channel id in the
    query and its value as a list of users members of that group
    channel.

    The user must be a member of the group ids in the query, or
    they will be omitted from the response.
    ##### Permissions
    Requires an active session but no other permissions.

    __Minimum server version__: 5.14

    Args:
        json_body (List[str]):

    Returns:
        Response[Union[Any, GetUsersByGroupChannelIdsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: List[str],
) -> Optional[Union[Any, GetUsersByGroupChannelIdsResponse200]]:
    """Get users by group channels ids

     Get an object containing a key per group channel id in the
    query and its value as a list of users members of that group
    channel.

    The user must be a member of the group ids in the query, or
    they will be omitted from the response.
    ##### Permissions
    Requires an active session but no other permissions.

    __Minimum server version__: 5.14

    Args:
        json_body (List[str]):

    Returns:
        Response[Union[Any, GetUsersByGroupChannelIdsResponse200]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: List[str],
) -> Response[Union[Any, GetUsersByGroupChannelIdsResponse200]]:
    """Get users by group channels ids

     Get an object containing a key per group channel id in the
    query and its value as a list of users members of that group
    channel.

    The user must be a member of the group ids in the query, or
    they will be omitted from the response.
    ##### Permissions
    Requires an active session but no other permissions.

    __Minimum server version__: 5.14

    Args:
        json_body (List[str]):

    Returns:
        Response[Union[Any, GetUsersByGroupChannelIdsResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: List[str],
) -> Optional[Union[Any, GetUsersByGroupChannelIdsResponse200]]:
    """Get users by group channels ids

     Get an object containing a key per group channel id in the
    query and its value as a list of users members of that group
    channel.

    The user must be a member of the group ids in the query, or
    they will be omitted from the response.
    ##### Permissions
    Requires an active session but no other permissions.

    __Minimum server version__: 5.14

    Args:
        json_body (List[str]):

    Returns:
        Response[Union[Any, GetUsersByGroupChannelIdsResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
