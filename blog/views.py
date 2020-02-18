from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import Word, Reply
from blog.forms import WordForm, ReplyForm

# Create your views here.

# Words section
def wordIndex(request):
	words = Word.objects.all()
	context = { 'words': words }

	return render(request, 'blog/word/index.html', context)

def wordCreate(request):
	if request.method == 'POST':
		stForm = WordForm(request.POST)

		if stForm.is_valid():
			stForm.save()

			return HttpResponseRedirect('/blog/word')
	else:
		stForm = WordForm()
		context = { 'form': stForm }

		return render(request, 'blog/word/create.html', context)

def wordShow(request, id):
	word = Word.objects.get(id = id)
	context = { 'word': word }

	return render(request, 'blog/word/show.html', context)

def wordEdit(request, id):
	word = Word.objects.get(id = id)

	if request.method == 'POST':
		stForm = WordForm(request.POST, instance = word)

		if stForm.is_valid():
			stForm.save()

			return HttpResponseRedirect('/blog/word')
	else:
		stForm = WordForm(instance = word)
		context = { 'form': stForm }

		return render(request, 'blog/word/create.html', context)

def wordDelete(request, id):
	word = Word.objects.get(id = id)
	word.delete()

	return HttpResponseRedirect('/blog/word')
# End Words section

# Replies section
def replyIndex(request):
	replies = Reply.objects.all()
	context = { 'replies': replies }

	return render(request, 'blog/reply/index.html', context)

def replyCreate(request):
	if request.method == 'POST':
		stForm = ReplyForm(request.POST)

		if stForm.is_valid():
			stForm.save()

			return HttpResponseRedirect('/blog/reply')
	else:
		stForm = ReplyForm()
		context = { 'form': stForm }

		return render(request, 'blog/reply/create.html', context)

def replyShow(request, id):
	reply = Reply.objects.get(id = id)
	context = { 'reply': reply }

	return render(request, 'blog/reply/show.html', context)

def replyEdit(request, id):
	reply = Reply.objects.get(id = id)

	if request.method == 'POST':
		stForm = ReplyForm(request.POST, instance = reply)

		if stForm.is_valid():
			stForm.save()

			return HttpResponseRedirect('/blog/reply')
	else:
		stForm = ReplyForm(instance = reply)
		context = { 'form': stForm }

		return render(request, 'blog/reply/create.html', context)

def replyDelete(request, id):
	reply = Reply.objects.get(id = id)
	reply.delete()

	return HttpResponseRedirect('/blog/reply')
# End Replies section