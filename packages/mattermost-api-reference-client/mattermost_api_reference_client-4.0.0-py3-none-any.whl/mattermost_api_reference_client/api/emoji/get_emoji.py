from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.emoji import Emoji
from ...types import Response


def _get_kwargs(
    emoji_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/emoji/{emoji_id}".format(client.base_url, emoji_id=emoji_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Emoji]]:
    if response.status_code == 200:
        response_200 = Emoji.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Emoji]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    emoji_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Emoji]]:
    """Get a custom emoji

     Get some metadata for a custom emoji.
    ##### Permissions
    Must be authenticated.

    Args:
        emoji_id (str):

    Returns:
        Response[Union[Any, Emoji]]
    """

    kwargs = _get_kwargs(
        emoji_id=emoji_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    emoji_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Emoji]]:
    """Get a custom emoji

     Get some metadata for a custom emoji.
    ##### Permissions
    Must be authenticated.

    Args:
        emoji_id (str):

    Returns:
        Response[Union[Any, Emoji]]
    """

    return sync_detailed(
        emoji_id=emoji_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    emoji_id: str,
    *,
    client: Client,
) -> Response[Union[Any, Emoji]]:
    """Get a custom emoji

     Get some metadata for a custom emoji.
    ##### Permissions
    Must be authenticated.

    Args:
        emoji_id (str):

    Returns:
        Response[Union[Any, Emoji]]
    """

    kwargs = _get_kwargs(
        emoji_id=emoji_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    emoji_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, Emoji]]:
    """Get a custom emoji

     Get some metadata for a custom emoji.
    ##### Permissions
    Must be authenticated.

    Args:
        emoji_id (str):

    Returns:
        Response[Union[Any, Emoji]]
    """

    return (
        await asyncio_detailed(
            emoji_id=emoji_id,
            client=client,
        )
    ).parsed
