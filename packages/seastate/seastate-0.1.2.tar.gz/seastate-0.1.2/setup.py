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
    'version': '0.1.2',
    'description': 'Collect ocean measurement data based on location and timeframe',
    'long_description': "# Seastate\n\n## Summary\nCollect ocean measurement data based on location and timeframe\n\n**Features**\n- Closest active station is selected for each measurement\n- Reaches into secondary historical archives when required\n- Returns pandas dataframe compatible lists\n- Available measurements: Tide, wind, water temp, air temp, air pressure, conductivity and swell information\n- Datasources: NOAA NDBC, NOAA Tides and Currents\n\n## Installing\n`pip install seastate`\n\n## Quick start\n```\nfrom seastate.seastate import SeaState\nfrom datetime import datetime\n\n# make SeaState object for specific location\nsan_diego = SeaState(32,-117)\n\n# retrieve measurements for today\nsan_diego_today = san_diego.measurements_from_date_range(datetime.today())\n\nsan_diego_today['tide'] -> [{t: time, v: value, s: stdev]\nsan_diego_today['wind']-> [{t: time, v: value, d: direction, g: gust}]\nsan_diego_today['water_temp']-> [{t: time, v: value}]\nsan_diego_today['air_temp']-> [{t: time, v: value}]\nsan_diego_today['air_press']-> [{t: time, v: value}]\nsan_diego_today['wave']-> [{t: time, v: Wave Height, dpd: Dominant Period, mwd: dpd Direction}]\nsan_diego_today['conductivity']-> [{t: time, v: value}] \n```\nMeasurement details for NDBC are [here](https://www.ndbc.noaa.gov/measdes.shtml) and for Tides and Currents [here](https://api.tidesandcurrents.noaa.gov/api/prod/responseHelp.html)\n\n## Measurement x API breakdown\n| Measurement | T&C | NDBC |\n| ---: | :---: | :---: |\n|tide | y | y |\n|wind | y | y |\n|water_temp | y | y |\n|air_temp | y | y |\n|air_press | y | y |\n|wave |  | y |\n|conductivity | y |  |\n\n## More Examples\n### Measurements for past 30 days\n```\nfrom seastate.seastate import SeaState\nfrom datetime import datetime, timedelta\n\nstart = datetime.today()-timedelta(days=30)\nend = datetime.today()\nsan_diego_past_30 = san_diego.measurements_from_date_range(start,end)\n```\n### Hourly Slices\n```\nsan_diego_past_30_hourly = san_diego.hourly(start,end) # this returns a single reading per hour\n# experimental feature\n# no guarantee between APIs that readings will align or exist in all cases\n```\n",
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
