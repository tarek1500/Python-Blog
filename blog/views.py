from django.shortcuts import render

# Create your views here.
from django.contrib.sites import requests
from django.shortcuts import render , render_to_response, redirect,  
from django.http import HttpResponse, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import auth
from forms import CommentForm
from models import post , comment ,category
from django.contrib.auth.models import User
# Create your views here.


def homePosts (request):
    posts = post.objects.all().order_by('-post_date')
    categories = category.objects.all()

    paginator = Paginator(posts , 1 )
    page = request.GET.get('page')
    try:
        posts_data = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        posts_data = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        posts_data = paginator.page(paginator.num_pages)
    current_user = request.user
    subscribed_cats = category.objects.filter(user = current_user.id)
    context = {'posts': posts_data , 'categories': categories, "subscribedCats": subscribed_cats }
    return render(request , 'main/home.html' , context)



def subscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = category.objects.get(id = cat_id)
    subscribed_cats.user.add(current_user)
    #confirmSubscription(current_user.email,subscribed_cats.cat_title)
    return HttpResponseRedirect('/home')

def unsubscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = category.objects.get(id = cat_id)
    subscribed_cats.user.remove(current_user)
    return HttpResponseRedirect('/home')


def PostDetails(request, id):
    #return HttpResponse('details of %s' %id)
    postDetails =  get_object_or_404(post, id = id)
    categoryDetails = postDetails.post_cat_id
    #comments = comment.objects.filter(comment_post_id = postDetails.id)
    form = CommentForm(request.POST or None)

    context = {'postDetails': postDetails, 'postCat': categoryDetails, 'form': form}
    return render(request, 'post/postDetails.html', context )

def addComment(request, postID):
    print postID, request.user
    if request.method == 'POST':
	    comment = CommentForm(request.POST, request.FILES)
	    if comment.is_valid():
		    comment = comment.save(commit=False)
            comment.comment_body = censor(comment.comment_body)
            comment.post = post.objects.get(id = postID)
            #comment.User = User.objects.get(id = request.user.id)
            comment.comment_user_id_id = request.user.id
            comment.comment_post_id_id = postID

            comment.save()
            return redirect(request.path)
    return HttpResponseRedirect("/main/"+postID+"/post")

def addReply(request, postID, commentID):
    if request.method == 'POST':
	    reply = CommentForm(request.POST, request.FILES)
	    if reply.is_valid():
		    reply = reply.save(commit=False)
            #reply.comment_body = censor(reply.comment_body)
            reply.post = post.objects.get(id = postID)
            #comment.User = User.objects.get(id = request.user.id)
            reply.comment_user_id_id = request.user.id
            reply.comment_post_id_id = postID
            reply.reply_comment_id = comment.objects.get(id = commentID)

            reply.save()
            return redirect(request.path)
    return HttpResponseRedirect("/main/"+postID+"/post")
