from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inventory/', include('inventory.urls')),
    path('register/', include('register.urls')),
    path('login/', include('login.urls')),
    path('', include('login.urls'))
]
