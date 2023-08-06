from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.get_saml_metadata_from_idp_json_body import GetSamlMetadataFromIdpJsonBody
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Dict[str, Any]:
    url = "{}/saml/metadatafromidp".format(client.base_url)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, str]]:
    if response.status_code == 200:
        response_200 = cast(str, response.json())
        return response_200
    if response.status_code == 501:
        response_501 = cast(Any, None)
        return response_501
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, str]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    *,
    client: Client,
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Response[Union[Any, str]]:
    """Get metadata from Identity Provider

     Get SAML metadata from the Identity Provider. SAML must be configured properly.
    ##### Permissions
    No permission required.

    Args:
        json_body (GetSamlMetadataFromIdpJsonBody):

    Returns:
        Response[Union[Any, str]]
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
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Optional[Union[Any, str]]:
    """Get metadata from Identity Provider

     Get SAML metadata from the Identity Provider. SAML must be configured properly.
    ##### Permissions
    No permission required.

    Args:
        json_body (GetSamlMetadataFromIdpJsonBody):

    Returns:
        Response[Union[Any, str]]
    """

    return sync_detailed(
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Response[Union[Any, str]]:
    """Get metadata from Identity Provider

     Get SAML metadata from the Identity Provider. SAML must be configured properly.
    ##### Permissions
    No permission required.

    Args:
        json_body (GetSamlMetadataFromIdpJsonBody):

    Returns:
        Response[Union[Any, str]]
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
    json_body: GetSamlMetadataFromIdpJsonBody,
) -> Optional[Union[Any, str]]:
    """Get metadata from Identity Provider

     Get SAML metadata from the Identity Provider. SAML must be configured properly.
    ##### Permissions
    No permission required.

    Args:
        json_body (GetSamlMetadataFromIdpJsonBody):

    Returns:
        Response[Union[Any, str]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
