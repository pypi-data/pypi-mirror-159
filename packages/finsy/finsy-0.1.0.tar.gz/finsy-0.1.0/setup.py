# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['finsy',
 'finsy.proto',
 'finsy.proto.gnmi1',
 'finsy.proto.google.rpc',
 'finsy.proto.google.rpc.context',
 'finsy.proto.p4',
 'finsy.proto.p4.config',
 'finsy.proto.p4.config.v1',
 'finsy.proto.p4.v1',
 'finsy.test']

package_data = \
{'': ['*']}

install_requires = \
['grpcio>=1.47.0,<2.0.0',
 'macaddress>=1.2.0,<2.0.0',
 'parsy>=1.4.0,<2.0.0',
 'protobuf>=4.21.2,<5.0.0',
 'pyee>=9.0.4,<10.0.0',
 'pylev>=1.4.0,<2.0.0']

setup_kwargs = {
    'name': 'finsy',
    'version': '0.1.0',
    'description': 'Async P4Runtime/gNMI Framework',
    'long_description': '# 🐟 Finsy \n\n[![ci](https://github.com/byllyfish/finsy/actions/workflows/ci.yml/badge.svg)](https://github.com/byllyfish/finsy/actions/workflows/ci.yml) [![codecov](https://codecov.io/gh/byllyfish/finsy/branch/main/graph/badge.svg?token=8RPYWRXNGS)](https://codecov.io/gh/byllyfish/finsy)\n\nFinsy is a P4Runtime controller framework written in Python using asyncio.\n\n```python\nimport asyncio\nimport finsy as fy\n\nasync def main():\n    sw1 = fy.Switch("sw1", "127.0.0.1:50001")\n    async with sw1:\n        print(sw1.p4info)\n\nasyncio.run(main())\n```\n\nFor more examples, see the examples directory.\n',
    'author': 'Bill Fisher',
    'author_email': 'william.w.fisher@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/byllyfish/finsy',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
