# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['pellet']

package_data = \
{'': ['*']}

install_requires = \
['rich==12.5.1']

setup_kwargs = {
    'name': 'pellet',
    'version': '0.1.3',
    'description': 'Pellet helps improve your Django app performance by discovering N+1 queries',
    'long_description': '# Pellet\n\nPellet helps improve your Django app performance by discovering `N+1` queries.\n\nThe Django ORM makes it easy to forget using `select_related` and `prefetch_related` correctly and can accidentally cause `N+1` queries to happen.\n\nPellet ultimately aims to recreate [Bullet](https://github.com/flyerhzm/bullet) for Django.\n\n## Installing Pellet\n\n`pip install pellet`\n\n## Enabling Pellet\n\n1. Add `pellet.middleware.PelletMiddleware` to your django middleware list.\n2. Configure pellet behaviour by using the `PELLET` variable in your django settings file.\n\n## Configuring Pellet\n\nYou can configure pellet by setting the `PELLET` variable in your django settings file. The default values used by pellet if this variable or any field in the object is not found is as follows:\n\n```python3\nPELLET = {\n    # Enable/Disable pellet\n    # If set to False the pellet\n    # middleware does nothing\n    "enabled": False,\n\n    # Enable this if you want count and time\n    # metrics at a query level\n    "query_level_metrics_enabled": False,\n\n    # Settings related to response headers\n    # set by pellet\n    "headers": {\n\n        # Enables setting response headers\n        "enabled": False,\n\n        # Header to be used for setting total query count\n        "query_count_header": "X-Pellet-Count",\n\n        # Header to be used for setting total query time\n        "query_time_header": "X-Pellet-Time"\n    },\n\n    # Settings related to pellet debug mode\n    "debug": {\n\n        # Enable debug mode\n        # Don\'t enable on prod as it will slow down your app\n        "enabled": False,\n\n        # Query count thresholds which will\n        # be used by pellet to report metrics\n        # on the console\n        "count_threshold": {\n\n            # Min number of times a query should happen\n            # for it to be classified as N+1\n            # Queries with less count than this will\n            # not show up in the debug table\n            "min": 2,\n\n            # Max number of times a query should happen\n            # for it to be classified as a low impact\n            # performance issue\n            "low": 5,\n\n            # Max number of times a query should happen\n            # for it to be classified as a warning impact\n            # performance issue\n            # Every query happening more times than this\n            # is classified as a high impact performance issue\n            "medium": 10\n        }\n    },\n\n    # Path to a callback function which will be called\n    # with the request, response and\n    # pellet metrics object\n    "callback": None\n}\n```\n\n## Callback function\n\nThe callback function should accept three arguments:\n1. `request` -> django request object\n2. `response` -> django response object\n3. `pellet_metrics` -> dict containing metrics collected by pellet\n\nExample functionality:\n1. collect and send api call level pellet metrics to an external service like datadog\n2. make integration tests fail for an api if too many queries are happening by raising an exception\n3. send alert emails, slack messages, etc on too many queries\n\n### Steps:\n\n1. Create a callback function:\n```python3\n# app/user/callbacks.py\n\nfrom pellet.utils import get_sanitised_path\n\ndef write_datadog_metrics(path, metrics):\n    # Writes metrics to datadog\n    pass\n\ndef pellet_callback(request, response, pellet_metrics):\n    # Get id stripped path\n    # eg: /api/user/1/ -> /api/user/_id_/\n    sanitised_path = get_sanitised_path(request.path)\n    write_datadog_metrics(sanitised_path, pellet_metrics)\n```\n\n2. Specify the callback function in the pellet config object.\n```python\nPELLET = {\n    # ..... rest of pellet config\n    "callback": "app.user.callbacks.pellet_callback"\n}\n```\n',
    'author': 'Harikrishnan Shaji',
    'author_email': 'hihari777@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/har777/pellet',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
