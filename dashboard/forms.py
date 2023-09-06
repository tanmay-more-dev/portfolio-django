from datetime import date
from typing import Any
from django import forms
from blogs.models import Blog
from ckeditor.widgets import CKEditorWidget
from projects.models import Project

class ProjectForm(forms.ModelForm):
    date = forms.DateField(widget=forms.HiddenInput, required=False)
    desc = forms.CharField(widget=CKEditorWidget(), required=False)
    class Meta:
        model = Project
        fields = "__all__"

class BlogForm(forms.ModelForm):
    posted_on = forms.DateField(widget=forms.HiddenInput, required=False)
    posted_by = forms.CharField(widget=forms.HiddenInput, required=False)
    content = forms.CharField(widget=CKEditorWidget())
    class Meta:
        model = Blog
        fields = "__all__"
    
    # def save(self, commit=True):
    #     m = super(BlogForm, self).save(commit=False)
    #     m.posted_on = date.today()
    #     if commit:
    #         m.save()
    #     return m