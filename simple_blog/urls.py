from django.contrib import admin
from django.urls import path,include







urlpatterns = [
    path('admin/', admin.site.urls),
    #path('',include('blog_app.urls')),
    path('', include('friendship_systeme.urls')),
    path('api/auth/', include('Auth_.urls')),
    path('post/', include('postes_app.urls')),
]
