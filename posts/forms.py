from django import forms
from .models import Post,Author

class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title','description','author','image','slug']

class AuthorModelForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ['user','author_email','cellphone_num']

