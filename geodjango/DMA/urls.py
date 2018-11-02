from django.conf.urls import url
from DMA import views

app_name = 'DMA'

urlpatterns=[
    url(r'^DMAs/(?P<pk>[-\w]+)$',
        views.DMAmap.as_view(), name='DMA-detail'),
    url(r'^$', views.overviewMAP, name = "DMA-overview"),
    url(r'^DMA-info/(?P<DMA_id>[-\w]+)$',
       views.DMA_info, name='DMA-info'),
    ]


#?P<pk> # is a python specific reg express
# it stores the value for later use
#>>> match = re.match("^users/(?P<pk>[0-9]+)/$", "users/123/")
#>>> match.group('pk')
#'123'
#>>> match.groupdict()
#{'pk': '123'}
