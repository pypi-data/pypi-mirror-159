# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['licensegh']

package_data = \
{'': ['*']}

install_requires = \
['GitPython>=3.1.23,<4.0.0',
 'PyYAML>=5.4.1,<6.0.0',
 'click>=8.0.1,<9.0.0',
 'rich>=12.4.4,<13.0.0']

entry_points = \
{'console_scripts': ['licensegh = licensegh.cli:main']}

setup_kwargs = {
    'name': 'licensegh',
    'version': '1.0.1',
    'description': 'licensegh is a command line tool that generates a license file for a project from the github open source lincese templates',
    'long_description': '# licensegh\n\n<a href="https://www.python.org/"><img alt="Python" src="https://img.shields.io/badge/-python-success?logo=python&logoColor=white"></a>\n<a href="https://github.com/sauljabin/licensegh"><img alt="GitHub" src="https://img.shields.io/badge/status-active-brightgreen"></a>\n<a href="https://github.com/sauljabin/licensegh/blob/main/LICENSE"><img alt="MIT License" src="https://img.shields.io/github/license/sauljabin/licensegh"></a>\n<a href="https://github.com/sauljabin/licensegh/actions"><img alt="GitHub Actions" src="https://img.shields.io/github/workflow/status/sauljabin/licensegh/CI?label=tests"></a>\n<a href="https://app.codecov.io/gh/sauljabin/licensegh"><img alt="Codecov" src="https://img.shields.io/codecov/c/github/sauljabin/licensegh"></a>\n<a href="https://pypi.org/project/licensegh"><img alt="Python Versions" src="https://img.shields.io/pypi/pyversions/licensegh"></a>\n<a href="https://pypi.org/project/licensegh"><img alt="Version" src="https://img.shields.io/pypi/v/licensegh"></a>\n<a href="https://libraries.io/pypi/licensegh"><img alt="Dependencies" src="https://img.shields.io/librariesio/release/pypi/licensegh"></a>\n<a href="https://pypi.org/project/licensegh"><img alt="Platform" src="https://img.shields.io/badge/platform-linux%20%7C%20osx-blueviolet"></a>\n\n`licensegh` is a command line tool that generates a `LICENSE` file for a project from the [github license templates repository](https://github.com/github/choosealicense.com/tree/gh-pages/_licenses).\n\n![https://raw.githubusercontent.com/sauljabin/licensegh/main/screenshots/options.png](https://raw.githubusercontent.com/sauljabin/licensegh/main/screenshots/options.png)\n\n## Installation\n\nInstall with pip:\n```sh\npip install licensegh\n```\n\nUpgrade with pip:\n```sh\npip install --upgrade licensegh\n```\n\n## Usage\n\nHelp:\n```sh\nlicensegh -h\n```\n\nVersion:\n```sh\nlicensegh --version\n```\n\nList all licenses:\n```sh\nlicensegh -l\n```\n\nSearch licenses:\n```sh\nlicensegh -s\n```\n\nPrint a license: \n```sh\nlicensegh -p\n```\n\nReset github template repository:\n```sh\nlicensegh --reset\n```\n\nSave a license:\n```sh\nlicensegh mit\n```\n\n## Development\n\nInstalling poetry:\n```sh\npip install poetry\n```\n\nInstalling development dependencies:\n```sh\npoetry install\n```\n\nRunning unit tests:\n```sh\npoetry run python -m scripts.tests\n```\n\nApplying code styles:\n```sh\npoetry run python -m scripts.styles\n```\n\nRunning code analysis:\n```sh\npoetry run python -m scripts.analyze\n```\n\nRunning code coverage:\n```sh\npoetry run python -m scripts.tests-coverage\n```\n\nRunning cli using `poetry`:\n```sh\npoetry run licensegh\n```\n',
    'author': 'Saúl Piña',
    'author_email': 'sauljabin@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/sauljabin/licensegh',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
