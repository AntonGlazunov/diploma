from django.urls import path

from content.apps import ContentConfig
from content.views import ContentListView, ContentDetailView, RecommendedMoviesListView

app_name = ContentConfig.name

urlpatterns = [
    path('', ContentListView.as_view(), name='content_list'),
    path('detail-content/<int:pk>', ContentDetailView.as_view(), name='detail_content'),
    path('recommended-list', RecommendedMoviesListView.as_view(template_name='content/movie_list.html'), name='recommended_list'),
]
