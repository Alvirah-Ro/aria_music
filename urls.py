from django.urls import path
from . import views

app_name = "aria_music"
urlpatterns = [
    path("", views.index_view, name="index"),
]
