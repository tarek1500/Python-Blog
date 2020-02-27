from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    content=forms.CharField(label="",widget=forms.Textarea(attrs={'class':'form-control', 'placeholder': 'write here....' , 'rows':'5','cols':'55'}))
    class Meta:
        model=Comment
        fields=('content',)