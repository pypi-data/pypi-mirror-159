"""Real Python feed tuu.

Import the `feed` module to work with the Real Python feed:

    >>> from catadoc import feed
    >>> feed.get_titles()
    ['Logging in Python', 'The Best Python Books', ...]

See https://github.com/realpython/reader/ for more information.
"""
# Standard library imports
from importlib import resources

try:
    import tomllib
except ModuleNotFoundError:
    # Third party imports
    import tomli as tomllib


# Version of catadoc package
# Version of catadoc package
__version__ = "1.1.1"

# Read URL of the Real Python feed from config file
_cfg = tomllib.loads(resources.read_text("catadoc", "config.toml"))
URL = _cfg["feed"]["url"]
