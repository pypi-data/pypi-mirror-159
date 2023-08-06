# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['mattermost_api_reference_client',
 'mattermost_api_reference_client.api',
 'mattermost_api_reference_client.api.bleve',
 'mattermost_api_reference_client.api.bots',
 'mattermost_api_reference_client.api.brand',
 'mattermost_api_reference_client.api.channels',
 'mattermost_api_reference_client.api.cloud',
 'mattermost_api_reference_client.api.cluster',
 'mattermost_api_reference_client.api.commands',
 'mattermost_api_reference_client.api.compliance',
 'mattermost_api_reference_client.api.data_retention',
 'mattermost_api_reference_client.api.elasticsearch',
 'mattermost_api_reference_client.api.emoji',
 'mattermost_api_reference_client.api.exports',
 'mattermost_api_reference_client.api.files',
 'mattermost_api_reference_client.api.groups',
 'mattermost_api_reference_client.api.imports',
 'mattermost_api_reference_client.api.insights',
 'mattermost_api_reference_client.api.integration_actions',
 'mattermost_api_reference_client.api.jobs',
 'mattermost_api_reference_client.api.ldap',
 'mattermost_api_reference_client.api.o_auth',
 'mattermost_api_reference_client.api.open_graph',
 'mattermost_api_reference_client.api.permissions',
 'mattermost_api_reference_client.api.plugins',
 'mattermost_api_reference_client.api.posts',
 'mattermost_api_reference_client.api.preferences',
 'mattermost_api_reference_client.api.reactions',
 'mattermost_api_reference_client.api.roles',
 'mattermost_api_reference_client.api.root',
 'mattermost_api_reference_client.api.saml',
 'mattermost_api_reference_client.api.schemes',
 'mattermost_api_reference_client.api.shared_channels',
 'mattermost_api_reference_client.api.status',
 'mattermost_api_reference_client.api.system',
 'mattermost_api_reference_client.api.teams',
 'mattermost_api_reference_client.api.terms_of_service',
 'mattermost_api_reference_client.api.threads',
 'mattermost_api_reference_client.api.uploads',
 'mattermost_api_reference_client.api.usage',
 'mattermost_api_reference_client.api.users',
 'mattermost_api_reference_client.api.webhooks',
 'mattermost_api_reference_client.models']

package_data = \
{'': ['*']}

install_requires = \
['attrs>=21.3.0', 'httpx>=0.15.4,<0.24.0', 'python-dateutil>=2.8.0,<3.0.0']

setup_kwargs = {
    'name': 'mattermost-api-reference-client',
    'version': '4.0.0',
    'description': 'A client library for accessing Mattermost API Reference',
    'long_description': '# mattermost-api-reference-client\nA client library for accessing Mattermost API Reference\n\n[![pypi](https://badge.fury.io/py/mattermost-api-reference-client.svg)](https://pypi.org/project/mattermost-api-reference-client/)\n[![builds.sr.ht status](https://builds.sr.ht/~nicoco/mattermost-api-reference-client/commits/master/.build.yml.svg)](https://builds.sr.ht/~nicoco/mattermost-api-reference-client/commits/master/.build.yml?)\n\nGenerated using the awesome [openapi-python-client](https://pypi.org/project/openapi-python-client/) using\nthe schema provided on the [mattermost api docs](https://api.mattermost.com).\n\nShould provide correct signatures for endpoint calls and correct type hinting for all response models.\nAuto-completion works like a charm in pycharm (pun intended), and probably other editors.\n\n## Usage\nFirst, create a client:\n\n```python\nfrom mattermost_api_reference_client import Client\n\nclient = Client(base_url="https://mattermost.example.com/api/v4")\n```\n\nIf the endpoints you\'re going to hit require authentication, use `AuthenticatedClient` instead.\nGet your token either by using the `users.login` endpoint or by grabbing the `MMAUTHTOKEN` from\na web session, using the "storage" tab of developer console to inspect cookies.\n\n```python\nfrom mattermost_api_reference_client import AuthenticatedClient\n\nclient = AuthenticatedClient(base_url="https://mattermost.example.com/api/v4", token="MMAUTHTOKEN_VALUE")\n```\n\nNow call your endpoint and use your models:\n\n```python\nfrom mattermost_api_reference_client.models import User\nfrom mattermost_api_reference_client.api.users import get_user\nfrom mattermost_api_reference_client.types import Response\n\nmy_data: User = get_user.sync("me", client=client)\n# or if you need more info (e.g. status_code)\nresponse: Response[User] = get_user.sync_detailed("me", client=client)\n```\n\nOr do the same thing with an async version:\n\n```python\nmy_data: User = await get_user.asyncio(client=client)\nresponse: Response[User] = await get_user.asyncio_detailed(client=client)\n```\n\nBy default, when you\'re calling an HTTPS API it will attempt to verify that SSL is working correctly. Using certificate verification is highly recommended most of the time, but sometimes you may need to authenticate to a server (especially an internal server) using a custom certificate bundle.\n\n```python\nclient = AuthenticatedClient(\n    base_url="https://internal_api.example.com", \n    token="MMAUTHTOKEN_VALUE",\n    verify_ssl="/path/to/certificate_bundle.pem",\n)\n```\n\nYou can also disable certificate validation altogether, but beware that **this is a security risk**.\n\n```python\nclient = AuthenticatedClient(\n    base_url="https://internal_api.example.com", \n    token="MMAUTHTOKEN_VALUE", \n    verify_ssl=False\n)\n```\n\nThings to know:\n1. Every path/method combo becomes a Python module with four functions:\n    1. `sync`: Blocking request that returns parsed data (if successful) or `None`\n    1. `sync_detailed`: Blocking request that always returns a `Request`, optionally with `parsed` set if the request was successful.\n    1. `asyncio`: Like `sync` but async instead of blocking\n    1. `asyncio_detailed`: Like `sync_detailed` but async instead of blocking\n\n1. All path/query params, and bodies become method arguments.\n1. If your endpoint had any tags on it, the first tag will be used as a module name for the function (my_tag above)\n1. Any endpoint which did not have a tag will be in `mattermost_api_reference_client.api.default`\n\n## Similar to\n\n- https://github.com/Vaelor/python-mattermost-driver\n- https://pypi.org/project/mattermost/\n',
    'author': 'Nicolas Cedilnik',
    'author_email': 'nicoco@nicoco.fr',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://git.sr.ht/~nicoco/mattermost-api-reference-client/',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
