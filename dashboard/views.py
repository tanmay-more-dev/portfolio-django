from datetime import date
from typing import Any, Dict
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic
from website.models import Contact
from blogs.models import Blog
from django.contrib.messages.views import SuccessMessageMixin
from .forms import BlogForm, ProjectForm
from projects.models import Project
from django.db.models import Q

class SearchResultsView(generic.TemplateView):
    template_name = "dashboard/search_results.html"

    def get_context_data(self, **kwargs):
        query = self.request.GET.get("q")
        context = super().get_context_data(**kwargs)
        context['blogs_list'] = Blog.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) | Q(posted_by__icontains=query) | Q(posted_on__icontains=query)
        )
        context['projects_list'] = Project.objects.filter(
            Q(title__icontains=query) | Q(category__icontains=query) | Q(date__icontains=query) | Q(desc__icontains=query) | Q(url__icontains=query)
        )
        context['messages_list'] = Contact.objects.filter(
            Q(name__icontains=query) | Q(email__icontains=query) | Q(subject__icontains=query) | Q(message__icontains=query)
        )
        context['query'] = query
        return context
    
    def dispatch(self, request, *args, **kwargs):
        if not self.request.GET.get("q"):
            return HttpResponseRedirect(reverse('dashboard:messages'))
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)

class UpdateProjectView(generic.UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'dashboard/add_project.html'
    success_url = reverse_lazy('dashboard:projects')

    def form_valid(self, form):
        if self.request.method == 'POST':
            obj = form.save(commit=False)
            obj.date = date.today()
            obj.save()
        return HttpResponseRedirect(self.success_url)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)

class AddProjectView(generic.CreateView):
    form_class = ProjectForm
    template_name = 'dashboard/add_project.html'
    success_url = reverse_lazy('dashboard:projects')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.date = date.today()
        obj.save()
        return HttpResponseRedirect(self.success_url)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)

class ProjectListView(generic.ListView):
    model = Project
    template_name = 'dashboard/projects.html'
    context_object_name = 'projects'
    paginate_by = 5

    def get_queryset(self):
        return Project.objects.order_by("-id")
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)
    
class ProjectDetails(generic.DetailView):
    model = Project
    template_name = 'dashboard/project_detail.html'
    context_object_name = 'project'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)

class ProjectDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Project
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:projects')
    success_message = "Project deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel_url"] = reverse('dashboard:projects')
        return context
    

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)  

class UpdateBlogView(generic.UpdateView):
    model = Blog
    form_class = BlogForm
    template_name = 'dashboard/add_blog.html'
    success_url = reverse_lazy('dashboard:blogs')

    def form_valid(self, form):
        if self.request.method == 'POST':
            obj = form.save(commit=False)
            obj.posted_by = self.request.user.get_full_name()
            obj.posted_on = date.today()
            obj.save()
        return HttpResponseRedirect(self.success_url)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)

class AddBlogView(generic.CreateView):
    form_class = BlogForm
    template_name = 'dashboard/add_blog.html'
    success_url = reverse_lazy('dashboard:blogs')

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.posted_by = self.request.user.get_full_name()
        obj.posted_on = date.today()
        obj.save()
        return HttpResponseRedirect(self.success_url)
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)

class BlogListView(generic.ListView):
    model = Blog
    template_name = 'dashboard/blogs.html'
    context_object_name = 'blogs'
    paginate_by = 5

    def get_queryset(self):
        return Blog.objects.order_by("-id")
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)
    
class BlogDetails(generic.DetailView):
    model = Blog
    template_name = 'dashboard/blog_detail.html'
    context_object_name = 'blog'

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)

class BlogDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Blog
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:blogs')
    success_message = "Blog deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel_url"] = reverse('dashboard:blogs')
        return context
    

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)    

class MessageListView(generic.ListView):
    model = Contact
    template_name = 'dashboard/messages.html'
    context_object_name = 'contacts'
    paginate_by = 5

    def get_queryset(self):
        return Contact.objects.order_by("-id")

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)
    
class MessageDetails(generic.DetailView):
    model = Contact
    template_name = 'dashboard/message_detail.html'
    context_object_name = 'message'

    def get_object(self):
        obj = super().get_object()
        obj.seen = True
        obj.save()
        return obj
    
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)

class MessageDeleteView(SuccessMessageMixin, generic.DeleteView):
    model = Contact
    template_name = 'dashboard/confirm_delete.html'
    success_url = reverse_lazy('dashboard:messages')
    success_message = "Message deleted"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cancel_url"] = reverse('dashboard:messages')
        return context
    

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse('dashboard:login'))
        return super().dispatch(request, *args, **kwargs)