from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.create_user_json_body import CreateUserJsonBody
from ...models.user import User
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    client: Client,
    json_body: CreateUserJsonBody,
    t: Union[Unset, None, str] = UNSET,
    iid: Union[Unset, None, str] = UNSET,
) -> Dict[str, Any]:
    url = "{}/users".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    params: Dict[str, Any] = {}
    params["t"] = t

    params["iid"] = iid

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    json_json_body = json_body.to_dict()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "json": json_json_body,
        "params": params,
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, User]]:
    if response.status_code == 201:
        response_201 = User.from_dict(response.json())

        return response_201
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, User]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: CreateUserJsonBody,
    t: Union[Unset, None, str] = UNSET,
    iid: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, User]]:
    """Create a user

     Create a new user on the system. Password is required for email login. For other authentication
    types such as LDAP or SAML, auth_data and auth_service fields are required.
    ##### Permissions
    No permission required for creating email/username accounts on an open server. Auth Token is
    required for other authentication types such as LDAP or SAML.

    Args:
        t (Union[Unset, None, str]):
        iid (Union[Unset, None, str]):
        json_body (CreateUserJsonBody):

    Returns:
        Response[Union[Any, User]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        t=t,
        iid=iid,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: CreateUserJsonBody,
    t: Union[Unset, None, str] = UNSET,
    iid: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, User]]:
    """Create a user

     Create a new user on the system. Password is required for email login. For other authentication
    types such as LDAP or SAML, auth_data and auth_service fields are required.
    ##### Permissions
    No permission required for creating email/username accounts on an open server. Auth Token is
    required for other authentication types such as LDAP or SAML.

    Args:
        t (Union[Unset, None, str]):
        iid (Union[Unset, None, str]):
        json_body (CreateUserJsonBody):

    Returns:
        Response[Union[Any, User]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
        t=t,
        iid=iid,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: CreateUserJsonBody,
    t: Union[Unset, None, str] = UNSET,
    iid: Union[Unset, None, str] = UNSET,
) -> Response[Union[Any, User]]:
    """Create a user

     Create a new user on the system. Password is required for email login. For other authentication
    types such as LDAP or SAML, auth_data and auth_service fields are required.
    ##### Permissions
    No permission required for creating email/username accounts on an open server. Auth Token is
    required for other authentication types such as LDAP or SAML.

    Args:
        t (Union[Unset, None, str]):
        iid (Union[Unset, None, str]):
        json_body (CreateUserJsonBody):

    Returns:
        Response[Union[Any, User]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
        t=t,
        iid=iid,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: CreateUserJsonBody,
    t: Union[Unset, None, str] = UNSET,
    iid: Union[Unset, None, str] = UNSET,
) -> Optional[Union[Any, User]]:
    """Create a user

     Create a new user on the system. Password is required for email login. For other authentication
    types such as LDAP or SAML, auth_data and auth_service fields are required.
    ##### Permissions
    No permission required for creating email/username accounts on an open server. Auth Token is
    required for other authentication types such as LDAP or SAML.

    Args:
        t (Union[Unset, None, str]):
        iid (Union[Unset, None, str]):
        json_body (CreateUserJsonBody):

    Returns:
        Response[Union[Any, User]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
            t=t,
            iid=iid,
        )
    ).parsed
