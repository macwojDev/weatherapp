from django.views.generic import RedirectView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('', include('core.urls')),
    path("admin/", admin.site.urls),
]
