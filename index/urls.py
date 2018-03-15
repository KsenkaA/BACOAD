from django.conf.urls import url
from django.contrib.auth import views as auth_views
from index import views
urlpatterns = [
    url(r'^search_form/$', views.search_form, name='search_form'),
    url(r'^search/$', views.search),
    url(r'^signup/$', views.signup),
    url(r'^login/$', views.login_user),
    url(r'^logout/$', auth_views.logout, {'next_page': '/index/search_form/'}, name='logout'),
    url(r'^adding/$', views.adding)
]