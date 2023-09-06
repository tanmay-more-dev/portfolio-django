from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('blog/<int:pk>/', views.BlogDetailView.as_view(), name="blog_detail"),
    path('project/<int:pk>/', views.ProjectDetailView.as_view(), name="project_detail"),
]