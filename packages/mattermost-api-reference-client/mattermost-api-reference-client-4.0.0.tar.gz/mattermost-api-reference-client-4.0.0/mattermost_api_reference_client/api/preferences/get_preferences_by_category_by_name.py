from typing import Any, Dict, Optional, Union, cast

import httpx

from ...client import Client
from ...models.preference import Preference
from ...types import Response


def _get_kwargs(
    user_id: str,
    category: str,
    preference_name: str,
    *,
    client: Client,
) -> Dict[str, Any]:
    url = "{}/users/{user_id}/preferences/{category}/name/{preference_name}".format(
        client.base_url, user_id=user_id, category=category, preference_name=preference_name
    )

    headers: Dict[str, str] = client.get_headers()
    cookies: Dict[str, Any] = client.get_cookies()

    return {
        "method": "get",
        "url": url,
        "headers": headers,
        "cookies": cookies,
        "timeout": client.get_timeout(),
    }


def _parse_response(*, response: httpx.Response) -> Optional[Union[Any, Preference]]:
    if response.status_code == 200:
        response_200 = Preference.from_dict(response.json())

        return response_200
    if response.status_code == 400:
        response_400 = cast(Any, None)
        return response_400
    if response.status_code == 401:
        response_401 = cast(Any, None)
        return response_401
    return None


def _build_response(*, response: httpx.Response) -> Response[Union[Any, Preference]]:
    return Response(
        status_code=response.status_code,
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(response=response),
    )


def sync_detailed(
    user_id: str,
    category: str,
    preference_name: str,
    *,
    client: Client,
) -> Response[Union[Any, Preference]]:
    """Get a specific user preference

     Gets a single preference for the current user with the given category and name.
    ##### Permissions
    Must be logged in as the user being updated or have the `edit_other_users` permission.

    Args:
        user_id (str):
        category (str):
        preference_name (str):

    Returns:
        Response[Union[Any, Preference]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        category=category,
        preference_name=preference_name,
        client=client,
    )

    response = httpx.request(
        verify=client.verify_ssl,
        **kwargs,
    )

    return _build_response(response=response)


def sync(
    user_id: str,
    category: str,
    preference_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, Preference]]:
    """Get a specific user preference

     Gets a single preference for the current user with the given category and name.
    ##### Permissions
    Must be logged in as the user being updated or have the `edit_other_users` permission.

    Args:
        user_id (str):
        category (str):
        preference_name (str):

    Returns:
        Response[Union[Any, Preference]]
    """

    return sync_detailed(
        user_id=user_id,
        category=category,
        preference_name=preference_name,
        client=client,
    ).parsed


async def asyncio_detailed(
    user_id: str,
    category: str,
    preference_name: str,
    *,
    client: Client,
) -> Response[Union[Any, Preference]]:
    """Get a specific user preference

     Gets a single preference for the current user with the given category and name.
    ##### Permissions
    Must be logged in as the user being updated or have the `edit_other_users` permission.

    Args:
        user_id (str):
        category (str):
        preference_name (str):

    Returns:
        Response[Union[Any, Preference]]
    """

    kwargs = _get_kwargs(
        user_id=user_id,
        category=category,
        preference_name=preference_name,
        client=client,
    )

    async with httpx.AsyncClient(verify=client.verify_ssl) as _client:
        response = await _client.request(**kwargs)

    return _build_response(response=response)


async def asyncio(
    user_id: str,
    category: str,
    preference_name: str,
    *,
    client: Client,
) -> Optional[Union[Any, Preference]]:
    """Get a specific user preference

     Gets a single preference for the current user with the given category and name.
    ##### Permissions
    Must be logged in as the user being updated or have the `edit_other_users` permission.

    Args:
        user_id (str):
        category (str):
        preference_name (str):

    Returns:
        Response[Union[Any, Preference]]
    """

    return (
        await asyncio_detailed(
            user_id=user_id,
            category=category,
            preference_name=preference_name,
            client=client,
        )
    ).parsed
