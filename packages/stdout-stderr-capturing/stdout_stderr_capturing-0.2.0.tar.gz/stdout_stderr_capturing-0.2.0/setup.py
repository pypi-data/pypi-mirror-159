# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['stdout_stderr_capturing']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'stdout-stderr-capturing',
    'version': '0.2.0',
    'description': 'Capture the stdout or stderr output as a list in a context manager block (with).',
    'long_description': "stdout_stderr_capturing\n=======================\n\nCapture the stdout or stderr output as a list in a context manager block (with).\n\nMaybe better alternatives:\n\n* `capturer <https://pypi.org/project/capturer>`_ https://github.com/xolox/python-capturer\n* `stdio-mgr <https://pypi.org/project/stdio-mgr>`_\n* `OutputCatcher <https://pypi.org/project/OutputCatcher>`_\n* `wurlitzer <https://pypi.org/project/wurlitzer>`_\n\nCapture stdout:\n\n.. code:: python\n\n    with Capturing() as output:\n        print('line 1')\n\n    print(output[0])\n\nis equivalent to\n\n.. code:: python\n\n    with Capturing(stream='stdout') as output:\n        print('line 1')\n\nCapture stderr:\n\n.. code:: python\n\n    with Capturing(stream='stderr') as output:\n        print('line 1', file=sys.stderr)\n",
    'author': 'Josef Friedrich',
    'author_email': 'josef@friedrich.rocks',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/Josef-Friedrich/stdout_stderr_capturing',
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
