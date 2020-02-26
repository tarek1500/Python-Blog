from django.contrib import admin
from blog.models import Category, Tags,Post,Comments,Word

admin.site.register(Category)
admin.site.register(Tags)
admin.site.register(Post)
admin.site.register(Comments)
# admin.site.register(Reply)
# admin.site.register(Likes)
admin.site.register(Word)
# Register your models here.