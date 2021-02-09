from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    img = forms.ImageField(label="Image", required=False)

    class Meta:
        model = Post
        fields = ('author', 'title', 'content', 'img')

        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'})
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text')

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            'content': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'})
        }
