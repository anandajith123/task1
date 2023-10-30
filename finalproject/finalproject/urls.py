from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static 


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app1.urls')),
    path('accounts/', include('django.contrib.auth.urls')),  # Include built-in authentication URLs
]



urlpatterns += static(settings.STATIC_URL)
