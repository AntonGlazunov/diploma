from django.urls import path
from django.views.decorators.cache import cache_page

from content.apps import ContentConfig
from content.views import ContentListView, ContentDetailView, RecommendedMoviesListView, statistics

app_name = ContentConfig.name

urlpatterns = [
    path('', statistics, name='statistics'),
    path('content_list/', cache_page(60)(ContentListView.as_view()), name='content_list'),
    path('detail-content/<int:pk>', ContentDetailView.as_view(), name='detail_content'),
    path('recommended-list', cache_page(60)(RecommendedMoviesListView.as_view(template_name='content/movie_list.html')), name='recommended_list'),
]
