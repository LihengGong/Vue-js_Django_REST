from rest_framework import routers
from article.viewsets import ArticleViewSet
from quickstart import views


router = routers.DefaultRouter()

router.register(r'article', ArticleViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
