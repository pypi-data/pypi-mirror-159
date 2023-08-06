from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post import Post
from ...types import UNSET, Response, Unset


def _get_kwargs(
    post_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/posts/{post_id}".format(client.base_url, post_id=post_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["include_deleted"] = include_deleted

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Post]]:
    if response.status_code == 200:
        response_200 = Post.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Post]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    post_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Response[Union[Any, Post]]:
    """Get a post

     Get a single post.
    ##### Permissions
    Must have `read_channel` permission for the channel the post is in or if the channel is public, have
    the `read_public_channels` permission for the team.

    Args:
        post_id (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        client=client,
        include_deleted=include_deleted,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    post_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, Post]]:
    """Get a post

     Get a single post.
    ##### Permissions
    Must have `read_channel` permission for the channel the post is in or if the channel is public, have
    the `read_public_channels` permission for the team.

    Args:
        post_id (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Post]]
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
        include_deleted=include_deleted,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Response[Union[Any, Post]]:
    """Get a post

     Get a single post.
    ##### Permissions
    Must have `read_channel` permission for the channel the post is in or if the channel is public, have
    the `read_public_channels` permission for the team.

    Args:
        post_id (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Post]]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        client=client,
        include_deleted=include_deleted,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    post_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, Post]]:
    """Get a post

     Get a single post.
    ##### Permissions
    Must have `read_channel` permission for the channel the post is in or if the channel is public, have
    the `read_public_channels` permission for the team.

    Args:
        post_id (str):
        include_deleted (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, Post]]
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
            include_deleted=include_deleted,
        )
    ).parsed
