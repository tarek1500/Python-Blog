import os
from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from blog.models import Category
from .forms import *
from django.contrib.admin.views.decorators import staff_member_required

# Create your views here.

# Dashboard section
@staff_member_required
def dashboardIndex(request):
	return render(request, 'dashboard/index.html')
# End Dashboard section

# Users section
@staff_member_required
def userIndex(request):
	users = User.objects.all()

	return render(request, 'user/index.html', { 'users': users })

@staff_member_required
def userCreate(request):
	if request.method == 'POST':
		form = CustomUserCreationForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/user')
	else:
		form = CustomUserCreationForm()

	return render(request, 'user/create.html', { 'form': form })

@staff_member_required
def userShow(request, id):
	user = User.objects.get(id = id)

	return render(request, 'user/show.html', { 'user': user })

@staff_member_required
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

@staff_member_required
def userDelete(request, id):
	user = User.objects.get(id = id)
	user.delete()

	return HttpResponseRedirect('/cp/user')
# End Users section

# Categories section
@staff_member_required
def categoryIndex(request):
	categories = Category.objects.all()

	return render(request, 'category/index.html', { 'categories': categories })

@staff_member_required
def categoryCreate(request):
	if request.method == 'POST':
		form = CategoryForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/category')
	else:
		form = CategoryForm()

	return render(request, 'category/create.html', { 'form': form })

@staff_member_required
def categoryShow(request, id):
	category = Category.objects.get(id = id)

	return render(request, 'category/show.html', { 'category': category })

@staff_member_required
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

@staff_member_required
def categoryDelete(request, id):
	category = Category.objects.get(id = id)
	category.delete()

	return HttpResponseRedirect('/cp/category')
# End Categories section

# Tags section
@staff_member_required
def tagIndex(request):
	tags = Tag.objects.all()

	return render(request, 'tag/index.html', { 'tags': tags })

@staff_member_required
def tagCreate(request):
	if request.method == 'POST':
		form = TagForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/tag')
	else:
		form = TagForm()

	return render(request, 'tag/create.html', { 'form': form })

@staff_member_required
def tagShow(request, id):
	tag = Tag.objects.get(id = id)

	return render(request, 'tag/show.html', { 'tag': tag })

@staff_member_required
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

@staff_member_required
def tagDelete(request, id):
	tag = Tag.objects.get(id = id)
	tag.delete()

	return HttpResponseRedirect('/cp/tag')
# End Tags section

# Posts section
@staff_member_required
def postIndex(request):
	posts = Post.objects.all()

	return render(request, 'post/index.html', { 'posts': posts })

@staff_member_required
def postCreate(request):
	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/post')
	else:
		form = PostForm()

	return render(request, 'post/create.html', { 'form': form })

@staff_member_required
def postShow(request, id):
	post = Post.objects.get(id = id)

	return render(request, 'post/show.html', { 'post': post })

@staff_member_required
def postEdit(request, id):
	post = Post.objects.get(id = id)

	if request.method == 'POST':
		form = PostForm(request.POST, request.FILES, instance = post)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/post')
	else:
		form = PostForm(instance = post)

	return render(request, 'post/create.html', { 'form': form })

@staff_member_required
def postDelete(request, id):
	post = Post.objects.get(id = id)

	if os.path.isfile(post.image.path):
		os.remove(post.image.path)

	post.delete()

	return HttpResponseRedirect('/cp/post')
# End Posts section

# Comments section
@staff_member_required
def commentIndex(request):
	comments = Comment.objects.all()

	return render(request, 'comment/index.html', { 'comments': comments })

@staff_member_required
def commentCreate(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/comment')
	else:
		form = CommentForm()

	return render(request, 'comment/create.html', { 'form': form })

@staff_member_required
def commentShow(request, id):
	comment = Comment.objects.get(id = id)

	return render(request, 'comment/show.html', { 'comment': comment })

@staff_member_required
def commentEdit(request, id):
	comment = Comment.objects.get(id = id)

	if request.method == 'POST':
		form = CommentForm(request.POST, instance = comment)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/comment')
	else:
		form = CommentForm(instance = comment)

	return render(request, 'comment/create.html', { 'form': form })

@staff_member_required
def commentDelete(request, id):
	comment = Comment.objects.get(id = id)
	comment.delete()

	return HttpResponseRedirect('/cp/comment')
# End Comments section

# Words section
@staff_member_required
def wordIndex(request):
	words = Word.objects.all()

	return render(request, 'word/index.html', { 'words': words })

@staff_member_required
def wordCreate(request):
	if request.method == 'POST':
		form = WordForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/word')
	else:
		form = WordForm()

	return render(request, 'word/create.html', { 'form': form })

@staff_member_required
def wordShow(request, id):
	word = Word.objects.get(id = id)

	return render(request, 'word/show.html', { 'word': word })

@staff_member_required
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

@staff_member_required
def wordDelete(request, id):
	word = Word.objects.get(id = id)
	word.delete()

	return HttpResponseRedirect('/cp/word')
# End Words section

# Likes section
@staff_member_required
def likeIndex(request):
	likes = Like.objects.all()

	return render(request, 'like/index.html', { 'likes': likes })

@staff_member_required
def likeCreate(request):
	if request.method == 'POST':
		form = LikeForm(request.POST)

		if form.is_valid():
			form.save()

			return HttpResponseRedirect('/cp/like')
	else:
		form = LikeForm()

	return render(request, 'like/create.html', { 'form': form })

@staff_member_required
def likeShow(request, id):
	like = Like.objects.get(id = id)

	return render(request, 'like/show.html', { 'like': like })

@staff_member_required
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

@staff_member_required
def likeDelete(request, id):
	like = Like.objects.get(id = id)
	like.delete()

	return HttpResponseRedirect('/cp/like')
# End Likes section