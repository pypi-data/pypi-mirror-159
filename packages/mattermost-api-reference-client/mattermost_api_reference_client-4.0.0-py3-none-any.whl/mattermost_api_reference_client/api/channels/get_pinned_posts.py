from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_list import PostList
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/pinned".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PostList]]:
    if response.status_code == 200:
        response_200 = PostList.from_dict(response.json())

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PostList]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    channel_id: str,
    *,
    client: Client,
) -> Response[Union[Any, PostList]]:
    """Get a channel's pinned posts

     Get a list of pinned posts for channel.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, PostList]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    channel_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, PostList]]:
    """Get a channel's pinned posts

     Get a list of pinned posts for channel.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, PostList]]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Client,
) -> Response[Union[Any, PostList]]:
    """Get a channel's pinned posts

     Get a list of pinned posts for channel.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, PostList]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    channel_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, PostList]]:
    """Get a channel's pinned posts

     Get a list of pinned posts for channel.

    Args:
        channel_id (str):

    Returns:
        Response[Union[Any, PostList]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
        )
    ).parsed
