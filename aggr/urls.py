from django.conf.urls.defaults import patterns, include, url
from aggr.models import *


urlpatterns = patterns('aggr.views',
                       # (r'', 'main'),
                       (r'^posts/$', 'index'),
                       (r'^posts/(?P<post_id>\d+)$', 'detail'),
)

