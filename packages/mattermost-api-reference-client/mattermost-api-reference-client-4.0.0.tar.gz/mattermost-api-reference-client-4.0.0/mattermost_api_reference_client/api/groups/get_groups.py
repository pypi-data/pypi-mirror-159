from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.group import Group
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    q: Union[Unset, None, str] = UNSET,
    include_member_count: Union[Unset, None, bool] = UNSET,
    not_associated_to_team: str,
    not_associated_to_channel: str,
    since: Union[Unset, None, int] = UNSET,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Dict[str, Any]:
    url = "{}/groups".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["page"] = page

    params["per_page"] = per_page

    params["q"] = q

    params["include_member_count"] = include_member_count

    params["not_associated_to_team"] = not_associated_to_team

    params["not_associated_to_channel"] = not_associated_to_channel

    params["since"] = since

    params["filter_allow_reference"] = filter_allow_reference

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Group]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Group.from_dict(response_200_item_data)

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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Group]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    q: Union[Unset, None, str] = UNSET,
    include_member_count: Union[Unset, None, bool] = UNSET,
    not_associated_to_team: str,
    not_associated_to_channel: str,
    since: Union[Unset, None, int] = UNSET,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[Group]]]:
    """Get groups

     Retrieve a list of all groups not associated to a particular channel or team.

    `not_associated_to_team` **OR** `not_associated_to_channel` is required.

    If you use `not_associated_to_team`, you must be a team admin for that particular team (permission
    to manage that team).

    If you use `not_associated_to_channel`, you must be a channel admin for that particular channel
    (permission to manage that channel).

    __Minimum server version__: 5.11

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        q (Union[Unset, None, str]):
        include_member_count (Union[Unset, None, bool]):
        not_associated_to_team (str):
        not_associated_to_channel (str):
        since (Union[Unset, None, int]):
        filter_allow_reference (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Group]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        include_member_count=include_member_count,
        not_associated_to_team=not_associated_to_team,
        not_associated_to_channel=not_associated_to_channel,
        since=since,
        filter_allow_reference=filter_allow_reference,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    q: Union[Unset, None, str] = UNSET,
    include_member_count: Union[Unset, None, bool] = UNSET,
    not_associated_to_team: str,
    not_associated_to_channel: str,
    since: Union[Unset, None, int] = UNSET,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[Group]]]:
    """Get groups

     Retrieve a list of all groups not associated to a particular channel or team.

    `not_associated_to_team` **OR** `not_associated_to_channel` is required.

    If you use `not_associated_to_team`, you must be a team admin for that particular team (permission
    to manage that team).

    If you use `not_associated_to_channel`, you must be a channel admin for that particular channel
    (permission to manage that channel).

    __Minimum server version__: 5.11

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        q (Union[Unset, None, str]):
        include_member_count (Union[Unset, None, bool]):
        not_associated_to_team (str):
        not_associated_to_channel (str):
        since (Union[Unset, None, int]):
        filter_allow_reference (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Group]]]
    """

    return sync_detailed(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        include_member_count=include_member_count,
        not_associated_to_team=not_associated_to_team,
        not_associated_to_channel=not_associated_to_channel,
        since=since,
        filter_allow_reference=filter_allow_reference,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    q: Union[Unset, None, str] = UNSET,
    include_member_count: Union[Unset, None, bool] = UNSET,
    not_associated_to_team: str,
    not_associated_to_channel: str,
    since: Union[Unset, None, int] = UNSET,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Response[Union[Any, List[Group]]]:
    """Get groups

     Retrieve a list of all groups not associated to a particular channel or team.

    `not_associated_to_team` **OR** `not_associated_to_channel` is required.

    If you use `not_associated_to_team`, you must be a team admin for that particular team (permission
    to manage that team).

    If you use `not_associated_to_channel`, you must be a channel admin for that particular channel
    (permission to manage that channel).

    __Minimum server version__: 5.11

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        q (Union[Unset, None, str]):
        include_member_count (Union[Unset, None, bool]):
        not_associated_to_team (str):
        not_associated_to_channel (str):
        since (Union[Unset, None, int]):
        filter_allow_reference (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Group]]]
    """

    kwargs = _get_kwargs(
        client=client,
        page=page,
        per_page=per_page,
        q=q,
        include_member_count=include_member_count,
        not_associated_to_team=not_associated_to_team,
        not_associated_to_channel=not_associated_to_channel,
        since=since,
        filter_allow_reference=filter_allow_reference,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
    q: Union[Unset, None, str] = UNSET,
    include_member_count: Union[Unset, None, bool] = UNSET,
    not_associated_to_team: str,
    not_associated_to_channel: str,
    since: Union[Unset, None, int] = UNSET,
    filter_allow_reference: Union[Unset, None, bool] = False,
) -> Optional[Union[Any, List[Group]]]:
    """Get groups

     Retrieve a list of all groups not associated to a particular channel or team.

    `not_associated_to_team` **OR** `not_associated_to_channel` is required.

    If you use `not_associated_to_team`, you must be a team admin for that particular team (permission
    to manage that team).

    If you use `not_associated_to_channel`, you must be a channel admin for that particular channel
    (permission to manage that channel).

    __Minimum server version__: 5.11

    Args:
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.
        q (Union[Unset, None, str]):
        include_member_count (Union[Unset, None, bool]):
        not_associated_to_team (str):
        not_associated_to_channel (str):
        since (Union[Unset, None, int]):
        filter_allow_reference (Union[Unset, None, bool]):

    Returns:
        Response[Union[Any, List[Group]]]
    """

    return (
        await asyncio_detailed(
            client=client,
            page=page,
            per_page=per_page,
            q=q,
            include_member_count=include_member_count,
            not_associated_to_team=not_associated_to_team,
            not_associated_to_channel=not_associated_to_channel,
            since=since,
            filter_allow_reference=filter_allow_reference,
        )
    ).parsed
