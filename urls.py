from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = "aria_music"
urlpatterns = [
    path("", views.index_view, name="index"),
    path("product/<str:product_sku>/", views.product_detail_view, name="product_detail"),
    path("product/search/", views.product_search_view, name="product_search"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
