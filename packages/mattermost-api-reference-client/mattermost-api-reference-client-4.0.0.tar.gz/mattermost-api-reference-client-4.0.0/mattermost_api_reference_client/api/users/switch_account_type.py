from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.switch_account_type_json_body import SwitchAccountTypeJsonBody
from ...models.switch_account_type_response_200 import SwitchAccountTypeResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SwitchAccountTypeJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/login/switch".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, SwitchAccountTypeResponse200]]:
    if response.status_code == 200:
        response_200 = SwitchAccountTypeResponse200.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, SwitchAccountTypeResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: SwitchAccountTypeJsonBody,
) -> Response[Union[Any, SwitchAccountTypeResponse200]]:
    """Switch login method

     Switch a user's login method from using email to OAuth2/SAML/LDAP or back to email. When switching
    to OAuth2/SAML, account switching is not complete until the user follows the returned link and
    completes any steps on the OAuth2/SAML service provider.

    To switch from email to OAuth2/SAML, specify `current_service`, `new_service`, `email` and
    `password`.

    To switch from OAuth2/SAML to email, specify `current_service`, `new_service`, `email` and
    `new_password`.

    To switch from email to LDAP/AD, specify `current_service`, `new_service`, `email`, `password`,
    `ldap_ip` and `new_password` (this is the user's LDAP password).

    To switch from LDAP/AD to email, specify `current_service`, `new_service`, `ldap_ip`, `password`
    (this is the user's LDAP password), `email`  and `new_password`.

    Additionally, specify `mfa_code` when trying to switch an account on LDAP/AD or email that has MFA
    activated.

    ##### Permissions
    No current authentication required except when switching from OAuth2/SAML to email.

    Args:
        json_body (SwitchAccountTypeJsonBody):

    Returns:
        Response[Union[Any, SwitchAccountTypeResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    json_body: SwitchAccountTypeJsonBody,
) -> Optional[Union[Any, SwitchAccountTypeResponse200]]:
    """Switch login method

     Switch a user's login method from using email to OAuth2/SAML/LDAP or back to email. When switching
    to OAuth2/SAML, account switching is not complete until the user follows the returned link and
    completes any steps on the OAuth2/SAML service provider.

    To switch from email to OAuth2/SAML, specify `current_service`, `new_service`, `email` and
    `password`.

    To switch from OAuth2/SAML to email, specify `current_service`, `new_service`, `email` and
    `new_password`.

    To switch from email to LDAP/AD, specify `current_service`, `new_service`, `email`, `password`,
    `ldap_ip` and `new_password` (this is the user's LDAP password).

    To switch from LDAP/AD to email, specify `current_service`, `new_service`, `ldap_ip`, `password`
    (this is the user's LDAP password), `email`  and `new_password`.

    Additionally, specify `mfa_code` when trying to switch an account on LDAP/AD or email that has MFA
    activated.

    ##### Permissions
    No current authentication required except when switching from OAuth2/SAML to email.

    Args:
        json_body (SwitchAccountTypeJsonBody):

    Returns:
        Response[Union[Any, SwitchAccountTypeResponse200]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: SwitchAccountTypeJsonBody,
) -> Response[Union[Any, SwitchAccountTypeResponse200]]:
    """Switch login method

     Switch a user's login method from using email to OAuth2/SAML/LDAP or back to email. When switching
    to OAuth2/SAML, account switching is not complete until the user follows the returned link and
    completes any steps on the OAuth2/SAML service provider.

    To switch from email to OAuth2/SAML, specify `current_service`, `new_service`, `email` and
    `password`.

    To switch from OAuth2/SAML to email, specify `current_service`, `new_service`, `email` and
    `new_password`.

    To switch from email to LDAP/AD, specify `current_service`, `new_service`, `email`, `password`,
    `ldap_ip` and `new_password` (this is the user's LDAP password).

    To switch from LDAP/AD to email, specify `current_service`, `new_service`, `ldap_ip`, `password`
    (this is the user's LDAP password), `email`  and `new_password`.

    Additionally, specify `mfa_code` when trying to switch an account on LDAP/AD or email that has MFA
    activated.

    ##### Permissions
    No current authentication required except when switching from OAuth2/SAML to email.

    Args:
        json_body (SwitchAccountTypeJsonBody):

    Returns:
        Response[Union[Any, SwitchAccountTypeResponse200]]
    """

    kwargs = _get_kwargs(
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    json_body: SwitchAccountTypeJsonBody,
) -> Optional[Union[Any, SwitchAccountTypeResponse200]]:
    """Switch login method

     Switch a user's login method from using email to OAuth2/SAML/LDAP or back to email. When switching
    to OAuth2/SAML, account switching is not complete until the user follows the returned link and
    completes any steps on the OAuth2/SAML service provider.

    To switch from email to OAuth2/SAML, specify `current_service`, `new_service`, `email` and
    `password`.

    To switch from OAuth2/SAML to email, specify `current_service`, `new_service`, `email` and
    `new_password`.

    To switch from email to LDAP/AD, specify `current_service`, `new_service`, `email`, `password`,
    `ldap_ip` and `new_password` (this is the user's LDAP password).

    To switch from LDAP/AD to email, specify `current_service`, `new_service`, `ldap_ip`, `password`
    (this is the user's LDAP password), `email`  and `new_password`.

    Additionally, specify `mfa_code` when trying to switch an account on LDAP/AD or email that has MFA
    activated.

    ##### Permissions
    No current authentication required except when switching from OAuth2/SAML to email.

    Args:
        json_body (SwitchAccountTypeJsonBody):

    Returns:
        Response[Union[Any, SwitchAccountTypeResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
