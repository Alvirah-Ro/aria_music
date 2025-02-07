from django.shortcuts import render
from .models import Product

# Create your views here.

# Home page view
def index_view(request):
    newest_product_list = Product.objects.order_by("-date_rec")[:5]
    product_name = Product.name
    product_img = Product.image
    product_price = Product.price

    # Return the context to the template
    return render(request, 'aria_music/index.html', {
        "newest_product_list": newest_product_list,
        "product_name": product_name,
        "product_img": product_img,
        "product_price": product_price
    })