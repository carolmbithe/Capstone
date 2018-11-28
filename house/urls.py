from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name='welcome'),
    url(r'^index/',views.index,name='index'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^create/profile$',views.create_profile,name='create-profile'),
    url(r'^new/receipt$',views.new_receipt,name='receipt'),
    url(r'^vacant/',views.vacant,name='vacant'),
    url(r'^home/',views.home,name='home'),
    url(r'^filter/(\d+)',views.filter,name='filter'),





]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
