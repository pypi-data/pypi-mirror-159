# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['asc2mb']

package_data = \
{'': ['*']}

install_requires = \
['click==8.0', 'lxml>=4.9.1,<5.0.0']

entry_points = \
{'console_scripts': ['asc2mb = asc2mb.asc2mb:main']}

setup_kwargs = {
    'name': 'asc2mb',
    'version': '0.6.2',
    'description': 'Manage your timetable by pasing the XML export from asc and format into two files suitable for upload into ManageBac',
    'long_description': '# aSc to ManageBac\n\n## Getting started\n\nRequires Python 3.6 or above. For Windows, install Python via the Microsoft Store. For Mac, install Python at [python.org](https://www.python.org). Installing Python also installs a package manager (called `pip`) that can install the command `asc2mb` into your command line environment.\n\nAfter installing Python, open the terminal or command line or PowerShell, and peform the following:\n\n```sh\npip install asc2mb\n```\n\nIf for some reason the `pip` command doesn\'t work, you can manually install it by following [the relevant instructions](https://pip.pypa.io/en/stable/installing/) for your system.\n\n### Upgrade\n\nShould you need to update to the latest version, you can do:\n\n```\npip install --upgrade asc2mb\n```\n\n## Use\n\nAfter `pip install` worked, it is now installed on your path, and the command `asc2mb` should be available:\n\n```\nasc2mb ~/path/to/xml.xml ~/path/to/save/timetable.csv ~/path/to/save/classes.csv\n```\n\nIt takes only a second to run. It reports how many records it processed.\n\n## Algorithm\n\nThis script uses input from more than one international school to generate the expected output. The key to success is using aSc Divisions to match the `uniq_id`s found in ManageBac classes.\n\n## Help\n\nFor built-in help, and list of options and their functionality:\n\n```\nasc2mb --help\n```\n\n## Miscellaneous\n\nThe command takes three required arguments, and there are additional options as well. The three required arguments tell the program where the xml file is located, and where to save the two csv files. \n\nThe options depend on your school\'s needs. For example, the class id is how ManageBac knows which class you are referring to, so that program helps you derive the class ID based on information contains in the xml file. It\'s up to you to ensure there are classes that have those IDs in ManageBac, but the program does produce a csv so that they can be uploaded in bulk.\n\nBy default, class id uses the pattern `{class_.short}_{division.name}`, which means "the short name of the class" plus an underscore, plus the name of the division." At the time of publication, having a different pattern is only possible by contacting the author (or, if you\'re a keen developer, add a pull request).\n\nIf you run the program without any options, it\'ll prompt you to enter them.\n\n\n\n\n\n\n\n',
    'author': 'Adam Morris',
    'author_email': 'adam.morris@fariaedu.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.6,<4.0',
}


setup(**setup_kwargs)
