from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.send_verification_email_json_body import SendVerificationEmailJsonBody
from ...models.status_ok import StatusOK
from ...types import Response


def _get_kwargs(
    *,
    client: Client,
    json_body: SendVerificationEmailJsonBody,
) -> Dict[str, Any]:
    url = "{}/users/email/verify/send".format(client.base_url)

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
    json_body: SendVerificationEmailJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Send verification email

     Send an email with a verification link to a user that has an email matching the one in the request
    body. This endpoint will return success even if the email does not match any users on the system.
    ##### Permissions
    No permissions required.

    Args:
        json_body (SendVerificationEmailJsonBody):

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
    json_body: SendVerificationEmailJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Send verification email

     Send an email with a verification link to a user that has an email matching the one in the request
    body. This endpoint will return success even if the email does not match any users on the system.
    ##### Permissions
    No permissions required.

    Args:
        json_body (SendVerificationEmailJsonBody):

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
    json_body: SendVerificationEmailJsonBody,
) -> Response[Union[Any, StatusOK]]:
    """Send verification email

     Send an email with a verification link to a user that has an email matching the one in the request
    body. This endpoint will return success even if the email does not match any users on the system.
    ##### Permissions
    No permissions required.

    Args:
        json_body (SendVerificationEmailJsonBody):

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
    json_body: SendVerificationEmailJsonBody,
) -> Optional[Union[Any, StatusOK]]:
    """Send verification email

     Send an email with a verification link to a user that has an email matching the one in the request
    body. This endpoint will return success even if the email does not match any users on the system.
    ##### Permissions
    No permissions required.

    Args:
        json_body (SendVerificationEmailJsonBody):

    Returns:
        Response[Union[Any, StatusOK]]
    """

    return (
        await asyncio_detailed(
            client=client,
            json_body=json_body,
        )
    ).parsed
