# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['zdppy_password_hash',
 'zdppy_password_hash._setup',
 'zdppy_password_hash.crypto',
 'zdppy_password_hash.crypto._blowfish',
 'zdppy_password_hash.crypto.scrypt',
 'zdppy_password_hash.ext',
 'zdppy_password_hash.ext.django',
 'zdppy_password_hash.handlers',
 'zdppy_password_hash.tests',
 'zdppy_password_hash.utils',
 'zdppy_password_hash.utils.compat']

package_data = \
{'': ['*'], 'zdppy_password_hash': ['_data/wordsets/*']}

setup_kwargs = {
    'name': 'zdppy-password-hash',
    'version': '0.1.0',
    'description': '实现常用的hash加密算法',
    'long_description': None,
    'author': 'zhangdapeng520',
    'author_email': '1156956636@qq.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.10,<4.0',
}


setup(**setup_kwargs)
