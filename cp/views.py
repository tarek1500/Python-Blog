import os
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from blog.models import Category
from .forms import *

# Create your views here.

# Dashboard section
def dashboardIndex(request):
	return render(request, 'dashboard/index.html')
# End Dashboard section

# Users section
def userIndex(request):
	users = User.objects.all()

	return render(request, 'user/index.html', { 'users': users })

def userCreate(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/user')
	else:
		form = CustomUserCreationForm()

	return render(request, 'user/create.html', { 'form': form })

def userShow(request, id):
	user = User.objects.get(id = id)

	return render(request, 'user/show.html', { 'user': user })

def userEdit(request, id):
	user = User.objects.get(id = id)

	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST, instance = user)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/user')
	else:
		form = CustomUserCreationForm(instance = user)

	return render(request, 'user/create.html', { 'form': form })

def userDelete(request, id):
	user = User.objects.get(id = id)
	user.delete()

	return HttpResponseRedirect('/cp/user')
# End Users section

# Categories section
def categoryIndex(request):
	categories = Category.objects.all()

	return render(request, 'category/index.html', { 'categories': categories })

def categoryCreate(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/category')
	else:
		form = CategoryForm()

	return render(request, 'category/create.html', { 'form': form })

def categoryShow(request, id):
	category = Category.objects.get(id = id)

	return render(request, 'category/show.html', { 'category': category })

def categoryEdit(request, id):
	category = Category.objects.get(id = id)

	if request.method == 'POST':
		form = CategoryForm(request.POST, instance = category)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/category')
	else:
		form = CategoryForm(instance = category)

	return render(request, 'category/create.html', { 'form': form })

def categoryDelete(request, id):
	category = Category.objects.get(id = id)
	category.delete()

	return HttpResponseRedirect('/cp/category')
# End Categories section

# Tags section
def tagIndex(request):
	tags = Tag.objects.all()

	return render(request, 'tag/index.html', { 'tags': tags })

def tagCreate(request):
	if request.method == 'POST':
		form = TagForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/tag')
	else:
		form = TagForm()

	return render(request, 'tag/create.html', { 'form': form })

def tagShow(request, id):
	tag = Tag.objects.get(id = id)

	return render(request, 'tag/show.html', { 'tag': tag })

def tagEdit(request, id):
	tag = Tag.objects.get(id = id)

	if request.method == 'POST':
		form = TagForm(request.POST, instance = tag)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/tag')
	else:
		form = TagForm(instance = tag)

	return render(request, 'tag/create.html', { 'form': form })

def tagDelete(request, id):
	tag = Tag.objects.get(id = id)
	tag.delete()

	return HttpResponseRedirect('/cp/tag')
# End Tags section

# Posts section
def postIndex(request):
	posts = Post.objects.all()

	return render(request, 'post/index.html', { 'posts': posts })

def postCreate(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/post')
	else:
		form = PostForm()

	return render(request, 'post/create.html', { 'form': form })

def postShow(request, id):
	post = Post.objects.get(id = id)

	return render(request, 'post/show.html', { 'post': post })

def postEdit(request, id):
	post = Post.objects.get(id = id)

	if request.method == 'POST':
		form = PostForm(request.POST, instance = post)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/post')
	else:
		form = PostForm(instance = post)

	return render(request, 'post/create.html', { 'form': form })

def postDelete(request, id):
	post = Post.objects.get(id = id)

	if os.path.isfile(post.image.path):
		os.remove(post.image.path)

	post.delete()

	return HttpResponseRedirect('/cp/post')
# End Posts section

# Comments section
def commentIndex(request):
	comments = Comment.objects.all()

	return render(request, 'comment/index.html', { 'comments': comments })

def commentCreate(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/comment')
	else:
		form = CommentForm()

	return render(request, 'comment/create.html', { 'form': form })

def commentShow(request, id):
	comment = Comment.objects.get(id = id)

	return render(request, 'comment/show.html', { 'comment': comment })

def commentEdit(request, id):
	comment = Comment.objects.get(id = id)

	if request.method == 'POST':
		form = commentForm(request.POST, instance = comment)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/comment')
	else:
		form = CommentForm(instance = comment)

	return render(request, 'comment/create.html', { 'form': form })

def commentDelete(request, id):
	comment = Comment.objects.get(id = id)
	comment.delete()

	return HttpResponseRedirect('/cp/comment')
# End Comments section

# Replies section
def replyIndex(request):
	replies = Reply.objects.all()

	return render(request, 'reply/index.html', { 'replies': replies })

def replyCreate(request):
	if request.method == 'POST':
		form = ReplyForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/reply')
	else:
		form = ReplyForm()

	return render(request, 'reply/create.html', { 'form': form })

def replyShow(request, id):
	reply = Reply.objects.get(id = id)

	return render(request, 'reply/show.html', { 'reply': reply })

def replyEdit(request, id):
	reply = Reply.objects.get(id = id)

	if request.method == 'POST':
		form = ReplyForm(request.POST, instance = reply)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/reply')
	else:
		form = ReplyForm(instance = reply)

	return render(request, 'reply/create.html', { 'form': form })

def replyDelete(request, id):
	reply = Reply.objects.get(id = id)
	reply.delete()

	return HttpResponseRedirect('/cp/reply')
# End Replies section

# Words section
def wordIndex(request):
	words = Word.objects.all()

	return render(request, 'word/index.html', { 'words': words })

def wordCreate(request):
	if request.method == 'POST':
		form = WordForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/word')
	else:
		form = WordForm()

	return render(request, 'word/create.html', { 'form': form })

def wordShow(request, id):
	word = Word.objects.get(id = id)

	return render(request, 'word/show.html', { 'word': word })

def wordEdit(request, id):
	word = Word.objects.get(id = id)

	if request.method == 'POST':
		form = WordForm(request.POST, instance = word)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/word')
	else:
		form = WordForm(instance = word)

	return render(request, 'word/create.html', { 'form': form })

def wordDelete(request, id):
	word = Word.objects.get(id = id)
	word.delete()

	return HttpResponseRedirect('/cp/word')
# End Words section

# Likes section
def likeIndex(request):
	likes = Like.objects.all()

	return render(request, 'like/index.html', { 'likes': likes })

def likeCreate(request):
	if request.method == 'POST':
		form = LikeForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/like')
	else:
		form = LikeForm()

	return render(request, 'like/create.html', { 'form': form })

def likeShow(request, id):
	like = Like.objects.get(id = id)

	return render(request, 'like/show.html', { 'like': like })

def likeEdit(request, id):
	like = Like.objects.get(id = id)

	if request.method == 'POST':
		form = LikeForm(request.POST, instance = like)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/like')
	else:
		form = LikeForm(instance = like)

	return render(request, 'like/create.html', { 'form': form })

def likeDelete(request, id):
	like = Like.objects.get(id = id)
	like.delete()

	return HttpResponseRedirect('/cp/like')
# End Likes section