from rest_framework import routers
from django.urls import include, path
from .views import PostViewSet, RetrieveUpdateDestroyAPIView, CommentViewSet, UpdateDestroyCommentViewSet


urlpatterns = [
    path('', PostViewSet.as_view()),
    path('update/', RetrieveUpdateDestroyAPIView.as_view()),
    path('<int:pk>/comment', CommentViewSet.as_view()),
    path('<int:pk>/comment_update', UpdateDestroyCommentViewSet.as_view())
]

