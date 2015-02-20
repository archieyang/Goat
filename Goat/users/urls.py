from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from Goat.users import views

urlpatterns = patterns('Goat.stores',
    # Examples:
    # url(r'^$', 'monkey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.UserList.as_view(), name='list'),
)

urlpatterns = format_suffix_patterns(urlpatterns)