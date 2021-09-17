from django.contrib import admin
from django.urls import path, include

from rh.urls import funcionarios_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(funcionarios_urls))
]
