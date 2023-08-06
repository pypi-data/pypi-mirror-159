from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    user_id: str,
    post_id: str,
    emoji_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/posts/{post_id}/reactions/{emoji_name}".format(
        client.base_url, user_id=user_id, post_id=post_id, emoji_name=emoji_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "delete",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    post_id: str,
    emoji_name: str,
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Remove a reaction from a post

     Deletes a reaction made by a user from the given post.
    ##### Permissions
    Must be user or have `manage_system` permission.

    Args:
        user_id (str):
        post_id (str):
        emoji_name (str):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        post_id=post_id,
        emoji_name=emoji_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    post_id: str,
    emoji_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Remove a reaction from a post

     Deletes a reaction made by a user from the given post.
    ##### Permissions
    Must be user or have `manage_system` permission.

    Args:
        user_id (str):
        post_id (str):
        emoji_name (str):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        user_id=user_id,
        post_id=post_id,
        emoji_name=emoji_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    post_id: str,
    emoji_name: str,
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Remove a reaction from a post

     Deletes a reaction made by a user from the given post.
    ##### Permissions
    Must be user or have `manage_system` permission.

    Args:
        user_id (str):
        post_id (str):
        emoji_name (str):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        post_id=post_id,
        emoji_name=emoji_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    post_id: str,
    emoji_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Remove a reaction from a post

     Deletes a reaction made by a user from the given post.
    ##### Permissions
    Must be user or have `manage_system` permission.

    Args:
        user_id (str):
        post_id (str):
        emoji_name (str):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            post_id=post_id,
            emoji_name=emoji_name,
            client=client,
        )
    ).parsed
