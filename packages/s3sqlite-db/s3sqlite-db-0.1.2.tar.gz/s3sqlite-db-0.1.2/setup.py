# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['s3sqlite_db']

package_data = \
{'': ['*']}

install_requires = \
['boto3>=1.24.31,<2.0.0', 'databases[aiosqlite]>=0.6.0,<0.7.0']

setup_kwargs = {
    'name': 's3sqlite-db',
    'version': '0.1.2',
    'description': '',
    'long_description': '# Welcome to s3sqlite-db\n![build status](../../workflows/ci/badge.svg)\n\nThis is an extension to [encode/databases](https://github.com/encode/databases)\nthat allows using sqlite database with AWS S3.\nMain purpose for this is use with AWS Lambda, to download sqlite db to Lambda on db connect and upload back on disconnect.\n\n## Installation\n\n```console\n$ pip install s3sqlite-db\n```\n\n## Usage\n\nYou can use S3Database as async context manager:\n\n```Python\nS3_BUCKET = \'my-bucket\'\nS3_KEY = \'database.sqlite\'\nDATABASE_URL = f\'s3sqlite://{S3_BUCKET}/{S3_KEY}\'\n\nasync with S3Database(DATABASE_URL) as db:\n    query = table.select()\n    db.fetch_all(query)\n\n```\n\nor with async framework like FastAPI:\n\n```Python\nfrom fastapi import FastAPI\n\n\napp = FastAPI()\ndatabase = S3Database(DATABASE_URL)\n\n\n@app.on_event("startup")\nasync def startup():\n    await database.connect()\n\n@app.on_event("shutdown")\nasync def shutdown():\n    await database.disconnect()\n```\n\n## Configuration\nBy default if remote database was modified, exception is raised, but `ignote_conflicts=True` argument can be specified, to force overwrite.\n\n```Python\nasync with S3Database(DATABASE_URL, ignote_conflicts=True) as db:\n    ...\n```\n\nAlso you can specify a path to download local copy of db.\nThis can be useful when working locally (not on AWS Lambda), or when whorking with several sqlite databaases at the same time.\n\n```Python\nasync with S3Database(DATABASE_URL, local_path=\'/path/to/db.sqlite\') as db:\n    ...\n```\n',
    'author': 'Smetanin Aleksandr',
    'author_email': 'smetamx@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/smetam/s3sqlite-db',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
