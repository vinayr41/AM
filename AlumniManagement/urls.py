from django.conf.urls import include,url
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'Database/',include('Database.urls')),
    url(r'Connect/', include('Connect.urls')),
    url(r'admin_module/',include('admin_module.urls')),
]
