from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.patch_role_json_body import PatchRoleJsonBody
from ...models.role import Role
from ...types import Response


def _get_kwargs(
    role_id: str,
    *,
    client: Client,
    json_body: PatchRoleJsonBody,
) -> Dict[str, Any]:
    url = "{}/roles/{role_id}/patch".format(client.base_url, role_id=role_id)

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


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Role]]:
    if response.status_code == 200:
        response_200 = Role.from_dict(response.json())

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
    if response.status_code == 404:
        response_404 = cast(Any, None)
        return response_404
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Role]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    role_id: str,
    *,
    client: Client,
    json_body: PatchRoleJsonBody,
) -> Response[Union[Any, Role]]:
    """Patch a role

     Partially update a role by providing only the fields you want to update. Omitted fields will not be
    updated. The fields that can be updated are defined in the request body, all other provided fields
    will be ignored.

    ##### Permissions
    `manage_system` permission is required.

    __Minimum server version__: 4.9

    Args:
        role_id (str):
        json_body (PatchRoleJsonBody):

    Returns:
        Response[Union[Any, Role]]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
        json_body=json_body,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    role_id: str,
    *,
    client: Client,
    json_body: PatchRoleJsonBody,
) -> Optional[Union[Any, Role]]:
    """Patch a role

     Partially update a role by providing only the fields you want to update. Omitted fields will not be
    updated. The fields that can be updated are defined in the request body, all other provided fields
    will be ignored.

    ##### Permissions
    `manage_system` permission is required.

    __Minimum server version__: 4.9

    Args:
        role_id (str):
        json_body (PatchRoleJsonBody):

    Returns:
        Response[Union[Any, Role]]
    """

    return sync_detailed(
        role_id=role_id,
        client=client,
        json_body=json_body,
    ).parsed


async def asyncio_detailed(
    role_id: str,
    *,
    client: Client,
    json_body: PatchRoleJsonBody,
) -> Response[Union[Any, Role]]:
    """Patch a role

     Partially update a role by providing only the fields you want to update. Omitted fields will not be
    updated. The fields that can be updated are defined in the request body, all other provided fields
    will be ignored.

    ##### Permissions
    `manage_system` permission is required.

    __Minimum server version__: 4.9

    Args:
        role_id (str):
        json_body (PatchRoleJsonBody):

    Returns:
        Response[Union[Any, Role]]
    """

    kwargs = _get_kwargs(
        role_id=role_id,
        client=client,
        json_body=json_body,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    role_id: str,
    *,
    client: Client,
    json_body: PatchRoleJsonBody,
) -> Optional[Union[Any, Role]]:
    """Patch a role

     Partially update a role by providing only the fields you want to update. Omitted fields will not be
    updated. The fields that can be updated are defined in the request body, all other provided fields
    will be ignored.

    ##### Permissions
    `manage_system` permission is required.

    __Minimum server version__: 4.9

    Args:
        role_id (str):
        json_body (PatchRoleJsonBody):

    Returns:
        Response[Union[Any, Role]]
    """

    return (
        await asyncio_detailed(
            role_id=role_id,
            client=client,
            json_body=json_body,
        )
    ).parsed
