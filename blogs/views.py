from django.shortcuts import render
from django.views import generic

class BlogsView(generic.TemplateView):
    template_name = "blogs.html"