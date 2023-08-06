from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.users_stats import UsersStats
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/known".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UsersStats]]:
    if response.status_code == 200:
        response_200 = UsersStats.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UsersStats]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, UsersStats]]:
    """Get user IDs of known users

     Get the list of user IDs of users with any direct relationship with a
    user. That means any user sharing any channel, including direct and
    group channels.
    ##### Permissions
    Must be authenticated.

    __Minimum server version__: 5.23

    Returns:
        Response[Union[Any, UsersStats]]
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
) -> Optional[Union[Any, UsersStats]]:
    """Get user IDs of known users

     Get the list of user IDs of users with any direct relationship with a
    user. That means any user sharing any channel, including direct and
    group channels.
    ##### Permissions
    Must be authenticated.

    __Minimum server version__: 5.23

    Returns:
        Response[Union[Any, UsersStats]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, UsersStats]]:
    """Get user IDs of known users

     Get the list of user IDs of users with any direct relationship with a
    user. That means any user sharing any channel, including direct and
    group channels.
    ##### Permissions
    Must be authenticated.

    __Minimum server version__: 5.23

    Returns:
        Response[Union[Any, UsersStats]]
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
) -> Optional[Union[Any, UsersStats]]:
    """Get user IDs of known users

     Get the list of user IDs of users with any direct relationship with a
    user. That means any user sharing any channel, including direct and
    group channels.
    ##### Permissions
    Must be authenticated.

    __Minimum server version__: 5.23

    Returns:
        Response[Union[Any, UsersStats]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
