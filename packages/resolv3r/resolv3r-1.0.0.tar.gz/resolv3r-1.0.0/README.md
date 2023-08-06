# Overview
Resolv3r is a simple python package aimed at resolving the vendor associated with a given ip

**Note: this package only resolves devices as either cisco or aruba!**

To install using pip, simply run:
```commandline
pip3 install resolv3r
```

# Dependencies
Tested in 3.10 (Use in older versions of python at your own risk)

Look in pyproject.toml for more details into the project dependencies:
 - asyncssh
 - netmiko

# How to use?
In your python project, simply write:
```commandline
from resolv3r import Resolver
```
Now, to resolve a given ip to a vendor, you first need to create a Resolver object:
```commandline
resolver = Resolver("192.168.0.1", "username", "password")
```
Now, begin the resolution process using:
```commandline
device_vendor = resolver.detect_vendor()
```
This should return the correct vendor of the ip in question: either "cisco_ios" or "hp_procurve"

# How does this work?
First, resolv3r uses asyncssh to connect to the device in question and determine device type using a single command ("sh version")

If that fails, resolv3r moves onto using netmiko's autodetection feature to resolve the vendor.

Finally, if that doesn't work, resolv3r raises a LookupError, indicating that the vendor resolution process was not successful.
