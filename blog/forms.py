from django import forms
from blog.models import Word, Reply

class WordForm(forms.ModelForm):
	class Meta:
		model = Word
		fields = ('name',)
		widgets = {
			'name': forms.TextInput(attrs = { 'class': 'form-control' }),
		}

class ReplyForm(forms.ModelForm):
	class Meta:
		model = Reply
		fields = ('content',)
		widgets = {
			'content': forms.TextInput(attrs = { 'class': 'form-control' }),
			'comment': forms.TextInput(attrs = { 'class': 'form-control' }),
			'user': forms.TextInput(attrs = { 'class': 'form-control' }),
		}