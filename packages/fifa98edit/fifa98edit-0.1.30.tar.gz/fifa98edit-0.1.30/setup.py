# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['fifa98edit']

package_data = \
{'': ['*'], 'fifa98edit': ['FifaStyles/*']}

install_requires = \
['colorama>=0.4.4,<0.5.0',
 'numpy>=1.19.0,<2.0.0',
 'pandas>=1.0.5,<2.0.0',
 'pillow>=7.2.0,<8.0.0',
 'unidecode>=1.3.2,<2.0.0']

extras_require = \
{':sys_platform == "win32"': ['pypiwin32>=223,<224']}

setup_kwargs = {
    'name': 'fifa98edit',
    'version': '0.1.30',
    'description': 'A command-line database editor for FIFA RTWC 98.',
    'long_description': '# fifa98edit\nA Python 3 editor for the old EA Sports PC game Fifa RTWC 98.\nRun fifa98edit.py. Help and instructions are provided in the editor.\n\n## Installation\n\nInstall Python 3.8 or higher and run:\n\n    pip install fifa98edit\n\nIf your system runs multiple versions of Python (e.g. Python 2 on many Macs) run:\n\n    pip3 install fifa98edit\n\nIf you wish to update to a new version, run:\n\n\n    pip3 install --upgrade fifa98edit\n\n\n## Use\n\n    python -m fifa98edit\nor\n    \n    python3 -m fifa98edit \nif running multiple versions of Python\n\nFurther help is provided in the application.\n\n## Uninstall\n\n    pip uninstall fifa98edit\nor\n    \n    pip3 uninstall fifa98edit\nif running multiple versions of Python\n\nThe command will produce a list of files that "Would not remove". Remove those files manually following the path provided.\n\n## Dependencies\n\nThe ability to add national teams or to move club teams to national team groups (for example, to create tournaments) depends on the ability to write compressed graphic files containing the flags. This is provided by [RefPack Tool by **KUDr**](https://github.com/MicaelJarniac/RefPack-Tool/tree/master/bin), which runs under Windows. Donwload the executables and follow the instructions in the editor.\n',
    'author': 'Megas Alexandros',
    'author_email': 'megas_alexandros@hotmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ma-akad/fifa98edit',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'extras_require': extras_require,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
