from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.team_unread import TeamUnread
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    exclude_team: str,
    include_collapsed_threads: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/teams/unread".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["exclude_team"] = exclude_team

    params["include_collapsed_threads"] = include_collapsed_threads

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[TeamUnread]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = TeamUnread.from_dict(response_200_item_data)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[TeamUnread]]]:
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
    exclude_team: str,
    include_collapsed_threads: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[TeamUnread]]]:
    """Get team unreads for a user

     Get the count for unread messages and mentions in the teams the user is a member of.
    ##### Permissions
    Must be logged in.

    Args:
        user_id (str):
        exclude_team (str):
        include_collapsed_threads (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[TeamUnread]]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        exclude_team=exclude_team,
        include_collapsed_threads=include_collapsed_threads,
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
    exclude_team: str,
    include_collapsed_threads: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[TeamUnread]]]:
    """Get team unreads for a user

     Get the count for unread messages and mentions in the teams the user is a member of.
    ##### Permissions
    Must be logged in.

    Args:
        user_id (str):
        exclude_team (str):
        include_collapsed_threads (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[TeamUnread]]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        exclude_team=exclude_team,
        include_collapsed_threads=include_collapsed_threads,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    exclude_team: str,
    include_collapsed_threads: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[TeamUnread]]]:
    """Get team unreads for a user

     Get the count for unread messages and mentions in the teams the user is a member of.
    ##### Permissions
    Must be logged in.

    Args:
        user_id (str):
        exclude_team (str):
        include_collapsed_threads (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[TeamUnread]]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        exclude_team=exclude_team,
        include_collapsed_threads=include_collapsed_threads,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
    exclude_team: str,
    include_collapsed_threads: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[TeamUnread]]]:
    """Get team unreads for a user

     Get the count for unread messages and mentions in the teams the user is a member of.
    ##### Permissions
    Must be logged in.

    Args:
        user_id (str):
        exclude_team (str):
        include_collapsed_threads (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[TeamUnread]]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            exclude_team=exclude_team,
            include_collapsed_threads=include_collapsed_threads,
        )
    ).parsed
