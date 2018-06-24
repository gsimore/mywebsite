from django.conf.urls import url
from .views import HomeView


urlpatterns = [
    # path('/', HomeView),
    url('about/$', HomeView.as_view()),
]
