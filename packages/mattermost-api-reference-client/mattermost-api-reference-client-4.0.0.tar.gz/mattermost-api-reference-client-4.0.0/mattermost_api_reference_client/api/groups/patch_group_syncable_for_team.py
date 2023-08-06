from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.group_syncable_team import GroupSyncableTeam
from ...models.patch_group_syncable_for_team_json_body import PatchGroupSyncableForTeamJsonBody
from ...types import Response


def _get_kwargs(
    group_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: PatchGroupSyncableForTeamJsonBody,
) -> Dict[str, Any]:
    url = "{}/groups/{group_id}/teams/{team_id}/patch".format(client.base_url, group_id=group_id, team_id=team_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "put",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GroupSyncableTeam]]:
    if response.status_code == 200:
        response_200 = GroupSyncableTeam.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GroupSyncableTeam]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    group_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: PatchGroupSyncableForTeamJsonBody,
) -> Response[Union[Any, GroupSyncableTeam]]:
    """Patch a GroupSyncable associated to Team

     Partially update a GroupSyncable by providing only the fields you want to update. Omitted fields
    will not be updated. The fields that can be updated are defined in the request body, all other
    provided fields will be ignored.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):
        team_id (str):
        json_body (PatchGroupSyncableForTeamJsonBody):

    Returns:
        Response[Union[Any, GroupSyncableTeam]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        team_id=team_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    group_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: PatchGroupSyncableForTeamJsonBody,
) -> Optional[Union[Any, GroupSyncableTeam]]:
    """Patch a GroupSyncable associated to Team

     Partially update a GroupSyncable by providing only the fields you want to update. Omitted fields
    will not be updated. The fields that can be updated are defined in the request body, all other
    provided fields will be ignored.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):
        team_id (str):
        json_body (PatchGroupSyncableForTeamJsonBody):

    Returns:
        Response[Union[Any, GroupSyncableTeam]]
    """

    return sync_detailed(
        group_id=group_id,
        team_id=team_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    group_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: PatchGroupSyncableForTeamJsonBody,
) -> Response[Union[Any, GroupSyncableTeam]]:
    """Patch a GroupSyncable associated to Team

     Partially update a GroupSyncable by providing only the fields you want to update. Omitted fields
    will not be updated. The fields that can be updated are defined in the request body, all other
    provided fields will be ignored.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):
        team_id (str):
        json_body (PatchGroupSyncableForTeamJsonBody):

    Returns:
        Response[Union[Any, GroupSyncableTeam]]
    """

    kwargs = _get_kwargs(
        group_id=group_id,
        team_id=team_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    group_id: str,
    team_id: str,
    *,
    client: Client,
    json_body: PatchGroupSyncableForTeamJsonBody,
) -> Optional[Union[Any, GroupSyncableTeam]]:
    """Patch a GroupSyncable associated to Team

     Partially update a GroupSyncable by providing only the fields you want to update. Omitted fields
    will not be updated. The fields that can be updated are defined in the request body, all other
    provided fields will be ignored.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.11

    Args:
        group_id (str):
        team_id (str):
        json_body (PatchGroupSyncableForTeamJsonBody):

    Returns:
        Response[Union[Any, GroupSyncableTeam]]
    """

    return (
        await asyncio_detailed(
            group_id=group_id,
            team_id=team_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
