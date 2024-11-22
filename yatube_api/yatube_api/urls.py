from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from rest_framework.authtoken import views
from api.views import PostViewSet, UserViewSet, CommentViewSet, GroupViewSet

router = routers.DefaultRouter()
router.register('posts', PostViewSet)
router.register('users', UserViewSet)
router.register('groups', GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('api/v1/posts/<int:pk>/comments/', CommentViewSet.as_view(
        {'get': 'list', 'post': 'create'})),
    path('api/v1/posts/<int:pk>/comments/<int:kp>/', views.obtain_auth_token),
    path('api/v1/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )
