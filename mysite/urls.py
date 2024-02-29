from polls.views import home, post, viewre, viewpost, registerup, registercreate, delete, deleteregister, editpost
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home, name=''),
    path('post/', post, name='post'),
    path('viewre/', viewre, name='viewre'),
    path('viewpost/', viewpost, name='viewpost'),
    path('delete/<int:id>/', delete, name='delete'),
    path('deleteregister/<int:id>/', deleteregister, name='deleteregister'),
    path('registercreate/', registercreate, name='registercreate'),
    path('register/<int:id>/', registerup, name='register'),
    path('editpost/<int:id>/', editpost, name='editpost'),
    path('admin/', admin.site.urls),

    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
