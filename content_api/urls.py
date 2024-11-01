from django.urls import path
from django.views.decorators.cache import cache_page

from content_api.apps import ContentApiConfig
from content_api.views import MovieListAPIView


app_name = ContentApiConfig.name

urlpatterns = [
    path('', cache_page(60)(MovieListAPIView.as_view()), name='recommended_list'),
]