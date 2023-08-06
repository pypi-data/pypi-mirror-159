from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...models.test_site_url_json_body import TestSiteURLJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: TestSiteURLJsonBody,
) -> Dict[str, Any]:
    url = "{}/site_url/test".format(client.base_url)

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
    json_body: TestSiteURLJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Checks the validity of a Site URL

     Sends a Ping request to the mattermost server using the specified Site URL.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        json_body (TestSiteURLJsonBody):

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
    json_body: TestSiteURLJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Checks the validity of a Site URL

     Sends a Ping request to the mattermost server using the specified Site URL.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        json_body (TestSiteURLJsonBody):

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
    json_body: TestSiteURLJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Checks the validity of a Site URL

     Sends a Ping request to the mattermost server using the specified Site URL.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        json_body (TestSiteURLJsonBody):

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
    json_body: TestSiteURLJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Checks the validity of a Site URL

     Sends a Ping request to the mattermost server using the specified Site URL.

    ##### Permissions
    Must have `manage_system` permission.

    __Minimum server version__: 5.16

    Args:
        json_body (TestSiteURLJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
