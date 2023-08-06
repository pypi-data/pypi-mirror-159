# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['audiocodes_exporter', 'audiocodes_exporter.collectors']

package_data = \
{'': ['*']}

install_requires = \
['prometheus-client>=0.14.1,<0.15.0', 'requests>=2.28.1,<3.0.0']

entry_points = \
{'console_scripts': ['audiocodes-exporter = audiocodes_exporter.cli:main']}

setup_kwargs = {
    'name': 'audiocodes-exporter',
    'version': '0.1.4',
    'description': 'AudioCodes SBC exporter for the Prometheus monitoring system.',
    'long_description': '# AudioCodes SBC Prometheus exporter\nThis is an exporter that exposes information gathered from AudioCodes SBC for use by the Prometheus monitoring system.\n\n**This is a work in progress!!**\n\n## Installation\n`pip install audiocodes-exporter`\n\n## Requirements\nAudioCodes SBC v7.4\nPython 3.10+',
    'author': 'Matthew Neirynck',
    'author_email': 'matthew.neirynck@telsmart.eu',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://bitbucket.org/matthew_neirynck/audiocodes-exporter',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
