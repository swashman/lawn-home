"""Hook into Alliance Auth"""

# Django
# Django
from django.utils.translation import gettext_lazy as _

# Alliance Auth
from allianceauth import hooks
from allianceauth.services.hooks import MenuItemHook, UrlHook

# Lawn Home
from lawnhome import urls


class LawnHomeMenuItem(MenuItemHook):
    """This class ensures only authorized users will see the menu entry"""

    def __init__(self):
        # setup menu entry for sidebar
        MenuItemHook.__init__(
            self,
            _("Lawn Home"),
            "fas fa-cube fa-fw",
            "lawnhome:index",
            navactive=["lawnhome:"],
        )

    def render(self, request):
        """Render the menu item"""

        if request.user.has_perm("lawnhome.basic_access"):
            return MenuItemHook.render(self, request)

        return ""


@hooks.register("menu_item_hook")
def register_menu():
    """Register the menu item"""

    return LawnHomeMenuItem()


@hooks.register("url_hook")
def register_urls():
    """Register app urls"""

    return UrlHook(urls, "lawnhome", r"^lawnhome/")
