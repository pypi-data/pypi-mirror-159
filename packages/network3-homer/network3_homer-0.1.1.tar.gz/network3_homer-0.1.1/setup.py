# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['network3_homer']

package_data = \
{'': ['*']}

install_requires = \
['Jinja2>=3.1.2,<4.0.0',
 'PyYAML>=6.0,<7.0',
 'click>=8.1.3,<9.0.0',
 'hedera-sdk-py>=2.16.3,<3.0.0',
 'pathlib>=1.0.1,<2.0.0']

entry_points = \
{'console_scripts': ['network3_homer = network3_homer.script:run']}

setup_kwargs = {
    'name': 'network3-homer',
    'version': '0.1.1',
    'description': 'Automated Business Ready Documents from network state stored on Hedera',
    'long_description': '# network3_homer\nBusiness ready documentation from network state stored on Hedera\n\n## Setup\n### Setup Python virtual environment\n```console\n$ python3 -m venv homer\n$ source homer/bin/activate\n(homer) $\n```\n### Setup Python virtual environment\n```console\n(socrates) $ pip install network3_homer\n```\n\n### Setup environment (Ubuntu with Java 11 OpenJDK)\nexport JAVA_HOME=/usr/lib/jvm/java-11-openjdk-amd64/\nexport OPERATOR_ID={ Hedera Account }\nexport OPERATOR_PRIVATE_KEY={ Hedera private key }',
    'author': 'John Capobianco',
    'author_email': 'ptcapo@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
