from django.urls import path
from .views import (
    VideoListAPIView, VideoRetrieveAPIView,
    VideoUpdateAPIView, VideoDestroyAPIView, VideoCreateAPIView
)

urlpatterns = [
    path('', VideoListAPIView.as_view(), name='video_list'),
    path('upload/', VideoCreateAPIView.as_view(), name='video_upload'),
    path('<int:pk>/', VideoRetrieveAPIView.as_view(), name='video_detail'),
    path('<int:pk>/update/', VideoUpdateAPIView.as_view(), name='video_update'),
    path('<int:pk>/delete/', VideoDestroyAPIView.as_view(), name='video_destroy'),
]