from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel import Channel
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
    last_delete_at: Union[Unset, None, int] = 0,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/teams/{team_id}/channels".format(client.base_url, user_id=user_id, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["include_deleted"] = include_deleted

    params["last_delete_at"] = last_delete_at

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Channel]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Channel.from_dict(response_200_item_data)

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Channel]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
    last_delete_at: Union[Unset, None, int] = 0,
) -> Response[Union[Any, List[Channel]]]:
    """Get channels for user

     Get all the channels on a team for a user.
    ##### Permissions
    Logged in as the user, or have `edit_other_users` permission, and `view_team` permission for the
    team.

    Args:
        user_id (str):
        team_id (str):
        include_deleted (Union[Unset, None, bool]):
        last_delete_at (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
        include_deleted=include_deleted,
        last_delete_at=last_delete_at,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
    last_delete_at: Union[Unset, None, int] = 0,
) -> Optional[Union[Any, List[Channel]]]:
    """Get channels for user

     Get all the channels on a team for a user.
    ##### Permissions
    Logged in as the user, or have `edit_other_users` permission, and `view_team` permission for the
    team.

    Args:
        user_id (str):
        team_id (str):
        include_deleted (Union[Unset, None, bool]):
        last_delete_at (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    return sync_detailed(
        user_id=user_id,
        team_id=team_id,
        client=client,
        include_deleted=include_deleted,
        last_delete_at=last_delete_at,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
    last_delete_at: Union[Unset, None, int] = 0,
) -> Response[Union[Any, List[Channel]]]:
    """Get channels for user

     Get all the channels on a team for a user.
    ##### Permissions
    Logged in as the user, or have `edit_other_users` permission, and `view_team` permission for the
    team.

    Args:
        user_id (str):
        team_id (str):
        include_deleted (Union[Unset, None, bool]):
        last_delete_at (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
        include_deleted=include_deleted,
        last_delete_at=last_delete_at,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    include_deleted: Union[Unset, None, bool] = False,
    last_delete_at: Union[Unset, None, int] = 0,
) -> Optional[Union[Any, List[Channel]]]:
    """Get channels for user

     Get all the channels on a team for a user.
    ##### Permissions
    Logged in as the user, or have `edit_other_users` permission, and `view_team` permission for the
    team.

    Args:
        user_id (str):
        team_id (str):
        include_deleted (Union[Unset, None, bool]):
        last_delete_at (Union[Unset, None, int]):

    Returns:
        Response[Union[Any, List[Channel]]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            client=client,
            include_deleted=include_deleted,
            last_delete_at=last_delete_at,
        )
    ).parsed
