from django import forms

from example.demo.models import *


class ProjectForm(forms.ModelForm):
    class Meta:
        model = ProjectsModel
        fields = ('name', 'display_name', 'description', 'author', 'category')
        widgets = {
            'author': forms.HiddenInput(),
            'name': forms.TextInput(attrs={'placeholder': 'Internal name'}),
            'display_name': forms.TextInput(attrs={'placeholder': 'Displayed (pretty) name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write patch description here'}),
            'category': forms.Select(),
        }


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = ProjectsModel
        fields = ('name', 'display_name', 'description', 'author', 'category')
        widgets = {
            'name': forms.HiddenInput(),
            'author': forms.HiddenInput(),
            'display_name': forms.TextInput(attrs={'placeholder': 'Displayed (pretty) name'}),
            'description': forms.Textarea(attrs={'placeholder': 'Write patch description here'}),
            'category': forms.Select(),
        }


class FileForm(forms.ModelForm):
    class Meta:
        model = FilesModel
        fields = ('version', 'compatible', 'document', 'changelog', 'author', 'project')
        widgets = {
            'author': forms.HiddenInput(),
            'project': forms.HiddenInput(),
            'version': forms.TextInput(attrs={'placeholder': '1.2.3'}),
            'compatible': forms.SelectMultiple(),
            'document': forms.ClearableFileInput(attrs={'accept': '.tar.gz,.tar.bz2,.tar.xz,.zip', 'class': 'btn btn-default btn-file'}),
            'changelog': forms.Textarea(attrs={'placeholder': 'Write changelog about this version'}),
        }


class FileEditForm(forms.ModelForm):
    class Meta:
        model = FilesModel
        fields = ('version', 'compatible', 'document', 'changelog', 'author', 'project')
        widgets = {
            'author': forms.HiddenInput(),
            'version': forms.HiddenInput(),
            'project': forms.HiddenInput(),
            'document': forms.HiddenInput(),
            'compatible': forms.SelectMultiple(),
            'changelog': forms.Textarea(attrs={'placeholder': 'Write changelog about this version'}),
        }


class ScreenshotForm(forms.ModelForm):
    class Meta:
        model = ScreenshotsModel
        fields = ('screenshot',)
        widgets = {
            'screenshot': forms.ClearableFileInput(attrs={'multiple': True, 'accept': '.png', 'class': 'btn btn-default btn-file'}),
        }
