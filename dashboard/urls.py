from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'dashboard'
urlpatterns = [
    path("search/", views.SearchResultsView.as_view(), name='search_result'),
    path("projects/<int:pk>/update", views.UpdateProjectView.as_view(), name='update_project'),
    path("projects/add/", views.AddProjectView.as_view(), name='add_project'),
    path("projects/<int:pk>/delete", views.ProjectDeleteView.as_view(), name='project_delete'),
    path("projects/<int:pk>/", views.ProjectDetails.as_view(), name='project_detail'),
    path("projects/", views.ProjectListView.as_view(), name='projects'),
    path("blogs/<int:pk>/update", views.UpdateBlogView.as_view(), name='update_blog'),
    path("blogs/add/", views.AddBlogView.as_view(), name='add_blog'),
    path("blogs/<int:pk>/delete", views.BlogDeleteView.as_view(), name='blog_delete'),
    path("blogs/<int:pk>/", views.BlogDetails.as_view(), name='blog_detail'),
    path("blogs/", views.BlogListView.as_view(), name='blogs'),
    path("", views.MessageListView.as_view(), name='dashboard'),
    path("msg/", views.MessageListView.as_view(), name='messages'),
    path('msg/<int:pk>/', views.MessageDetails.as_view(), name='message_detail'),
    path('msg/<int:pk>/delete', views.MessageDeleteView.as_view(), name='message_delete'),
    path('login/', auth_views.LoginView.as_view(template_name='dashboard/login.html', next_page='/dashboard/msg/'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='dashboard/login.html', next_page='/dashboard/msg/',), name='logout'),
]