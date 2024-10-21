from django import forms
from . import models

class FilesForm(forms.ModelForm):
    class Meta:
        model = models.VotableFiles
        fields = "__all__"