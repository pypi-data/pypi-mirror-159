from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.status_ok import StatusOK
from ...models.upload_saml_public_certificate_multipart_data import UploadSamlPublicCertificateMultipartData
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    multipart_data: UploadSamlPublicCertificateMultipartData,
) -> Dict[str, Any]:
    url = "{}/saml/certificate/public".format(client.base_url)

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    multipart_multipart_data = multipart_data.to_multipart()

    return {
        "method": "post",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
        "files": multipart_multipart_data,
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
    *,
    client: Client,
    multipart_data: UploadSamlPublicCertificateMultipartData,
) -> Response[Union[Any, StatusOK]]:
    """Upload public certificate

     Upload the public certificate to be used for encryption with your SAML configuration. The server
    will pick a hard-coded filename for the PublicCertificateFile setting in your `config.json`.
    ##### Permissions
    Must have `sysconsole_write_authentication` permission.

    Args:
        multipart_data (UploadSamlPublicCertificateMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    *,
    client: Client,
    multipart_data: UploadSamlPublicCertificateMultipartData,
) -> Optional[Union[Any, StatusOK]]:
    """Upload public certificate

     Upload the public certificate to be used for encryption with your SAML configuration. The server
    will pick a hard-coded filename for the PublicCertificateFile setting in your `config.json`.
    ##### Permissions
    Must have `sysconsole_write_authentication` permission.

    Args:
        multipart_data (UploadSamlPublicCertificateMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return sync_detailed(
        client=client,
        multipart_data=multipart_data,
    ).parsed


async def asyncio_detailed(
    *,
    client: Client,
    multipart_data: UploadSamlPublicCertificateMultipartData,
) -> Response[Union[Any, StatusOK]]:
    """Upload public certificate

     Upload the public certificate to be used for encryption with your SAML configuration. The server
    will pick a hard-coded filename for the PublicCertificateFile setting in your `config.json`.
    ##### Permissions
    Must have `sysconsole_write_authentication` permission.

    Args:
        multipart_data (UploadSamlPublicCertificateMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    kwargs = _get_kwargs(
        client=client,
        multipart_data=multipart_data,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    *,
    client: Client,
    multipart_data: UploadSamlPublicCertificateMultipartData,
) -> Optional[Union[Any, StatusOK]]:
    """Upload public certificate

     Upload the public certificate to be used for encryption with your SAML configuration. The server
    will pick a hard-coded filename for the PublicCertificateFile setting in your `config.json`.
    ##### Permissions
    Must have `sysconsole_write_authentication` permission.

    Args:
        multipart_data (UploadSamlPublicCertificateMultipartData):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
            multipart_data=multipart_data,
        )
    ).parsed
