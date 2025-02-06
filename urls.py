from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = "aria_music"
urlpatterns = [
    path("", views.index_view, name="index"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)