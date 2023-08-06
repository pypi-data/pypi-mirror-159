from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.payment_setup_intent import PaymentSetupIntent
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/cloud/payment".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, PaymentSetupIntent]]:
    if response.status_code == 201:
        response_201 = PaymentSetupIntent.from_dict(response.json())

        return response_201
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


def _build_response(*, response: httpx.Response) -> Response[Union[Any, PaymentSetupIntent]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, PaymentSetupIntent]]:
    """Create a customer setup payment intent

     Creates a customer setup payment intent for the given Mattermost cloud installation.

    ##### Permissions

    Must have `manage_system` permission and be licensed for Cloud.

    __Minimum server version__: 5.28
    __Note:__: This is intended for internal use and is subject to change.

    Returns:
        Response[Union[Any, PaymentSetupIntent]]
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
) -> Optional[Union[Any, PaymentSetupIntent]]:
    """Create a customer setup payment intent

     Creates a customer setup payment intent for the given Mattermost cloud installation.

    ##### Permissions

    Must have `manage_system` permission and be licensed for Cloud.

    __Minimum server version__: 5.28
    __Note:__: This is intended for internal use and is subject to change.

    Returns:
        Response[Union[Any, PaymentSetupIntent]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, PaymentSetupIntent]]:
    """Create a customer setup payment intent

     Creates a customer setup payment intent for the given Mattermost cloud installation.

    ##### Permissions

    Must have `manage_system` permission and be licensed for Cloud.

    __Minimum server version__: 5.28
    __Note:__: This is intended for internal use and is subject to change.

    Returns:
        Response[Union[Any, PaymentSetupIntent]]
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
) -> Optional[Union[Any, PaymentSetupIntent]]:
    """Create a customer setup payment intent

     Creates a customer setup payment intent for the given Mattermost cloud installation.

    ##### Permissions

    Must have `manage_system` permission and be licensed for Cloud.

    __Minimum server version__: 5.28
    __Note:__: This is intended for internal use and is subject to change.

    Returns:
        Response[Union[Any, PaymentSetupIntent]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
