from django.urls import path

from content.apps import ContentConfig
from content.views import ContentListView, ContentDetailView, home

app_name = ContentConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('content-list', ContentListView.as_view(), name='content_list'),
    path('detail-content/<int:pk>', ContentDetailView.as_view(), name='detail_content'),
]
