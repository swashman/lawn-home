"""App Configuration"""

# Django
from django.apps import AppConfig

# Lawn Home
from lawnhome import __version__


class LawnHomeConfig(AppConfig):
    """App Config"""

    name = "lawnhome"
    label = "lawnhome"
    verbose_name = f"Lawn Home v{__version__}"
