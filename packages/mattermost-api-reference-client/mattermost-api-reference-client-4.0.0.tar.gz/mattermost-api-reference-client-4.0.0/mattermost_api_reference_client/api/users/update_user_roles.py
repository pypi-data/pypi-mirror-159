from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...models.update_user_roles_json_body import UpdateUserRolesJsonBody
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserRolesJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/roles".format(client.base_url, user_id=user_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, StatusOK]]:
    if response.status_code == 200:
        response_200 = StatusOK.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, StatusOK]]:
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
    json_body: UpdateUserRolesJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Update a user's roles

     Update a user's system-level roles. Valid user roles are \"system_user\", \"system_admin\" or both
    of them. Overwrites any previously assigned system-level roles.
    ##### Permissions
    Must have the `manage_roles` permission.

    Args:
        user_id (str):
        json_body (UpdateUserRolesJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
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
    json_body: UpdateUserRolesJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Update a user's roles

     Update a user's system-level roles. Valid user roles are \"system_user\", \"system_admin\" or both
    of them. Overwrites any previously assigned system-level roles.
    ##### Permissions
    Must have the `manage_roles` permission.

    Args:
        user_id (str):
        json_body (UpdateUserRolesJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        user_id=user_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserRolesJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Update a user's roles

     Update a user's system-level roles. Valid user roles are \"system_user\", \"system_admin\" or both
    of them. Overwrites any previously assigned system-level roles.
    ##### Permissions
    Must have the `manage_roles` permission.

    Args:
        user_id (str):
        json_body (UpdateUserRolesJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserRolesJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Update a user's roles

     Update a user's system-level roles. Valid user roles are \"system_user\", \"system_admin\" or both
    of them. Overwrites any previously assigned system-level roles.
    ##### Permissions
    Must have the `manage_roles` permission.

    Args:
        user_id (str):
        json_body (UpdateUserRolesJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
