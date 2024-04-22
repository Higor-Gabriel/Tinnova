from django.contrib import admin
from django.urls import path, include
from produtores.api import urls as produtores_api_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(produtores_api_urls)),
]
