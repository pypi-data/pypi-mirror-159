# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['seastate', 'seastate.api']

package_data = \
{'': ['*']}

install_requires = \
['defusedxml>=0.7.1,<0.8.0',
 'numpy>=1.23.1,<2.0.0',
 'requests>=2.28.1,<3.0.0',
 'urllib3>=1.26.10,<2.0.0']

setup_kwargs = {
    'name': 'seastate',
    'version': '0.1.0',
    'description': 'Collect seastate data based on location and timeframe',
    'long_description': '# Seastate\n\n## Summary\nCollect sea state data based on location and timeframe\n\n**Features**\n- Closest active station is selected for each measurement\n- Reaches into secondary historical archives when required\n- Returns pandas dataframe compatible lists\n- Available measurements: Tide, wind, water temp, air temp, air pressure, conductivity and swell information\n- Datasources: NOAA NDBC, NOAA Tides and Currents\n\n## Installing\n`pip install seastate`\n\n## Examples\n### Retrieving raw data\n```\nfrom seastate.seastate import SeaState\nfrom datetime import datetime, timedelta\n\n# make SeaState object for specific location\nsan_diego = SeaState(32,-117)\n\n# retrieve measurements for today\nstart = datetime.today()\nsan_diego_today = san_diego.measurements_from_date_range(start)\n\n# retrieve measurements for past 30 days\nstart = datetime.today()-timedelta(days=30)\nend = datetime.today()\nsan_diego_past_30 = san_diego.measurements_from_date_range(start,end)\n\n```\n',
    'author': 'Ivo',
    'author_email': 'ivorivetta@users.noreply.github.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/ivorivetta/seastate',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4',
}


setup(**setup_kwargs)
