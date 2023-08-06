__version__ = "1.0.3"


import asyncssh
import asyncio
from netmiko import SSHDetect


class Resolver(object):
    def __init__(self, ip: str, username: str, password: str, **kwargs):
        self._ip = ip
        self.username = username
        self.password = password
        self.kwargs = kwargs

        self.vendor: str = ""

    def detect_vendor(self) -> str:
        self.async_detect_vendor()

        if self.vendor != "":
            return self.vendor

        self.netmiko_detect_device()

        if self.vendor != "":
            return self.vendor

        raise LookupError("Could not identify device type")

    def async_detect_vendor(self) -> None:
        asyncio.get_event_loop().run_until_complete(self._async_detect_vendor())

    async def _async_detect_vendor(self) -> None:
        self.vendor = ""
        try:
            async with asyncssh.connect(
                self._ip,
                username=self.username,
                password=self.password,
                known_hosts=None,
                **self.kwargs
            ) as conn:
                async with conn.create_process(
                    ""
                ) as process:
                    process.stdin.write("sh version\n")
                    result = await process.stdout.readline()

                    self.vendor = "hp_procurve" if "login" in result.lower() else "cisco_ios"

        except asyncssh.misc.PermissionDenied:
            self.vendor = ""
            raise ConnectionRefusedError("Incorrect credentials")

        except (OSError, asyncssh.Error) as e:
            self.vendor = ""
            raise OSError("Couldn't connect to device")

    def netmiko_detect_device(self) -> None:
        remote_device = {
            "device_type": "autodetect",
            "host": self._ip,
            "username": self.username,
            "password": self.password
        }
        guesser = SSHDetect(**remote_device)
        self.vendor = guesser.autodetect()

        if self.vendor == "aruba_osswitch":
            self.vendor = "hp_procurve"
