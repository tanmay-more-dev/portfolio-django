from django.shortcuts import render
from django.views import generic

class ProjectsView(generic.TemplateView):
    template_name = "projects.html"

