from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.config import Config
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: Config,
) -> Dict[str, Any]:
    url = "{}/file/s3_test".format(client.base_url)

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
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
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
    json_body: Config,
) -> Response[Union[Any, StatusOK]]:
    """Test AWS S3 connection

     Send a test to validate if can connect to AWS S3. Optionally provide a configuration in the request
    body to test. If no valid configuration is present in the request body the current server
    configuration will be tested.
    ##### Permissions
    Must have `manage_system` permission.
    __Minimum server version__: 4.8

    Args:
        json_body (Config):

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
    json_body: Config,
) -> Optional[Union[Any, StatusOK]]:
    """Test AWS S3 connection

     Send a test to validate if can connect to AWS S3. Optionally provide a configuration in the request
    body to test. If no valid configuration is present in the request body the current server
    configuration will be tested.
    ##### Permissions
    Must have `manage_system` permission.
    __Minimum server version__: 4.8

    Args:
        json_body (Config):

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
    json_body: Config,
) -> Response[Union[Any, StatusOK]]:
    """Test AWS S3 connection

     Send a test to validate if can connect to AWS S3. Optionally provide a configuration in the request
    body to test. If no valid configuration is present in the request body the current server
    configuration will be tested.
    ##### Permissions
    Must have `manage_system` permission.
    __Minimum server version__: 4.8

    Args:
        json_body (Config):

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
    json_body: Config,
) -> Optional[Union[Any, StatusOK]]:
    """Test AWS S3 connection

     Send a test to validate if can connect to AWS S3. Optionally provide a configuration in the request
    body to test. If no valid configuration is present in the request body the current server
    configuration will be tested.
    ##### Permissions
    Must have `manage_system` permission.
    __Minimum server version__: 4.8

    Args:
        json_body (Config):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
