from django.conf import settings
from django.shortcuts import render
from django.views import View


class BaseView(View):
    """
    An "abstract view" to manage the elements all of the site's pages have in common
    """

    def __init__(self):
        super().__init__()
        self.params = {
            "title_suffix": "",
            "debug": settings.DEBUG,
        }


class IndexView(BaseView):
    """
    A view for the site's index page
    """

    def get(self, request):
        return render(request, "index.html", self.params)
