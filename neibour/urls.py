# from django.urls import path
from . import views
from neibour import views as user_views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import url

urlpatterns = [
    url('', views.home, name='home'),
    url('accounts/register/', views.register, name='register'),
    url('profile/', views.profile, name='profile'),
    url('update_profile/', user_views.update_profile, name='update_profile'),
    url('new_hood/', views.new_hood, name='new_hood'),
    url('hood/', views.hood, name='hood'),
    url('edithood/', views.edit_hood, name='edithood'),
    url('businesses/<id>', views.businesses, name='hoodbusiness'),
    url('singlehood/<id>', views.singlehood, name='singlehood'),
    url('new_business/', views.newbiz, name='newbiz'),
    url('post', views.post, name='post'),
    url('hoodpost/<id>', views.posthood, name='hoodpost'),
    url('joinhood/<id>', views.joinhood, name='joinhood'),
    url('leavehood/<id>', views.leavehood, name='leavehood'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)