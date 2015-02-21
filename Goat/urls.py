from django.conf.urls import patterns, include, url

from django.contrib import admin
from rest_framework.routers import DefaultRouter
from Goat.stores.views import StoreViewSet

admin.autodiscover()

router = DefaultRouter()
router.register(r'stores', StoreViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Goat.views.api_root', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^users/', include('Goat.users.urls', namespace='users')),
)

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls',
                               namespace='rest_framework')),
]
