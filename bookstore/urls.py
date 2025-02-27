from rest_framework import routers

from .viewsets import BookViewSet 

app_name = 'bookstore'
router = routers.SimpleRouter()
router.register(r'', BookViewSet, basename='book')
urlpatterns = router.urls
