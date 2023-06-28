from django import forms
from .models import Lionstudyapp, Comment


class LionstudyappForm(forms.ModelForm):
    class Meta:
        model = Lionstudyapp
        fields = ["title", "content"]


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
