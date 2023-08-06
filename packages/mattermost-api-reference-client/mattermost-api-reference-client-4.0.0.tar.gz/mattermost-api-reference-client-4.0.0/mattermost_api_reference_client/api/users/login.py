from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.login_json_body import LoginJsonBody
from ...models.user import User
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: LoginJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/login".format(client.base_url)

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
    json_body: LoginJsonBody,
) -> Response[Union[Any, User]]:
    """Login to Mattermost server

     ##### Permissions
    No permission required

    Args:
        json_body (LoginJsonBody):

    Returns:
        Response[Union[Any, User]]
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
    json_body: LoginJsonBody,
) -> Optional[Union[Any, User]]:
    """Login to Mattermost server

     ##### Permissions
    No permission required

    Args:
        json_body (LoginJsonBody):

    Returns:
        Response[Union[Any, User]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: LoginJsonBody,
) -> Response[Union[Any, User]]:
    """Login to Mattermost server

     ##### Permissions
    No permission required

    Args:
        json_body (LoginJsonBody):

    Returns:
        Response[Union[Any, User]]
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
    json_body: LoginJsonBody,
) -> Optional[Union[Any, User]]:
    """Login to Mattermost server

     ##### Permissions
    No permission required

    Args:
        json_body (LoginJsonBody):

    Returns:
        Response[Union[Any, User]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
