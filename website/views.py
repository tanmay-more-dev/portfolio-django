from django.views import generic
from .models import Contact
from django.contrib.messages.views import SuccessMessageMixin
from blogs.models import Blog
from projects.models import Project

class IndexView(SuccessMessageMixin, generic.CreateView):
    model = Contact
    template_name = "website/index.html"
    fields = "__all__"
    success_url = '/#contact'
    success_message = "Message sent successfully!"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["blogs_list"] = Blog.objects.order_by("-id")[:3]
        context["projects_list"] = Project.objects.order_by("-id")[:3]
        return context

class BlogView(generic.ListView):
    model = Blog
    template_name = 'website/blogs.html'
    context_object_name = "blogs_list"

    def get_queryset(self):
        return Blog.objects.order_by("-id")
    

class ProjectView(generic.ListView):
    model = Project
    template_name = 'website/projects.html'
    context_object_name = "projects_list"

    def get_queryset(self):
        return Project.objects.order_by("-id")

class BlogDetailView(generic.DetailView):
    model = Blog
    template_name = 'website/blog_detail.html'
    context_object_name = 'blog'

class ProjectDetailView(generic.DetailView):
    model = Project
    template_name = 'website/project_detail.html'
    context_object_name = 'project'
