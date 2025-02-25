from django.shortcuts import render, get_object_or_404
from .models import Product
from django.templatetags.static import static
from django.conf import settings

# Create your views here.

# Home page view
def index_view(request):
    newest_product_list = Product.objects.order_by("-date_rec")[:5]
    product_image_url = static(f"aria_music/{Product.sku}.jpg")

    # Return the context to the template
    return render(request, 'aria_music/index.html', {
        "newest_product_list": newest_product_list,
        "product_image_url": product_image_url
    })

def product_detail_view(request, product_sku):
    product = get_object_or_404(Product, sku=product_sku)
    product_image_url = static(f"aria_music/{product.sku}.jpg")

    return render(request, 'aria_music/product.html', {
        "product": product,
        "product_image_url": product_image_url
    })

def product_search_view(request):
    query = request.GET.get("q", "") # Get search query from URL parameter
    products = Product.objects.filter(name__icontains=query) if query else []
    product_image_url = settings.STATIC_URL + "aria_music/" + str(Product.sku) + ".jpg"


    return render(request, "aria_music/search_results.html", {
        "query": query,
        "products": products,
        "product_image_url":product_image_url
    })