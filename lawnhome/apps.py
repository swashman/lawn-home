"""App Configuration"""

# Django
from django.apps import AppConfig

# Lawn Home
from lawnhome import __version__


class LawnHomeConfig(AppConfig):
    """App Config"""

    name = "Lawn Home"
    label = "Lawn Home"
    verbose_name = f"Lawn Home v{__version__}"
