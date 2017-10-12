from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^room$', views.room_list, name='room_list'),
    url(r'^room/new$', views.room_new, name='room_new'),
    url(r'^room/(?P<number>[\w]+)$', views.room_edit, name='room_edit'),

    url(r'^mnfs$', views.mnf_list, name='mnf_list'),
    url(r'^mnfs/new$', views.mnf_new, name='mnf_new'),
    url(r'^mnfs/(?P<name>[\w]+)$', views.mnf_edit, name="mnf_edit"),

    url(r'^list$', views.list, name='list'),
    url(r'^edit/(?P<inv_number>[\w]+)$',
        views.eq_edit,
        name='eq_edit'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
