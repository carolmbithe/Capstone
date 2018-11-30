from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url(r'^index/',views.index,name='index'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^create/profile$',views.create_profile,name='create-profile'),
    url(r'^edit/profile$',views.edit_profile,name='edit-profile'),
    url(r'^new/post$',views.new_post,name='post'),
    url(r'^new/receipt$',views.new_receipt,name='receipt'),
    url(r'^vacant/',views.vacant,name='vacant'),
    url(r'^home/',views.home,name='home'),
    url(r'^house/(\d+)',views.house,name='house'),





]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
