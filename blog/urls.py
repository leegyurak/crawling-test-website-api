from rest_framework.routers import SimpleRouter

from blog.views import PostListRetrieveViewSet


urlpatterns = []

router = SimpleRouter(trailing_slash=False)

router.register('post', PostListRetrieveViewSet)

urlpatterns += router.urls