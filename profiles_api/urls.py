from django.urls import path, include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('profile', views.UserViewset)
urlpatterns = [
    path('users', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('', include(router.urls)),


]