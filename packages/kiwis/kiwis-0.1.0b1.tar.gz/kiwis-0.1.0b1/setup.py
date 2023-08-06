# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['kiwis']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'Markdown>=3.3.7,<4.0.0',
 'pymdown-extensions>=9.5,<10.0',
 'python-frontmatter>=1.0.0,<2.0.0',
 'rich-click>=1.5.1,<2.0.0',
 'rich>=12.5.1,<13.0.0',
 'toml>=0.10.2,<0.11.0',
 'watchdog>=2.1.9,<3.0.0']

entry_points = \
{'console_scripts': ['kiwis = kiwis.__main__:cli']}

setup_kwargs = {
    'name': 'kiwis',
    'version': '0.1.0b1',
    'description': 'A simple yet powerful static site generator',
    'long_description': '',
    'author': 'wxllow',
    'author_email': 'willow@wxllow.dev',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/wxllow/kiwis',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)
