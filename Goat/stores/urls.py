from django.conf.urls import patterns, include, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('Goat.stores',
    # Examples:
    # url(r'^$', 'monkey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'views.store_list', name='list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)