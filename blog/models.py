from django.db import models

# Create your models here.

class Word(models.Model):
	name = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)

class Reply(models.Model):
	content = models.CharField(max_length = 200)
	# comment = models.ForeignKey(Comment, on_delete = models.DO_NOTHING)
	# user = models.ForeignKey(User, on_delete = models.DO_NOTHING)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)