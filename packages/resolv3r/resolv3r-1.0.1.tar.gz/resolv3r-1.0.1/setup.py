# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['resolv3r']

package_data = \
{'': ['*']}

install_requires = \
['asyncssh>=2.11.0,<3.0.0', 'netmiko>=4.1.1,<5.0.0']

setup_kwargs = {
    'name': 'resolv3r',
    'version': '1.0.1',
    'description': 'A simple python package aimed at simplifying the vendor resolution process for network devices',
    'long_description': '# Overview\nResolv3r is a simple python package aimed at resolving the vendor associated with a given ip\n\n**Note: this package only resolves devices as either cisco or aruba!**\n\nTo install using pip, simply run:\n```commandline\npip3 install resolv3r\n```\n\n# Dependencies\nTested in 3.10 (Use in older versions of python at your own risk)\n\nLook in pyproject.toml for more details into the project dependencies:\n - asyncssh\n - netmiko\n\n# How to use?\nIn your python project, simply write:\n```commandline\nfrom resolv3r import Resolver\n```\nNow, to resolve a given ip to a vendor, you first need to create a Resolver object:\n```commandline\nresolver = Resolver("192.168.0.1", "username", "password")\n```\nNow, begin the resolution process using:\n```commandline\ndevice_vendor = resolver.detect_vendor()\n```\nThis should return the correct vendor of the ip in question: either "cisco_ios" or "hp_procurve"\n\n# How does this work?\nFirst, resolv3r uses asyncssh to connect to the device in question and determine device type using a single command ("sh version")\n\nIf that fails, resolv3r moves onto using netmiko\'s autodetection feature to resolve the vendor.\n\nFinally, if that doesn\'t work, resolv3r raises a LookupError, indicating that the vendor resolution process was not successful.\n',
    'author': 'hullabrian',
    'author_email': None,
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://github.com/HullaBrian/resolv3r',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
