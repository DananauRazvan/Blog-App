from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import index, ArticleViewSet, UserViewSet


router = DefaultRouter()
router.register(r'articles', ArticleViewSet, basename='articles')
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('', index),
    # path('articles/', ArticleList.as_view()),
    # path('articles/<int:id>/', ArticleDetails.as_view()),
]