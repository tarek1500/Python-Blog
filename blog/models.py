from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class  Category(models.Model):
    categoryName =models.CharField(max_length=50)
    subscribe = models.ManyToManyField(User, blank=true , null=true)

class Post(models.Model):
    postId = models.IntegerField()
    title = models.CharField(max_length=200, unique=True)
    body = models.TextField()
    post_image = models.ImageField(upload_to='./static/images'null=true,blank=true)
    created_on = models.DateTimeField(auto_now_add=True) 
    tags = models.ManyToManyField(Tags,blank=true , null=true)
    author = models..ForeignKey(User, on_delete= models.CASCADE)
    category_name = models.ForeignKey(Category,on_delete= models.CASCADE) 
    updated_on = models.DateTimeField(auto_now= True)       
    #  slug = models.SlugField(max_length=200, unique=True)


class Comments(models.Model):
    user_id=models.ForeignKey(User,on_delete= models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete= models.CASCADE)
    commentId=models.IntegerField()
    content=models.TextField()
    commentTime= models.DateTimeField(auto_now_add=True) 
    updated_on = models.DateTimeField(auto_now= True) 


class Reply(models.Model):
    comment_id=models.ForeignKey(Comments,on_delete=models.CASCADE)
    userId= models.ForeignKey(User,on_delete= models.CASCADE)
    replyBody=models.TextField()
    replyTime= models.DateTimeField(auto_now_add=True) 
    updated_on = models.DateTimeField(auto_now= True) 



class Tags(models.Model):
    tag=models.CharField(max_length=200, unique=True)

class Likes(models.Model):
    like=models.BooleanField()
    userId=models.ForeignKey(User,on_delete= models.CASCADE)
    post_id=models.ForeignKey(Post,on_delete= models.CASCADE)









