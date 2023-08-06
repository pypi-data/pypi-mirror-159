from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/warn_metrics/status".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
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
) -> Response[Union[Any, StatusOK]]:
    """Get the warn metrics status (enabled or disabled)

     Get the status of a set of metrics (enabled or disabled) from the Systems table.

    The returned JSON contains the metrics that we need to warn the admin on with regard
    to their status (we return the ones whose status is \"true\", which means that they are
    in a \"warnable\" state - e.g. a threshold has been crossed or some other condition has
    been fulfilled).

    __Minimum server version__: 5.26

    ##### Permissions

    Must have `manage_system` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Get the warn metrics status (enabled or disabled)

     Get the status of a set of metrics (enabled or disabled) from the Systems table.

    The returned JSON contains the metrics that we need to warn the admin on with regard
    to their status (we return the ones whose status is \"true\", which means that they are
    in a \"warnable\" state - e.g. a threshold has been crossed or some other condition has
    been fulfilled).

    __Minimum server version__: 5.26

    ##### Permissions

    Must have `manage_system` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, StatusOK]]:
    """Get the warn metrics status (enabled or disabled)

     Get the status of a set of metrics (enabled or disabled) from the Systems table.

    The returned JSON contains the metrics that we need to warn the admin on with regard
    to their status (we return the ones whose status is \"true\", which means that they are
    in a \"warnable\" state - e.g. a threshold has been crossed or some other condition has
    been fulfilled).

    __Minimum server version__: 5.26

    ##### Permissions

    Must have `manage_system` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
) -> Optional[Union[Any, StatusOK]]:
    """Get the warn metrics status (enabled or disabled)

     Get the status of a set of metrics (enabled or disabled) from the Systems table.

    The returned JSON contains the metrics that we need to warn the admin on with regard
    to their status (we return the ones whose status is \"true\", which means that they are
    in a \"warnable\" state - e.g. a threshold has been crossed or some other condition has
    been fulfilled).

    __Minimum server version__: 5.26

    ##### Permissions

    Must have `manage_system` permission.

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
