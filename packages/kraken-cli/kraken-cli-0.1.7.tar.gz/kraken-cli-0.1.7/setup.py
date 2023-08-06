# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['cli', 'cli.locking']

package_data = \
{'': ['*']}

install_requires = \
['kraken-core>=0.2.15,<0.3.0',
 'nr-python-environment>=0.1.2,<0.2.0',
 'packaging>=20.0',
 'setuptools>=33.0.0',
 'slap.core.cli>=0.3.1,<0.4.0',
 'termcolor>=1.1.0,<2.0.0',
 'types-termcolor>=1.1.5,<2.0.0']

entry_points = \
{'console_scripts': ['kraken = kraken.cli.__main__:_entrypoint']}

setup_kwargs = {
    'name': 'kraken-cli',
    'version': '0.1.7',
    'description': '',
    'long_description': '# kraken-cli\n\n[![Python application](https://github.com/kraken-build/kraken-cli/actions/workflows/python-package.yml/badge.svg)](https://github.com/kraken-build/kraken-cli/actions/workflows/python-package.yml)\n[![PyPI version](https://badge.fury.io/py/kraken-cli.svg)](https://badge.fury.io/py/kraken-cli)\n\nThe command-line interface to the Kraken CLI.\n\nUnless you set the environment variable `KRAKEN_MANAGED=0`, the CLI will always bootstrap a new Python virtual\nenvironment for you that contains exactly the build requirements set forth in your project requirements. These\nrequirements can be specified either in a spearate file (`.kraken/requirements.txt`) or in the build script directly.\n\n```py\n# ::requirements PyYAML kraken-std\n# ::requirements --extra-index-url https://test.pypi.org/simple\n#\n# This is a Kraken build script\n\nfrom kraken.std.docker import build_docker_image\nbuild_docker_image()\n```\n\nFor package indices that require authentication, the typical way to configure credentials of additional indexes in\nPip should be used (it is recommended to use `~/.netrc` if possible).\n\n## Development\n\nWhen developing this package locally, it may be desirable to have the current version being developed installed\ninto the virtual environment. For this purpose, you can set the `KRAKEN_DEVELOP=1` variable, which will change\nthe implied dependency from `kraken-cli` to the directory that contains the `kraken.cli` module.\n\n> Note: Currently, the source directory of the kraken-cli project is derived by following the symlink of the\n> `kraken/cli/__init__.py` file and then looking four directories up (cli, kraken, src, kraken-cli project root).\n> This assumption is made based on how symlink installs work with `slap link` or `slap install --link`.\n',
    'author': 'Niklas Rosenstein',
    'author_email': 'rosensteinniklas@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
