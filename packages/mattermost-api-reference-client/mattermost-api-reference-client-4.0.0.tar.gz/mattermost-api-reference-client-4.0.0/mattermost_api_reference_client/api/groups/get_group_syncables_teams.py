from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.group_syncable_teams import GroupSyncableTeams
from ...types import Response


def _get_kwargs(
    group_id: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/groups/{group_id}/teams".format(client.base_url, group_id=group_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[GroupSyncableTeams]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = GroupSyncableTeams.from_dict(response_200_item_data)

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
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[GroupSyncableTeams]]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    group_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List[GroupSyncableTeams]]]:
    """Get group teams

     Retrieve the list of teams associated to the group
    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):

    Returns:
        Response[Union[Any, List[GroupSyncableTeams]]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    group_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List[GroupSyncableTeams]]]:
    """Get group teams

     Retrieve the list of teams associated to the group
    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):

    Returns:
        Response[Union[Any, List[GroupSyncableTeams]]]
    """

    return sync_detailed(
        group_id=group_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    *,
    client: Client,
) -> Response[Union[Any, List[GroupSyncableTeams]]]:
    """Get group teams

     Retrieve the list of teams associated to the group
    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):

    Returns:
        Response[Union[Any, List[GroupSyncableTeams]]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    group_id: str,
    *,
    client: Client,
) -> Optional[Union[Any, List[GroupSyncableTeams]]]:
    """Get group teams

     Retrieve the list of teams associated to the group
    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):

    Returns:
        Response[Union[Any, List[GroupSyncableTeams]]]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            client=client,
        )
    ).parsed
