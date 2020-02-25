from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Category(models.Model):
    categoryName = models.CharField(max_length=200)
    subscribe = models.ManyToManyField(User)
    def __str__(self):
	    return self.categoryName


class Tags(models.Model):
    tag =models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.tag

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    post_image = models.ImageField(upload_to='images/',null=True,blank=True)
    created_on = models.DateTimeField(auto_now_add=True) 
    tags = models.ManyToManyField(Tags)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    category_name = models.ForeignKey(Category,on_delete= models.CASCADE) 
    updated_on = models.DateTimeField(auto_now= True)       
    #  slug = models.SlugField(max_length=200, unique=True)
    def __str__(self):
	    return self.title
    
    def snippet(self):
        return self.body[:200]+"....."


class Comments(models.Model):
    user_id=models.ForeignKey(User,on_delete= models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete= models.CASCADE)
    content=models.TextField()
    reply=models.ForeignKey('Comments',null=True,related_name='replies',on_delete= models.CASCADE)
    commentTime= models.DateTimeField(auto_now_add=True) 
    updated_on = models.DateTimeField(auto_now= True) 
    def __str__(self):
	    return self.content


# class Reply(models.Model):
#     comment_id=models.ForeignKey(Comments,on_delete=models.CASCADE)
#     userId= models.ForeignKey(User,on_delete= models.CASCADE)
#     replyBody=models.TextField()
#     replyTime= models.DateTimeField(auto_now_add=True) 
#     updated_on = models.DateTimeField(auto_now= True) 



class Likes(models.Model):
    like=models.BooleanField()
    userId=models.ForeignKey(User,on_delete= models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete= models.CASCADE)


class Word(models.Model):
	name = models.CharField(max_length = 100)
	created_at = models.DateTimeField(auto_now_add = True)
	updated_at = models.DateTimeField(auto_now = True)
