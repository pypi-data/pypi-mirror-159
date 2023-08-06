from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...models.update_channel_scheme_json_body import UpdateChannelSchemeJsonBody
from ...types import Response


def _get_kwargs(
    channel_id: str,
    *,
    client: Client,
    json_body: UpdateChannelSchemeJsonBody,
) -> Dict[str, Any]:
    url = "{}/channels/{channel_id}/scheme".format(client.base_url, channel_id=channel_id)

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
    channel_id: str,
    *,
    client: Client,
    json_body: UpdateChannelSchemeJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Set a channel's scheme

     Set a channel's scheme, more specifically sets the scheme_id value of a channel record.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 4.10

    Args:
        channel_id (str):
        json_body (UpdateChannelSchemeJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    channel_id: str,
    *,
    client: Client,
    json_body: UpdateChannelSchemeJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Set a channel's scheme

     Set a channel's scheme, more specifically sets the scheme_id value of a channel record.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 4.10

    Args:
        channel_id (str):
        json_body (UpdateChannelSchemeJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        channel_id=channel_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    channel_id: str,
    *,
    client: Client,
    json_body: UpdateChannelSchemeJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Set a channel's scheme

     Set a channel's scheme, more specifically sets the scheme_id value of a channel record.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 4.10

    Args:
        channel_id (str):
        json_body (UpdateChannelSchemeJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        channel_id=channel_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    channel_id: str,
    *,
    client: Client,
    json_body: UpdateChannelSchemeJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Set a channel's scheme

     Set a channel's scheme, more specifically sets the scheme_id value of a channel record.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 4.10

    Args:
        channel_id (str):
        json_body (UpdateChannelSchemeJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            channel_id=channel_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
