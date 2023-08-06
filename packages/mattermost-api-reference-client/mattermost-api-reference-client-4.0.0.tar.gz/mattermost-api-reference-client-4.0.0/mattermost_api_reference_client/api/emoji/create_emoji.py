from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.create_emoji_multipart_data import CreateEmojiMultipartData
from ...models.emoji import Emoji
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: CreateEmojiMultipartData,
) -> Dict[str, Any]:
    url = "{}/emoji".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Emoji]]:
    if response.status_code == 201:
        response_201 = Emoji.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 413:
        response_413 = cast(Any, None)
        return response_413
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
    *,
    client: Client,
    multipart_data: CreateEmojiMultipartData,
) -> Response[Union[Any, Emoji]]:
    """Create a custom emoji

     Create a custom emoji for the team.
    ##### Permissions
    Must be authenticated.

    Args:
        multipart_data (CreateEmojiMultipartData):

    Returns:
        Response[Union[Any, Emoji]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: CreateEmojiMultipartData,
) -> Optional[Union[Any, Emoji]]:
    """Create a custom emoji

     Create a custom emoji for the team.
    ##### Permissions
    Must be authenticated.

    Args:
        multipart_data (CreateEmojiMultipartData):

    Returns:
        Response[Union[Any, Emoji]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: CreateEmojiMultipartData,
) -> Response[Union[Any, Emoji]]:
    """Create a custom emoji

     Create a custom emoji for the team.
    ##### Permissions
    Must be authenticated.

    Args:
        multipart_data (CreateEmojiMultipartData):

    Returns:
        Response[Union[Any, Emoji]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: CreateEmojiMultipartData,
) -> Optional[Union[Any, Emoji]]:
    """Create a custom emoji

     Create a custom emoji for the team.
    ##### Permissions
    Must be authenticated.

    Args:
        multipart_data (CreateEmojiMultipartData):

    Returns:
        Response[Union[Any, Emoji]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
