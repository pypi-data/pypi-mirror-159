from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.config import Config
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Config,
) -> Dict[str, Any]:
    url = "{}/config".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Config]]:
    if response.status_code == 200:
        response_200 = Config.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Config]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: Config,
) -> Response[Union[Any, Config]]:
    """Update configuration

     Submit a new configuration for the server to use. As of server version 4.8, the
    `PluginSettings.EnableUploads` setting cannot be modified by this endpoint.
    Note that the parameters that aren't set in the configuration that you provide will be reset to
    default values. Therefore, if you want to change a configuration parameter and leave the other ones
    unchanged, you need to get the existing configuration first, change the field that you want, then
    put that new configuration.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (Config):

    Returns:
        Response[Union[Any, Config]]
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
    json_body: Config,
) -> Optional[Union[Any, Config]]:
    """Update configuration

     Submit a new configuration for the server to use. As of server version 4.8, the
    `PluginSettings.EnableUploads` setting cannot be modified by this endpoint.
    Note that the parameters that aren't set in the configuration that you provide will be reset to
    default values. Therefore, if you want to change a configuration parameter and leave the other ones
    unchanged, you need to get the existing configuration first, change the field that you want, then
    put that new configuration.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (Config):

    Returns:
        Response[Union[Any, Config]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: Config,
) -> Response[Union[Any, Config]]:
    """Update configuration

     Submit a new configuration for the server to use. As of server version 4.8, the
    `PluginSettings.EnableUploads` setting cannot be modified by this endpoint.
    Note that the parameters that aren't set in the configuration that you provide will be reset to
    default values. Therefore, if you want to change a configuration parameter and leave the other ones
    unchanged, you need to get the existing configuration first, change the field that you want, then
    put that new configuration.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (Config):

    Returns:
        Response[Union[Any, Config]]
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
    json_body: Config,
) -> Optional[Union[Any, Config]]:
    """Update configuration

     Submit a new configuration for the server to use. As of server version 4.8, the
    `PluginSettings.EnableUploads` setting cannot be modified by this endpoint.
    Note that the parameters that aren't set in the configuration that you provide will be reset to
    default values. Therefore, if you want to change a configuration parameter and leave the other ones
    unchanged, you need to get the existing configuration first, change the field that you want, then
    put that new configuration.
    ##### Permissions
    Must have `manage_system` permission.

    Args:
        json_body (Config):

    Returns:
        Response[Union[Any, Config]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
