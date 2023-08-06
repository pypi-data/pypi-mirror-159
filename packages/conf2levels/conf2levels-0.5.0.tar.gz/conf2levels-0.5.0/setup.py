# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['conf2levels']

package_data = \
{'': ['*']}

install_requires = \
['typing-extensions>=4.3.0,<5.0.0']

setup_kwargs = {
    'name': 'conf2levels',
    'version': '0.5.0',
    'description': 'A configuration reader which reads values stored in two key levels. The first key level is named “section” and the second level “key”.',
    'long_description': "A configuration reader which reads values stored in two key levels.\nThe first key level is named ``section`` and the second level ``key``.\n\nargparse arguments (`argparse`): (You have to specify a mapping)\n\n.. code:: python\n\n    mapping = {\n        'section.key': 'args_attribute'\n    }\n\nA python dictionary (`dictonary`):\n\n.. code:: python\n\n    {\n        'section':  {\n            'key': 'value'\n        }\n    }\n\nEnvironment variables (`environ`):\n\n.. code:: shell\n\n    export prefix__section__key=value\n\nINI file (`ini`):\n\n.. code:: ini\n\n    [section]\n    key = value\n\n\n.. code:: python\n\n    CONF_DEFAULTS = {\n        'email': {\n            'subject_prefix': 'command_watcher',\n        },\n        'nsca': {\n            'port': 5667,\n        },\n    }\n\n    CONFIG_READER_SPEC: Spec = {\n        'email': {\n            'from_addr': {\n                'description': 'The email address of the sender.',\n            },\n            'to_addr': {\n                'description': 'The email address of the recipient.',\n                'not_empty': True,\n            },\n            'to_addr_critical': {\n                'description': 'The email address of the recipient to send '\n                              'critical messages to.',\n                'default': None,\n            },\n            'smtp_login': {\n                'description': 'The SMTP login name.',\n                'not_empty': True,\n            },\n            'smtp_password': {\n                'description': 'The SMTP password.',\n                'not_empty': True,\n            },\n            'smtp_server': {\n                'description': 'The URL of the SMTP server, for example: '\n                              '`smtp.example.com:587`.',\n                'not_empty': True,\n            },\n        },\n        'icinga': {\n            'url': {\n                'description': 'The HTTP URL. /v1/actions/process-check-result '\n                              'is appended.',\n                'not_empty': True,\n            },\n            'user': {\n                'description': 'The user for the HTTP authentification.',\n                'not_empty': True,\n            },\n            'password': {\n                'description': 'The password for the HTTP authentification.',\n                'not_empty': True,\n            },\n        },\n        'beep': {\n            'activated': {\n                'description': 'Activate the beep channel to report auditive '\n                              'messages.',\n                'default': False,\n            }\n        }\n    }\n\n    config_reader = ConfigReader(\n        spec=CONFIG_READER_SPEC,\n        ini=config_file,\n        dictionary=CONF_DEFAULTS,\n    )\n",
    'author': 'Josef Friedrich',
    'author_email': 'josef@friedrich.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
