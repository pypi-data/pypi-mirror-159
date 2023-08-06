from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.user_auth_data import UserAuthData
from ...types import Response


def _get_kwargs(
    user_id: str,
    *,
    client: Client,
    json_body: UserAuthData,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/auth".format(client.base_url, user_id=user_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, UserAuthData]]:
    if response.status_code == 200:
        response_200 = UserAuthData.from_dict(response.json())

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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, UserAuthData]]:
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
    json_body: UserAuthData,
) -> Response[Union[Any, UserAuthData]]:
    """Update a user's authentication method

     Updates a user's authentication method. This can be used to change them to/from LDAP authentication
    for example.

    __Minimum server version__: 4.6
    ##### Permissions
    Must have the `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (UserAuthData):

    Returns:
        Response[Union[Any, UserAuthData]]
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
    json_body: UserAuthData,
) -> Optional[Union[Any, UserAuthData]]:
    """Update a user's authentication method

     Updates a user's authentication method. This can be used to change them to/from LDAP authentication
    for example.

    __Minimum server version__: 4.6
    ##### Permissions
    Must have the `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (UserAuthData):

    Returns:
        Response[Union[Any, UserAuthData]]
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
    json_body: UserAuthData,
) -> Response[Union[Any, UserAuthData]]:
    """Update a user's authentication method

     Updates a user's authentication method. This can be used to change them to/from LDAP authentication
    for example.

    __Minimum server version__: 4.6
    ##### Permissions
    Must have the `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (UserAuthData):

    Returns:
        Response[Union[Any, UserAuthData]]
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
    json_body: UserAuthData,
) -> Optional[Union[Any, UserAuthData]]:
    """Update a user's authentication method

     Updates a user's authentication method. This can be used to change them to/from LDAP authentication
    for example.

    __Minimum server version__: 4.6
    ##### Permissions
    Must have the `edit_other_users` permission.

    Args:
        user_id (str):
        json_body (UserAuthData):

    Returns:
        Response[Union[Any, UserAuthData]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
