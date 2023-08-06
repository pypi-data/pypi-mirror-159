from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.post_list import PostList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/posts/flagged".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["team_id"] = team_id

    params["channel_id"] = channel_id

    params["page"] = page

    params["per_page"] = per_page

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[PostList]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = PostList.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[PostList]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, List[PostList]]]:
    """Get a list of flagged posts

     Get a page of flagged posts of a user provided user id string. Selects from a channel, team, or all
    flagged posts by a user. Will only return posts from channels in which the user is member.
    ##### Permissions
    Must be user or have `manage_system` permission.

    Args:
        user_id (str):
        team_id (Union[Unset, None, str]):
        channel_id (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, List[PostList]]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        team_id=team_id,
        channel_id=channel_id,
        page=page,
        per_page=per_page,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, List[PostList]]]:
    """Get a list of flagged posts

     Get a page of flagged posts of a user provided user id string. Selects from a channel, team, or all
    flagged posts by a user. Will only return posts from channels in which the user is member.
    ##### Permissions
    Must be user or have `manage_system` permission.

    Args:
        user_id (str):
        team_id (Union[Unset, None, str]):
        channel_id (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, List[PostList]]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        team_id=team_id,
        channel_id=channel_id,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, List[PostList]]]:
    """Get a list of flagged posts

     Get a page of flagged posts of a user provided user id string. Selects from a channel, team, or all
    flagged posts by a user. Will only return posts from channels in which the user is member.
    ##### Permissions
    Must be user or have `manage_system` permission.

    Args:
        user_id (str):
        team_id (Union[Unset, None, str]):
        channel_id (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, List[PostList]]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        team_id=team_id,
        channel_id=channel_id,
        page=page,
        per_page=per_page,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
    team_id: Union[Unset, None, str] = UNSET,
    channel_id: Union[Unset, None, str] = UNSET,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, List[PostList]]]:
    """Get a list of flagged posts

     Get a page of flagged posts of a user provided user id string. Selects from a channel, team, or all
    flagged posts by a user. Will only return posts from channels in which the user is member.
    ##### Permissions
    Must be user or have `manage_system` permission.

    Args:
        user_id (str):
        team_id (Union[Unset, None, str]):
        channel_id (Union[Unset, None, str]):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, List[PostList]]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            team_id=team_id,
            channel_id=channel_id,
            page=page,
            per_page=per_page,
        )
    ).parsed
