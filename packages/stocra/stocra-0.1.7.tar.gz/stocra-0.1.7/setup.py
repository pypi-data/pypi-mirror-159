# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stocra', 'stocra.asynchronous', 'stocra.synchronous']

package_data = \
{'': ['*']}

install_requires = \
['pydantic']

extras_require = \
{'asynchronous': ['aiohttp'], 'synchronous': ['requests']}

setup_kwargs = {
    'name': 'stocra',
    'version': '0.1.7',
    'description': 'Stocra.com python sdk',
    'long_description': '# Stocra Python SDK\n- [SDK API documentation](https://stocra.github.io/sdk-python/)\n  - [Models](https://stocra.github.io/sdk-python/stocra/models.html)\n  - [Synchronous client](https://stocra.github.io/sdk-python/stocra/synchronous/client.html)\n  - [Asynchronous client](https://stocra.github.io/sdk-python/stocra/asynchronous/client.html)\n- [Using synchronous client](#synchronous-client)\n- [Using asynchronous client](#asynchronous-client)\n- [Error handlers](#error-handlers)\n\n## Synchronous client\n### Install\n```bash\npip install stocra[synchronous]\n# or\npoetry add stocra --extras synchronous\n```\n### Usage\n```python\nfrom concurrent.futures import ThreadPoolExecutor\nfrom decimal import Decimal\n\nfrom requests import Session\nfrom requests.adapters import HTTPAdapter\nfrom stocra.synchronous.client import Stocra\nfrom stocra.synchronous.error_handlers import retry_on_too_many_requests, retry_on_service_unavailable\n\nadapter = HTTPAdapter(pool_connections=100, pool_maxsize=100)\nsession = Session()\nsession.mount(\'https://\', adapter)\nstocra_client = Stocra(\n    api_key="<api-key>", # optional\n    session=session, # optional\n    executor=ThreadPoolExecutor(), # optional\n    error_handlers=[ \n        retry_on_service_unavailable,\n        retry_on_too_many_requests,\n    ] # optional\n)\n\n# stream new blocks\nfor block in stocra_client.stream_new_blocks(blockchain="ethereum"):\n    print(block)\n\n# stream new blocks, load new blocks in the background for faster processing. \n# Works only if executor was provided during instantiation.\nfor block in stocra_client.stream_new_blocks_ahead(blockchain="ethereum"):\n    print(block)\n    \n# stream new transactions\nfor block, transaction in stocra_client.stream_new_transactions(blockchain="ethereum"):\n    print(block.height, transaction.hash)\n    \n# get one block\nblock = stocra_client.get_block(blockchain="bitcoin", hash_or_height=57043)\n\n# get one transaction\ntransaction = stocra_client.get_transaction(\n    blockchain="bitcoin", \n    transaction_hash="a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d"\n)\n\n# get all transactions in block\ntransactions = stocra_client.get_all_transactions_of_block(blockchain="bitcoin", block=block) \nfor transaction in transactions:\n    print(transaction)\n    \n# scale token value\nvalue = stocra_client.scale_token_value(\n    "ethereum", \n    "0xa49ded8b4607f958003e0d87d7f2d2f69bcadd41",  # USDT\n    Decimal("34500000000000000000000000") # raw value in token transfer\n)\n```\n## Asynchronous client\n### Install\n```bash\npip install stocra[asynchronous]\n# or\npoetry add stocra --extras asynchronous\n```\n### Usage\n```python\nfrom asyncio import Semaphore\nfrom decimal import Decimal\n\nfrom aiohttp import ClientSession\nfrom stocra.asynchronous.client import Stocra\nfrom stocra.asynchronous.error_handlers import retry_on_too_many_requests, retry_on_service_unavailable\n\nsession = ClientSession()\nstocra_client = Stocra(\n    api_key="<api-key>", # optional\n    session=session, # optional\n    semaphore=Semaphore(50), # optional\n    error_handlers=[\n        retry_on_service_unavailable,\n        retry_on_too_many_requests,\n    ] # optional\n)\n# stream new transactions\nasync for block, transaction in stocra_client.stream_new_transactions(blockchain="ethereum"):\n    print(block.height, transaction.hash)\n\n# stream new blocks and always load next 5 blocks in the background.\n# useful when you need to parse multiple blocks in short time span\nasync for block in stocra_client.stream_new_blocks(blockchain="ethereum", n_blocks_ahead=5):\n    print(block)\n\n# get one block\nblock = await stocra_client.get_block(\n    blockchain="bitcoin",\n    hash_or_height="00000000152340ca42227603908689183edc47355204e7aca59383b0aaac1fd8"\n)\n\n# get one transaction\ntransaction = await stocra_client.get_transaction(\n    blockchain="bitcoin",\n    transaction_hash="a1075db55d416d3ca199f55b6084e2115b9345e16c5cf302fc80e9d5fbf5d48d", \n)\n\n# get all transactions in block\ntransactions = stocra_client.get_all_transactions_of_block(blockchain="bitcoin", block=block)\nasync for transaction in transactions:\n    print(transaction)\n\n# scale token value\nvalue = await stocra_client.scale_token_value(\n    "ethereum", \n    "0xa49ded8b4607f958003e0d87d7f2d2f69bcadd41",  # USDT\n    Decimal("34500000000000000000000000") # raw value in token transfer\n)\n\n```\n## Error handlers\nError handlers are functions that are called after a request fails. \nThey receive single argument, [StocraHTTPError](https://stocra.github.io/sdk-python/stocra/models.html#StocraHTTPError) \nand return boolean indicating whether to retry request (`True`) or raise (`False`).\n\nError handler signature: `ErrorHandler = Callable[[StocraHTTPError], Union[bool, Awaitable[bool]]]`\n\nNo errors handlers are used by default although there are two already defined for both sync and async version: \n- synchronous error handlers: [stocra.synchronous.error_handlers](https://stocra.github.io/sdk-python/stocra/synchronous/error_handlers.html)\n- of asynchronous error handlers: [stocra.asynchronous.error_handlers](https://stocra.github.io/sdk-python/stocra/asynchronous/error_handlers.html)\n',
    'author': 'Lukáš Vokráčko',
    'author_email': 'lukas@vokracko.cz',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://stocra.com',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
