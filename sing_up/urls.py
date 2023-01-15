from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin/', admin.site.urls),
    path('', include('sing.urls')),
    path('signup/', include('sing.urls'), name='singupuser'),
    path('logout/', include('sing.urls')),
    path('login', include('sing.urls')),
    path('ready/', include('sing.urls'))
]

