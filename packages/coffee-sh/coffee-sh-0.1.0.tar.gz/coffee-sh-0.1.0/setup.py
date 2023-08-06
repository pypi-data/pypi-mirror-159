# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['coffee_sh']

package_data = \
{'': ['*']}

install_requires = \
['tinydb>=4.7.0,<5.0.0', 'typer[all]>=0.6.1,<0.7.0']

entry_points = \
{'console_scripts': ['coffee = coffee_sh.main:app']}

setup_kwargs = {
    'name': 'coffee-sh',
    'version': '0.1.0',
    'description': 'Coffee is a command-line utility for developers who want their task list at termial',
    'long_description': '# Coffee.sh\n\nCoffee is a command-line utility for developers who want their task list at terminal\n\n## Installation\n\n```bash\npip install coffee-sh\n```\n\n## Usage\n\nTo add a new task\n\n```bash\ncoffee add "Drink Water"\n```\n\nTo Update task\n\n```bash\ncoffee update 1 --task "Drink More Water"\n```\n\n> Here 1 is task ID which is unique\n\nTo Delete task\n\n```bash\ncoffee drop 1\n```\n\n> Here 1 is task ID which is unique\n\nTo show all tasks\n\n```\ncoffee tasks\n```\n\nTo remove all tasks\n```bash\ncoffee erase\n```\n',
    'author': 'Aadityansha',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
