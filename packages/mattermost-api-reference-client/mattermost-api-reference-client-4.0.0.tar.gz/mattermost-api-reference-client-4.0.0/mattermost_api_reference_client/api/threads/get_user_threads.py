from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.user_threads import UserThreads
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    since: Union[Unset, None, int] = UNSET,
    deleted: Union[Unset, None, bool] = False,
    extended: Union[Unset, None, bool] = False,
    page: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = 30,
    totals_only: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/teams/{team_id}/threads".format(client.base_url, user_id=user_id, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["since"] = since

    params["deleted"] = deleted

    params["extended"] = extended

    params["page"] = page

    params["pageSize"] = page_size

    params["totalsOnly"] = totals_only

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UserThreads]]:
    if response.status_code == 200:
        response_200 = UserThreads.from_dict(response.json())

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
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UserThreads]]:
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
    since: Union[Unset, None, int] = UNSET,
    deleted: Union[Unset, None, bool] = False,
    extended: Union[Unset, None, bool] = False,
    page: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = 30,
    totals_only: Union[Unset, None, bool] = False,
) -> Response[Union[Any, UserThreads]]:
    """Get all threads that user is following

     Get all threads that user is following

    __Minimum server version__: 5.29

    ##### Permissions
    Must be logged in as the user or have `edit_other_users` permission.

    Args:
        user_id (str):
        team_id (str):
        since (Union[Unset, None, int]):
        deleted (Union[Unset, None, bool]):
        extended (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):  Default: 30.
        totals_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, UserThreads]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
        since=since,
        deleted=deleted,
        extended=extended,
        page=page,
        page_size=page_size,
        totals_only=totals_only,
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
    since: Union[Unset, None, int] = UNSET,
    deleted: Union[Unset, None, bool] = False,
    extended: Union[Unset, None, bool] = False,
    page: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = 30,
    totals_only: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, UserThreads]]:
    """Get all threads that user is following

     Get all threads that user is following

    __Minimum server version__: 5.29

    ##### Permissions
    Must be logged in as the user or have `edit_other_users` permission.

    Args:
        user_id (str):
        team_id (str):
        since (Union[Unset, None, int]):
        deleted (Union[Unset, None, bool]):
        extended (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):  Default: 30.
        totals_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, UserThreads]]
    """

    return sync_detailed(
        user_id=user_id,
        team_id=team_id,
        client=client,
        since=since,
        deleted=deleted,
        extended=extended,
        page=page,
        page_size=page_size,
        totals_only=totals_only,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    since: Union[Unset, None, int] = UNSET,
    deleted: Union[Unset, None, bool] = False,
    extended: Union[Unset, None, bool] = False,
    page: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = 30,
    totals_only: Union[Unset, None, bool] = False,
) -> Response[Union[Any, UserThreads]]:
    """Get all threads that user is following

     Get all threads that user is following

    __Minimum server version__: 5.29

    ##### Permissions
    Must be logged in as the user or have `edit_other_users` permission.

    Args:
        user_id (str):
        team_id (str):
        since (Union[Unset, None, int]):
        deleted (Union[Unset, None, bool]):
        extended (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):  Default: 30.
        totals_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, UserThreads]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        team_id=team_id,
        client=client,
        since=since,
        deleted=deleted,
        extended=extended,
        page=page,
        page_size=page_size,
        totals_only=totals_only,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    team_id: str,
    *,
    client: Client,
    since: Union[Unset, None, int] = UNSET,
    deleted: Union[Unset, None, bool] = False,
    extended: Union[Unset, None, bool] = False,
    page: Union[Unset, None, int] = 0,
    page_size: Union[Unset, None, int] = 30,
    totals_only: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, UserThreads]]:
    """Get all threads that user is following

     Get all threads that user is following

    __Minimum server version__: 5.29

    ##### Permissions
    Must be logged in as the user or have `edit_other_users` permission.

    Args:
        user_id (str):
        team_id (str):
        since (Union[Unset, None, int]):
        deleted (Union[Unset, None, bool]):
        extended (Union[Unset, None, bool]):
        page (Union[Unset, None, int]):
        page_size (Union[Unset, None, int]):  Default: 30.
        totals_only (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, UserThreads]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            team_id=team_id,
            client=client,
            since=since,
            deleted=deleted,
            extended=extended,
            page=page,
            page_size=page_size,
            totals_only=totals_only,
        )
    ).parsed
