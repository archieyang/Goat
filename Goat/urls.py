from django.conf.urls import patterns, include, url

from django.contrib import admin
from rest_framework.routers import DefaultRouter
from Goat.stores.views import StoreViewSet
from Goat.users.views import UserViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'stores', StoreViewSet)
router.register(r'users', UserViewSet)

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'Goat.views.api_root', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^', include(router.urls)),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api-auth/', include('rest_framework.urls',
                                                  namespace='rest_framework')),
)

