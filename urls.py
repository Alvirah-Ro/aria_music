from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = "aria_music"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("product/{{ product.sku }}/", views.product_view, name="product"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
