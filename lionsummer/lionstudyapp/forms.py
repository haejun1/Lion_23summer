from django import forms
from .models import Lionstudyapp


class LionstudyappForm(forms.ModelForm):
    class Meta:
        model = Lionstudyapp
        fields = ["title", "content"]
