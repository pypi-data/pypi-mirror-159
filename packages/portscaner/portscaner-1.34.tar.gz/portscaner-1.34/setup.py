# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['portscaner']
setup_kwargs = {
    'name': 'portscaner',
    'version': '1.34',
    'description': 'Simple port scanner with progress bar',
    'long_description': None,
    'author': 'AllewKley',
    'author_email': '100071713+AllewKley@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'python_requires': '>=3.5,<4.0',
}


setup(**setup_kwargs)
