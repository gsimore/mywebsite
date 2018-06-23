from django.conf.urls import url
from django.views.generic import TemplateView

urlpatterns = [
    # path('/', HomeView),
    url('about/', TemplateView.as_view(template_name="index.html")),
]
