from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_list import PostList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    since: Union[Unset, None, int] = UNSET,
    before: Union[Unset, None, str] = UNSET,
    after: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/posts".format(client.base_url, channel_id=channel_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params["since"] = since

    params["before"] = before

    params["after"] = after

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
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
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    since: Union[Unset, None, int] = UNSET,
    before: Union[Unset, None, str] = UNSET,
    after: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, PostList]]:
    """Get posts for a channel

     Get a page of posts in a channel. Use the query parameters to modify the behaviour of this endpoint.
    The parameter `since` must not be used with any of `before`, `after`, `page`, and `per_page`
    parameters.
    If `since` is used, it will always return all posts modified since that time, ordered by their
    create time limited till 1000. A caveat with this parameter is that there is no guarantee that the
    returned posts will be consecutive. It is left to the clients to maintain state and fill any missing
    holes in the post order.
    ##### Permissions
    Must have `read_channel` permission for the channel.

    Args:
        channel_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        since (Union[Unset, None, int]):
        before (Union[Unset, None, str]):
        after (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, PostList]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        page=page,
        per_page=per_page,
        since=since,
        before=before,
        after=after,
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
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    since: Union[Unset, None, int] = UNSET,
    before: Union[Unset, None, str] = UNSET,
    after: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, PostList]]:
    """Get posts for a channel

     Get a page of posts in a channel. Use the query parameters to modify the behaviour of this endpoint.
    The parameter `since` must not be used with any of `before`, `after`, `page`, and `per_page`
    parameters.
    If `since` is used, it will always return all posts modified since that time, ordered by their
    create time limited till 1000. A caveat with this parameter is that there is no guarantee that the
    returned posts will be consecutive. It is left to the clients to maintain state and fill any missing
    holes in the post order.
    ##### Permissions
    Must have `read_channel` permission for the channel.

    Args:
        channel_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        since (Union[Unset, None, int]):
        before (Union[Unset, None, str]):
        after (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, PostList]]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        page=page,
        per_page=per_page,
        since=since,
        before=before,
        after=after,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    since: Union[Unset, None, int] = UNSET,
    before: Union[Unset, None, str] = UNSET,
    after: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, PostList]]:
    """Get posts for a channel

     Get a page of posts in a channel. Use the query parameters to modify the behaviour of this endpoint.
    The parameter `since` must not be used with any of `before`, `after`, `page`, and `per_page`
    parameters.
    If `since` is used, it will always return all posts modified since that time, ordered by their
    create time limited till 1000. A caveat with this parameter is that there is no guarantee that the
    returned posts will be consecutive. It is left to the clients to maintain state and fill any missing
    holes in the post order.
    ##### Permissions
    Must have `read_channel` permission for the channel.

    Args:
        channel_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        since (Union[Unset, None, int]):
        before (Union[Unset, None, str]):
        after (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, PostList]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        page=page,
        per_page=per_page,
        since=since,
        before=before,
        after=after,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    channel_id: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    since: Union[Unset, None, int] = UNSET,
    before: Union[Unset, None, str] = UNSET,
    after: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, PostList]]:
    """Get posts for a channel

     Get a page of posts in a channel. Use the query parameters to modify the behaviour of this endpoint.
    The parameter `since` must not be used with any of `before`, `after`, `page`, and `per_page`
    parameters.
    If `since` is used, it will always return all posts modified since that time, ordered by their
    create time limited till 1000. A caveat with this parameter is that there is no guarantee that the
    returned posts will be consecutive. It is left to the clients to maintain state and fill any missing
    holes in the post order.
    ##### Permissions
    Must have `read_channel` permission for the channel.

    Args:
        channel_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        since (Union[Unset, None, int]):
        before (Union[Unset, None, str]):
        after (Union[Unset, None, str]):

    Returns:
        Response[Union[Any, PostList]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            page=page,
            per_page=per_page,
            since=since,
            before=before,
            after=after,
        )
    ).parsed
