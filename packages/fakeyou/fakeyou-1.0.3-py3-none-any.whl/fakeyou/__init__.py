__title__ = "fakeyou.py"
__author__ = "Shards-7"
__license__ = "GNU"
__copyright__ = "Copyright 2022 Shards"
__version__ = "1.0.3"

from .fakeyou import FakeYou
from requests import get
from json import loads
__newest__=loads(get("https://pypi.python.org/pypi/Amino.py/json").text)["info"]["version"]

if __newest__ != __version__:
	print(f"New version of fakeyou.py is out : {__newest__} (Using __version__)")