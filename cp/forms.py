from django.utils.translation import ugettext, ugettext_lazy as _
from django import forms
from blog.models import *
from django.contrib.auth.forms import UserCreationForm

class CategoryForm(forms.ModelForm):
	class Meta:
		model = Category
		fields = ['name', 'subscribe']

class CustomUserCreationForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['is_superuser', 'is_staff', 'is_active']

class TagForm(forms.ModelForm):
	class Meta:
		model = Tag
		fields = ['name']

class PostForm(forms.ModelForm):
	class Meta:
		model = Post
		fields = ['title', 'body', 'author', 'tag', 'category', 'image']

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content', 'user', 'post']

class WordForm(forms.ModelForm):
	class Meta:
		model = Word
		fields = ['name']

class LikeForm(forms.ModelForm):
	class Meta:
		model = Like
		fields = ['like', 'user', 'post']