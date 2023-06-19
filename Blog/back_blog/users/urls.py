from rest_framework import routers
from django.urls import include, path
from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', views.LoginView.as_view()),


]