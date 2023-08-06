from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.data_retention_policy_with_team_and_channel_counts import DataRetentionPolicyWithTeamAndChannelCounts
from ...models.data_retention_policy_with_team_and_channel_ids import DataRetentionPolicyWithTeamAndChannelIds
from ...types import Response


def _get_kwargs(
    policy_id: str,
    *,
    client: Client,
    json_body: DataRetentionPolicyWithTeamAndChannelIds,
) -> Dict[str, Any]:
    url = "{}/data_retention/policies/{policy_id}".format(client.base_url, policy_id=policy_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "patch",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]:
    if response.status_code == 200:
        response_200 = DataRetentionPolicyWithTeamAndChannelCounts.from_dict(response.json())

        return response_200
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    policy_id: str,
    *,
    client: Client,
    json_body: DataRetentionPolicyWithTeamAndChannelIds,
) -> Response[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]:
    """Patch a granular data retention policy

     Patches (i.e. replaces the fields of) a granular data retention policy.
    If any fields are omitted, they will not be changed.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_write_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (DataRetentionPolicyWithTeamAndChannelIds):

    Returns:
        Response[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    policy_id: str,
    *,
    client: Client,
    json_body: DataRetentionPolicyWithTeamAndChannelIds,
) -> Optional[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]:
    """Patch a granular data retention policy

     Patches (i.e. replaces the fields of) a granular data retention policy.
    If any fields are omitted, they will not be changed.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_write_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (DataRetentionPolicyWithTeamAndChannelIds):

    Returns:
        Response[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]
    """

    return sync_detailed(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    policy_id: str,
    *,
    client: Client,
    json_body: DataRetentionPolicyWithTeamAndChannelIds,
) -> Response[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]:
    """Patch a granular data retention policy

     Patches (i.e. replaces the fields of) a granular data retention policy.
    If any fields are omitted, they will not be changed.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_write_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (DataRetentionPolicyWithTeamAndChannelIds):

    Returns:
        Response[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]
    """

    kwargs = _get_kwargs(
        policy_id=policy_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    policy_id: str,
    *,
    client: Client,
    json_body: DataRetentionPolicyWithTeamAndChannelIds,
) -> Optional[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]:
    """Patch a granular data retention policy

     Patches (i.e. replaces the fields of) a granular data retention policy.
    If any fields are omitted, they will not be changed.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_write_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (DataRetentionPolicyWithTeamAndChannelIds):

    Returns:
        Response[Union[Any, DataRetentionPolicyWithTeamAndChannelCounts]]
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
