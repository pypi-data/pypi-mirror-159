# -*- coding: utf-8 -*-
from setuptools import setup

modules = \
['mathhew']
install_requires = \
['click>=8.1.3,<9.0.0']

entry_points = \
{'console_scripts': ['matthew = mathhew:main']}

setup_kwargs = {
    'name': 'mathhew',
    'version': '0.1.1',
    'description': 'Fast and Simple Math Interpreter',
    'long_description': None,
    'author': 'micziz',
    'author_email': 'miczicontent@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'py_modules': modules,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
