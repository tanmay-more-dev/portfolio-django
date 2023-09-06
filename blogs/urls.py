from django.urls import path
from . import views

app_name = "blogs"
urlpatterns = [
    path('', views.BlogsView.as_view(), name="blogs_list"),
]
