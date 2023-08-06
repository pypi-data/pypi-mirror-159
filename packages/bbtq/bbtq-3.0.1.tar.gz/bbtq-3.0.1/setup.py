# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bbtq', 'bbtq.tests']

package_data = \
{'': ['*']}

install_requires = \
['toml>=0.10.0,<0.11.0']

entry_points = \
{'console_scripts': ['tq = bbtq.cli:main']}

setup_kwargs = {
    'name': 'bbtq',
    'version': '3.0.1',
    'description': 'Barebones TOML query.',
    'long_description': '# bbtq\n\nBarebones TOML query. Like jq, but for TOML instead of JSON.\n\n<a href="https://pypi.org/project/bbtq/"><img alt="PyPI" src="https://img.shields.io/pypi/v/bbtq"></a>\n[![Test Status](https://github.com/aerickson/bbtq/actions/workflows/test.yml/badge.svg)](https://github.com/aerickson/bbtq/actions/workflows/test.yml)\n[![Code Coverage](https://codecov.io/gh/aerickson/bbtq/branch/master/graph/badge.svg?token=y0FQaJuAJu)](https://codecov.io/gh/aerickson/bbtq)\n\n## installation\n\n```bash\n# via pypi\npip3 install bbtq\n\n# directly from repo\npip3 install git+https://github.com/aerickson/bbtq.git@master\n```\n\n## usage\n\n```bash\n# a search of \'.\' shows the entire document\n$ tq bbtq/tests/test.toml .\ntitle = "TOML Example"\n\n[owner]\nname = "Tom Preston-Werner"\ndob = 1979-05-27T07:32:00-08:00\n\n[database]\nserver = "192.168.1.1"\nports = [ 8001, 8001, 8002,]\nconnection_max = 5000\nenabled = true\n\n# retrieve items\n$ tq bbtq/tests/test.toml .title\nTOML Example\n$ tq bbtq/tests/test.toml .database.ports\n[8001, 8001, 8002]\n\n# retreive an array element\n$ tq bbtq/tests/test.toml ".database.ports[2]"\n8002\n\n# can also be used via pipe\n$ cat bbtq/tests/test.toml | ./bin/tq - .\n```\n\n## known limitations\n\n- supports a subset of yq filter syntax\n  - https://mikefarah.gitbook.io/yq/usage/path-expressions\n  - doesn\'t support pipe operator\n\n## why\n\n- I couldn\'t get yq\'s experimental support for TOML working.\n- I wanted a python implementation, all others seem to use go.\n\n## links\n\n- jq: https://github.com/stedolan/jq\n- yq: https://github.com/kislyuk/yq\n',
    'author': 'Andrew Erickson',
    'author_email': 'aerickson@gmail.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
