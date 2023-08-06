from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.channel_with_team_data import ChannelWithTeamData
from ...models.search_channels_for_retention_policy_json_body import SearchChannelsForRetentionPolicyJsonBody
from ...types import Response


def _get_kwargs(
    policy_id: str,
    *,
    client: Client,
    json_body: SearchChannelsForRetentionPolicyJsonBody,
) -> Dict[str, Any]:
    url = "{}/data_retention/policies/{policy_id}/channels/search".format(client.base_url, policy_id=policy_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[ChannelWithTeamData]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for componentsschemas_channel_list_with_team_data_item_data in _response_200:
            componentsschemas_channel_list_with_team_data_item = ChannelWithTeamData.from_dict(
                componentsschemas_channel_list_with_team_data_item_data
            )

            response_200.append(componentsschemas_channel_list_with_team_data_item)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[ChannelWithTeamData]]]:
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
    json_body: SearchChannelsForRetentionPolicyJsonBody,
) -> Response[Union[Any, List[ChannelWithTeamData]]]:
    """Search for the channels in a granular data retention policy

     Searches for the channels to which a granular data retention policy is applied.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (SearchChannelsForRetentionPolicyJsonBody):

    Returns:
        Response[Union[Any, List[ChannelWithTeamData]]]
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
    json_body: SearchChannelsForRetentionPolicyJsonBody,
) -> Optional[Union[Any, List[ChannelWithTeamData]]]:
    """Search for the channels in a granular data retention policy

     Searches for the channels to which a granular data retention policy is applied.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (SearchChannelsForRetentionPolicyJsonBody):

    Returns:
        Response[Union[Any, List[ChannelWithTeamData]]]
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
    json_body: SearchChannelsForRetentionPolicyJsonBody,
) -> Response[Union[Any, List[ChannelWithTeamData]]]:
    """Search for the channels in a granular data retention policy

     Searches for the channels to which a granular data retention policy is applied.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (SearchChannelsForRetentionPolicyJsonBody):

    Returns:
        Response[Union[Any, List[ChannelWithTeamData]]]
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
    json_body: SearchChannelsForRetentionPolicyJsonBody,
) -> Optional[Union[Any, List[ChannelWithTeamData]]]:
    """Search for the channels in a granular data retention policy

     Searches for the channels to which a granular data retention policy is applied.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (SearchChannelsForRetentionPolicyJsonBody):

    Returns:
        Response[Union[Any, List[ChannelWithTeamData]]]
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
