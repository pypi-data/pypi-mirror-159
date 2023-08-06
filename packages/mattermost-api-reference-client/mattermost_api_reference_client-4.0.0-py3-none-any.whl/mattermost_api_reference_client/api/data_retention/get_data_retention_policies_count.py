from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_data_retention_policies_count_response_200 import GetDataRetentionPoliciesCountResponse200
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/data_retention/policies_count".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, GetDataRetentionPoliciesCountResponse200]]:
    if response.status_code == 200:
        response_200 = GetDataRetentionPoliciesCountResponse200.from_dict(response.json())

        return response_200
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    if response.status_code == 403:
        response_403 = cast(Any, None)
        return response_403
    if response.status_code == 500:
        response_500 = cast(Any, None)
        return response_500
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, GetDataRetentionPoliciesCountResponse200]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
) -> Response[Union[Any, GetDataRetentionPoliciesCountResponse200]]:
    """Get the number of granular data retention policies

     Gets the number of granular (i.e. team or channel-specific) data retention
    policies from the server.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Returns:
        Response[Union[Any, GetDataRetentionPoliciesCountResponse200]]
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
) -> Optional[Union[Any, GetDataRetentionPoliciesCountResponse200]]:
    """Get the number of granular data retention policies

     Gets the number of granular (i.e. team or channel-specific) data retention
    policies from the server.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Returns:
        Response[Union[Any, GetDataRetentionPoliciesCountResponse200]]
    """

    return sync_detailed(
        client=client,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
) -> Response[Union[Any, GetDataRetentionPoliciesCountResponse200]]:
    """Get the number of granular data retention policies

     Gets the number of granular (i.e. team or channel-specific) data retention
    policies from the server.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Returns:
        Response[Union[Any, GetDataRetentionPoliciesCountResponse200]]
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
) -> Optional[Union[Any, GetDataRetentionPoliciesCountResponse200]]:
    """Get the number of granular data retention policies

     Gets the number of granular (i.e. team or channel-specific) data retention
    policies from the server.

    __Minimum server version__: 5.35

    ##### Permissions
    Must have the `sysconsole_read_compliance_data_retention` permission.

    ##### License
    Requires an E20 license.

    Returns:
        Response[Union[Any, GetDataRetentionPoliciesCountResponse200]]
    """

    return (
        await asyncio_detailed(
            client=client,
        )
    ).parsed
