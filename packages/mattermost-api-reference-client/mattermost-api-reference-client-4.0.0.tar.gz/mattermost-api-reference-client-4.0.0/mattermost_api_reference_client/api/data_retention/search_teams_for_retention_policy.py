from typing import Any, Dict, List, Optional, Union, cast

import httpx

from ...client import Client
from ...models.search_teams_for_retention_policy_json_body import SearchTeamsForRetentionPolicyJsonBody
from ...models.team import Team
from ...types import Response


def _get_kwargs(
    policy_id: str,
    *,
    client: Client,
    json_body: SearchTeamsForRetentionPolicyJsonBody,
) -> Dict[str, Any]:
    url = "{}/data_retention/policies/{policy_id}/teams/search".format(client.base_url, policy_id=policy_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, List[Team]]]:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = Team.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, List[Team]]]:
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
    json_body: SearchTeamsForRetentionPolicyJsonBody,
) -> Response[Union[Any, List[Team]]]:
    """Search for the teams in a granular data retention policy

     Searches for the teams to which a granular data retention policy is applied.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (SearchTeamsForRetentionPolicyJsonBody):

    Returns:
        Response[Union[Any, List[Team]]]
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
    json_body: SearchTeamsForRetentionPolicyJsonBody,
) -> Optional[Union[Any, List[Team]]]:
    """Search for the teams in a granular data retention policy

     Searches for the teams to which a granular data retention policy is applied.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (SearchTeamsForRetentionPolicyJsonBody):

    Returns:
        Response[Union[Any, List[Team]]]
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
    json_body: SearchTeamsForRetentionPolicyJsonBody,
) -> Response[Union[Any, List[Team]]]:
    """Search for the teams in a granular data retention policy

     Searches for the teams to which a granular data retention policy is applied.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (SearchTeamsForRetentionPolicyJsonBody):

    Returns:
        Response[Union[Any, List[Team]]]
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
    json_body: SearchTeamsForRetentionPolicyJsonBody,
) -> Optional[Union[Any, List[Team]]]:
    """Search for the teams in a granular data retention policy

     Searches for the teams to which a granular data retention policy is applied.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Args:
        policy_id (str):
        json_body (SearchTeamsForRetentionPolicyJsonBody):

    Returns:
        Response[Union[Any, List[Team]]]
    """

    return (
        await asyncio_detailed(
            policy_id=policy_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
