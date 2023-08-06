from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.retention_policy_for_team_list import RetentionPolicyForTeamList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/data_retention/team_policies".format(client.base_url, user_id=user_id)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, RetentionPolicyForTeamList]]:
    if response.status_code == 200:
        response_200 = RetentionPolicyForTeamList.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, RetentionPolicyForTeamList]]:
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
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, RetentionPolicyForTeamList]]:
    """Get the policies which are applied to a user's teams

     Gets the policies which are applied to the all of the teams to which a user belongs.

    __Minimum server version__: 5.35

    ##### Permissions
    Must be logged in as the user or have the `manage_system` permission.

    ##### License
    Requires an E20 license.

    Args:
        user_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, RetentionPolicyForTeamList]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
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
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, RetentionPolicyForTeamList]]:
    """Get the policies which are applied to a user's teams

     Gets the policies which are applied to the all of the teams to which a user belongs.

    __Minimum server version__: 5.35

    ##### Permissions
    Must be logged in as the user or have the `manage_system` permission.

    ##### License
    Requires an E20 license.

    Args:
        user_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, RetentionPolicyForTeamList]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        page=page,
        per_page=per_page,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Response[Union[Any, RetentionPolicyForTeamList]]:
    """Get the policies which are applied to a user's teams

     Gets the policies which are applied to the all of the teams to which a user belongs.

    __Minimum server version__: 5.35

    ##### Permissions
    Must be logged in as the user or have the `manage_system` permission.

    ##### License
    Requires an E20 license.

    Args:
        user_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, RetentionPolicyForTeamList]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
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
    page: Union[Unset, None, int] = 0,
    per_page: Union[Unset, None, int] = 60,
) -> Optional[Union[Any, RetentionPolicyForTeamList]]:
    """Get the policies which are applied to a user's teams

     Gets the policies which are applied to the all of the teams to which a user belongs.

    __Minimum server version__: 5.35

    ##### Permissions
    Must be logged in as the user or have the `manage_system` permission.

    ##### License
    Requires an E20 license.

    Args:
        user_id (str):
        page (Union[Unset, None, int]):
        per_page (Union[Unset, None, int]):  Default: 60.

    Returns:
        Response[Union[Any, RetentionPolicyForTeamList]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            page=page,
            per_page=per_page,
        )
    ).parsed
