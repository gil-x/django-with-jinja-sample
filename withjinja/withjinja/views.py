from django.views.generic.base import TemplateView

class HomePageView(TemplateView):

    template_name = "home.html"


class SimplePageView(TemplateView):

    template_name = "simple.html"
# plup+nico+gino+celine