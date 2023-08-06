from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.enable_user_access_token_json_body import EnableUserAccessTokenJsonBody
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: EnableUserAccessTokenJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/tokens/enable".format(client.base_url)

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
    *,
    client: Client,
    json_body: EnableUserAccessTokenJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Enable personal access token

     Re-enable a personal access token that has been disabled.

    __Minimum server version__: 4.4

    ##### Permissions
    Must have `create_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        json_body (EnableUserAccessTokenJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
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
    json_body: EnableUserAccessTokenJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Enable personal access token

     Re-enable a personal access token that has been disabled.

    __Minimum server version__: 4.4

    ##### Permissions
    Must have `create_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        json_body (EnableUserAccessTokenJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: EnableUserAccessTokenJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Enable personal access token

     Re-enable a personal access token that has been disabled.

    __Minimum server version__: 4.4

    ##### Permissions
    Must have `create_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        json_body (EnableUserAccessTokenJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
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
    json_body: EnableUserAccessTokenJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Enable personal access token

     Re-enable a personal access token that has been disabled.

    __Minimum server version__: 4.4

    ##### Permissions
    Must have `create_user_access_token` permission. For non-self requests, must also have the
    `edit_other_users` permission.

    Args:
        json_body (EnableUserAccessTokenJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
