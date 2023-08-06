# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['f1_telemetry']

package_data = \
{'': ['*'], 'f1_telemetry': ['webapp/*', 'webapp/art/*']}

install_requires = \
['f1-packets>=2022.1.2,<2023.0.0',
 'influxdb-client>=1.30.0,<2.0.0',
 'websockets>=10.3,<11.0']

entry_points = \
{'console_scripts': ['f1-tel = f1_telemetry.__main__:main']}

setup_kwargs = {
    'name': 'f1-telemetry',
    'version': '2022.1.0',
    'description': 'F1 telemetry data collection and visualisation',
    'long_description': '# F1 Telemetry Data Collector\n\nThis Python application uses InfluxDB to collect telemetry data from the\nofficial F1 game.\n\n<p align="center">\n    <img src="art/telemetry-demo.gif"/>\n</p>\n\nIt is also possible to display live session and car data.\n\n<p align="center">\n    <img src="art/live-data.png"/>\n</p>\n\n\n## Installation\n\nThe application requires Python >= 3.8 to work.\n\n~~~\npip install pipx\npipx install f1-telemetry\n~~~\n\n## Usage\n\nEnsure that InfluxDB is running with at least an Org and an access token, and\nconfigured with an `f1-telemetry` bucket.\n\n~~~\nf1-tel <org> <token>\n~~~\n\nThis also serves a very basic web application for time-series and live data\nvisualisations. With InfluxDB still running, navigate to\n`http://localhost:20776/index.html` page in the browser with the `org` and\n`token` parameters, e.g.\n\n~~~\nhttp://localhost:20776/index.html?org=P403n1x87&token=NLyjW4ml8XuTPTwCbtC5PC1Z-JJ6lwjAm7B1-ScM_XP9N_eoCkIGTmm3wHrC92cQVsMmKofgqbx6PM-ZZgVQKw==\n~~~\n',
    'author': 'Gabriele N. Tornetta',
    'author_email': 'phoenix1987@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/P403n1x87/f1-telemetry',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
