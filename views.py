from django.shortcuts import render
from .models import Product

# Create your views here.

# Home page view
def index_view(request):
    newest_product_list = Product.objects.order_by("-date_rec")[:5]

    # Return the context to the template
    return render(request, 'aria_music/index.html', {
        "newest_product_list": newest_product_list,
    })