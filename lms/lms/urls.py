from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/manager/', include('manager.urls')),
    path('docs/', include('docs.urls'))
]
