from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...models.update_user_mfa_json_body import UpdateUserMfaJsonBody
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: UpdateUserMfaJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/mfa".format(client.base_url, user_id=user_id)

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
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
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
    json_body: UpdateUserMfaJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Update a user's MFA

     Activates multi-factor authentication for the user if `activate` is true and a valid `code` is
    provided. If activate is false, then `code` is not required and multi-factor authentication is
    disabled for the user.
    ##### Permissions
    Must be logged in as the user being updated or have the `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (UpdateUserMfaJsonBody):

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
    json_body: UpdateUserMfaJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Update a user's MFA

     Activates multi-factor authentication for the user if `activate` is true and a valid `code` is
    provided. If activate is false, then `code` is not required and multi-factor authentication is
    disabled for the user.
    ##### Permissions
    Must be logged in as the user being updated or have the `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (UpdateUserMfaJsonBody):

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
    json_body: UpdateUserMfaJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Update a user's MFA

     Activates multi-factor authentication for the user if `activate` is true and a valid `code` is
    provided. If activate is false, then `code` is not required and multi-factor authentication is
    disabled for the user.
    ##### Permissions
    Must be logged in as the user being updated or have the `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (UpdateUserMfaJsonBody):

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
    json_body: UpdateUserMfaJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Update a user's MFA

     Activates multi-factor authentication for the user if `activate` is true and a valid `code` is
    provided. If activate is false, then `code` is not required and multi-factor authentication is
    disabled for the user.
    ##### Permissions
    Must be logged in as the user being updated or have the `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (UpdateUserMfaJsonBody):

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
