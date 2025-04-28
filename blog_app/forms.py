from django import forms
from blog_app.models import Comment, Post



class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    #email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False, widget=forms.Textarea)

class CommentForm(forms.ModelForm): # форма будет создана автоматически на основе модели
    class Meta:
        model = Comment # форма связана с моделью Comment
        fields = ['name', 'email', 'body'] # Список полей модели, которые должны быть включены в форму


class SearchForm(forms.Form):
    query = forms.CharField()