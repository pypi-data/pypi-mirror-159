# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['bgprecorder']

package_data = \
{'': ['*']}

install_requires = \
['logzero>=1.7.0,<2.0.0',
 'pickleDB>=0.9.2,<0.10.0',
 'psycopg2-binary>=2.9.3,<3.0.0']

entry_points = \
{'console_scripts': ['bgpquery = bgprecorder.cli:query',
                     'bgprecorder = bgprecorder.cli:recorder']}

setup_kwargs = {
    'name': 'bgprecorder',
    'version': '0.1.3',
    'description': 'BGP rib timeseries recording tool',
    'long_description': '# bgp route collector\n\nCreate a BGP RIB time series database from MRT format dump files.\n\n## how to deploy\n### docker\n1. Create docker-compose.yml with reference to docker-compose.sample.yml.\n2. Create .env\n```\nBGPRECORDER_DB_HOST=postgres\nBGPRECORDER_DB_PORT=5432\nBGPRECORDER_DB_NAME=bgprecorder\nBGPRECORDER_DB_USER=postgres\nBGPRECORDER_DB_PASSWORD=PASSWORD\n\n```\n3. run\n```\ndocker-compose up -d\n```\n\n\n### native install\nTBD\n\n## CLI tool\n\n### bgprecord\n\n```\n$ bgprecorder  -h \nusage: bgprecorder [-h] [-H DB_HOST] [-p DB_PORT] [-u DB_USER] [-w DB_PASSWORD] [-d DB_NAME] [-c COMPRESS] [-i DURATION] [-f MRT_DUMP_FILES]\n\nbgprecord dump BGP MRT rib to DB\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -H DB_HOST, --db_host DB_HOST\n                        db host. default: localhost or $BGPRECORDER_DB_HOST\n  -p DB_PORT, --db_port DB_PORT\n                        db port. default: 5432 or $BGPRECORDER_DB_PORT\n  -u DB_USER, --db_user DB_USER\n                        db user. default: postgres or $BGPRECORDER_DB_USER\n  -w DB_PASSWORD, --db_password DB_PASSWORD\n                        db password. default: None or $BGPRECORDER_DB_PASSWORD\n  -d DB_NAME, --db_name DB_NAME\n                        db name. default: bgprecorder or $BGPRECORDER_DB_RECORDER\n  -c COMPRESS, --compress COMPRESS\n                        compress MRT dump after import. default: False\n  -i DURATION, --duration DURATION\n                        interval of recording (sec.) default: 3600 or $BGPRECORDER_DURATION\n  -f MRT_DUMP_FILES, --mrt_dump_files MRT_DUMP_FILES\n                        target MRT dumpfile match rule. default: ./mrt/*.dump or $BGPRECORDER_DURATION\n```\n\n\n```\n$ bash misc/env.sh\n$ bgprecord \n```\n\n### bgpquery\n```\n$ bgpquery  -h \nusage: bgpquery [-h] -a ADDRESS [-t DATETIME] [-H DB_HOST] [-p DB_PORT] [-u DB_USER] [-w DB_PASSWORD] [-d DB_NAME]\n\nbgpquery: get BGP rib json from bgprecorder db\n\noptional arguments:\n  -h, --help            show this help message and exit\n  -a ADDRESS, --address ADDRESS\n                        target address\n  -t DATETIME, --datetime DATETIME\n                        target datetime. example: "200601021504"\n  -H DB_HOST, --db_host DB_HOST\n                        db host. default: localhost or $BGPRECORDER_DB_HOST\n  -p DB_PORT, --db_port DB_PORT\n                        db port. default: 5432 or $BGPRECORDER_DB_PORT\n  -u DB_USER, --db_user DB_USER\n                        db user. default: postgres or $BGPRECORDER_DB_USER\n  -w DB_PASSWORD, --db_password DB_PASSWORD\n                        db user. default: None or $BGPRECORDER_DB_PASSWORD\n  -d DB_NAME, --db_name DB_NAME\n                        db user. default: bgprecorder or $BGPRECORDER_DB_RECORDER\n```\n\n```\n$ bash misc/env.sh\n$ bgpquery -a 3ffe::114  -d 202207131800  | jq\n{\n  "id": 13735,\n  "time": "2022-07-13T17:00:32",\n  "path_id": 3204,\n  "type_name": "TABLE_DUMP2_AP",\n  "sequence": null,\n  "from_ip": "2001:200:e00:300:dad::4",\n  "from_as": 0,\n  "originated": null,\n  "origin": "IGP",\n  "aspath": "400 300",\n  "nlri_type": null,\n  "nlri": "3ffe::/32",\n  "nexthop": "2001:db8::ace",\n  "community": "4690:64500",\n  "large_community": null\n}\n{\n  "id": 13736,\n  "time": "2022-07-13T17:00:32",\n  "path_id": 4634,\n  "type_name": "TABLE_DUMP2_AP",\n  "sequence": null,\n  "from_ip": "2001:200:e00:300:dad::5",\n  "from_as": 0,\n  "originated": null,\n  "origin": "IGP",\n  "aspath": "100 200 300",\n  "nlri_type": null,\n  "nlri": "3ffe::/32",\n  "nexthop": "2001:db8::beaf",\n  "community": "4690:64501",\n  "large_community": null\n}\n```\n\n',
    'author': 'yas-nyan',
    'author_email': 'yas-nyan@sfc.wide.ad.jp',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/wide-vsix/bgprecorder',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
