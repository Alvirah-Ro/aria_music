from django.shortcuts import render

# Create your views here.
def index_view(request):
    store_name = "Aria Music"
    # Return the context to the template
    return render(request, 'aria_music/index.html', {
        'store_name': store_name, 
    })    
    