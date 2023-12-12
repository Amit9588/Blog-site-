from django import forms
from BlogApp.models import Post,Comments

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = (
            'author', 'title', 'text'
        )
        widget= {

            'title':forms.TextInput(attrs={'class':'textinputclass'}),
            'text' :forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})              
            }
    

class CommentsForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author','text')

        widgets = {

            'author':forms.TextInput(attrs={'class':'textinputclass'}),
            'text' :forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
        }
    