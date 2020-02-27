from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

def stringify(self):
	return self.first_name + ' ' + self.last_name

User.add_to_class('__str__', stringify)

class Category(models.Model):
	name = models.CharField(max_length = 100)
	subscribe = models.ManyToManyField(User, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

class Tag(models.Model):
	name = models.CharField(max_length = 200, unique = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.name

class Post(models.Model):
	title = models.CharField(max_length = 200, unique = True)
	body = models.TextField()
	author = models.ForeignKey(User, on_delete = models.CASCADE)
	tag = models.ManyToManyField(Tag, blank = True)
	category = models.ForeignKey(Category, on_delete = models.CASCADE)
	image = models.ImageField(null = True, blank = True)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

	def __str__(self):
		return self.title
  
  def snippet(self):
    return self.body[:200] + "..."

class Comment(models.Model):
	content = models.TextField()
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
  reply = models.ForeignKey('Comments', null = True, related_name = 'replies', on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now=True)
	
	def __str__(self):
		return self.content
  
  def removeWords(self):
    words = Word.objects.all()

    for word in words:
        self.content = self.content.replace(word.name, '*' * len(word.name))

    return self.content

# class Reply(models.Model):
# 	content = models.TextField()
# 	comment = models.ForeignKey(Comment, on_delete = models.CASCADE)
# 	user = models.ForeignKey(User, on_delete = models.CASCADE)
# 	created_at = models.DateTimeField(auto_now_add = True)
# 	updated_at = models.DateTimeField(auto_now = True)

class Word(models.Model):
	name = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Like(models.Model):
	like = models.BooleanField()
	post = models.ForeignKey(Post, on_delete = models.CASCADE)
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
