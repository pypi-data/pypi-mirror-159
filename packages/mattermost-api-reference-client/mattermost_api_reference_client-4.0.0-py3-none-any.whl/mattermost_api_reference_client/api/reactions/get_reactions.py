from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.reaction import Reaction
from ...types import Response


def _get_kwargs(
    post_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/posts/{post_id}/reactions".format(client.base_url, post_id=post_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Reaction]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Reaction.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Reaction]]]:
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
) -> Response[Union[Any, List[Reaction]]]:
    """Get a list of reactions to a post

     Get a list of reactions made by all users to a given post.
    ##### Permissions
    Must have `read_channel` permission for the channel the post is in.

    Args:
        post_id (str):

    Returns:
        Response[Union[Any, List[Reaction]]]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        client=client,
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
) -> Optional[Union[Any, List[Reaction]]]:
    """Get a list of reactions to a post

     Get a list of reactions made by all users to a given post.
    ##### Permissions
    Must have `read_channel` permission for the channel the post is in.

    Args:
        post_id (str):

    Returns:
        Response[Union[Any, List[Reaction]]]
    """

    return sync_detailed(
        post_id=post_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    post_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List[Reaction]]]:
    """Get a list of reactions to a post

     Get a list of reactions made by all users to a given post.
    ##### Permissions
    Must have `read_channel` permission for the channel the post is in.

    Args:
        post_id (str):

    Returns:
        Response[Union[Any, List[Reaction]]]
    """

    kwargs = _get_kwargs(
        post_id=post_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    post_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List[Reaction]]]:
    """Get a list of reactions to a post

     Get a list of reactions made by all users to a given post.
    ##### Permissions
    Must have `read_channel` permission for the channel the post is in.

    Args:
        post_id (str):

    Returns:
        Response[Union[Any, List[Reaction]]]
    """

    return (
        await asyncio_detailed(
            post_id=post_id,
            client=client,
        )
    ).parsed
