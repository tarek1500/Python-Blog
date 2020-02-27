from django.contrib import admin
from blog.models import Category, Tag,Post,Comment,Word

admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
# admin.site.register(Reply)
#admin.site.register(Likes)
#admin.site.register(Word)
# Register your models here.
