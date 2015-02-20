from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns
from Goat.stores import views

urlpatterns = patterns('Goat.stores',
    # Examples:
    # url(r'^$', 'monkey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.StoreList.as_view(), name='list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)