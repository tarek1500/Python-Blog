from django.urls import path
from . import views

app_name = 'cp'

urlpatterns = [
	path('', views.dashboardIndex, name = 'dashboard-index'),

	path('user', views.userIndex, name = 'user-index'),
	path('user/create', views.userCreate, name = 'user-create'),
	path('user/show/<id>', views.userShow, name = 'user-show'),
	path('user/edit/<id>', views.userEdit, name = 'user-edit'),
	path('user/delete/<id>', views.userDelete, name = 'user-delete'),

	path('category', views.categoryIndex, name = 'category-index'),
	path('category/create', views.categoryCreate, name = 'category-create'),
	path('category/show/<id>', views.categoryShow, name = 'category-show'),
	path('category/edit/<id>', views.categoryEdit, name = 'category-edit'),
	path('category/delete/<id>', views.categoryDelete, name = 'category-delete'),

	path('tag', views.tagIndex, name = 'tag-index'),
	path('tag/create', views.tagCreate, name = 'tag-create'),
	path('tag/show/<id>', views.tagShow, name = 'tag-show'),
	path('tag/edit/<id>', views.tagEdit, name = 'tag-edit'),
	path('tag/delete/<id>', views.tagDelete, name = 'tag-delete'),

	path('post', views.postIndex, name = 'post-index'),
	path('post/create', views.postCreate, name = 'post-create'),
	path('post/show/<id>', views.postShow, name = 'post-show'),
	path('post/edit/<id>', views.postEdit, name = 'post-edit'),
	path('post/delete/<id>', views.postDelete, name = 'post-delete'),

	path('comment', views.commentIndex, name = 'comment-index'),
	path('comment/create', views.commentCreate, name = 'comment-create'),
	path('comment/show/<id>', views.commentShow, name = 'comment-show'),
	path('comment/edit/<id>', views.commentEdit, name = 'comment-edit'),
	path('comment/delete/<id>', views.commentDelete, name = 'comment-delete'),

	path('word', views.wordIndex, name = 'word-index'),
	path('word/create', views.wordCreate, name = 'word-create'),
	path('word/show/<id>', views.wordShow, name = 'word-show'),
	path('word/edit/<id>', views.wordEdit, name = 'word-edit'),
	path('word/delete/<id>', views.wordDelete, name = 'word-delete'),

	path('like', views.likeIndex, name = 'like-index'),
	path('like/create', views.likeCreate, name = 'like-create'),
	path('like/show/<id>', views.likeShow, name = 'like-show'),
	path('like/edit/<id>', views.likeEdit, name = 'like-edit'),
	path('like/delete/<id>', views.likeDelete, name = 'like-delete')
]