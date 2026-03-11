from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("home.urls")),
    path("about/", include("about.urls")),
    path("portfolio/", include("portfolio.urls")),
    path("blog/", include("blog.urls")),
    path("contact/", include("contact.urls")),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
