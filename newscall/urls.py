from django.urls import path
from .views import StoriesAPIView, StoryDetailAPIView

urlpatterns = [
    path('stories/', StoriesAPIView.as_view(), name='stories_list'),
    path('stories/<str:internalID>/', StoryDetailAPIView.as_view(), name='story_detail'),
]
