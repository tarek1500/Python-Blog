from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from blog.models import Category ,Post , Comment , Like, Tag
from .forms import *
from django.db.models import Q
from django.contrib.auth.decorators import login_required

def landpage(request):
    category = Category.objects.all()

    if request.user.is_authenticated:
        subscribed = category.filter(subscribe = request.user)
        post = Post.objects.filter(category__in = subscribed).order_by('-created_at')[:5]

        context = {'category': category, 'post': post, 'sub': subscribed}
    else:
        post = Post.objects.all().order_by('-created_at')[:5]
        context = {'category': category, 'post': post}

    return render(request, 'index.html', context)

@login_required
def subscribe(request, num):
    category = Category.objects.get(id = num)

    if request.POST.get('subscribe') == '0':
        category.subscribe.remove(request.user)
    else:
        category.subscribe.add(request.user)

    return HttpResponseRedirect('/')

def categoryPosts(request, cat):
    posts = Post.objects.filter(category = cat).order_by('-created_at')
    context = {'posts': posts}

    return render(request, 'posts.html', context)

@login_required
def searchPost(request):
    queryset= request.GET.get("query")
    if queryset:
        queryset_list=Post.objects.filter(Q(title__icontains=queryset)| Q(tag__tag__icontains=queryset))
        context = {'posts':queryset_list}
        return render(request,'posts.html',context)
    else:
        return HttpResponse ("<h1> There is nothing </h1>")

@login_required
def showPostsByTags(request, id):
    tag = Tag.objects.get(id = id)
    posts = Post.objects.filter(tag = tag).order_by('-created_at')
    context = {'posts': posts}

    return render(request, 'posts.html', context)

def showpost(request, num):
    is_liked=None
    post = Post.objects.get(id=num)
    like = Like.objects.filter(post_id=post)

    post_likes = like.filter(like = True).count()
    post_dislikes = like.filter(like = False).count()

    if request.user.is_authenticated:
        like = Like.objects.filter(post_id=post, userId=request.user)

        if like.exists():
            if like.get().like == True:
                is_liked=True
            else:
                is_liked=False

    comments=Comment.objects.filter(post_id=post.id , reply=None).order_by('-id')
    if request.method =='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comment.objects.get(id=reply_id)
            comment=Comment.objects.create(post_id=post,user_id=request.user , content=content , reply=comment_qs)
            comment.save()
            comment_form = CommentForm()
    else : 
        comment_form=CommentForm()  
    context ={'post':post, 'is_liked': is_liked, 'post_likes': post_likes, 'post_dislikes': post_dislikes, 'comments':comments , 'comment_form':comment_form}
    return render(request,'onePost.html',context)

@login_required
def like(request,num):
    if not Like.objects.filter(post_id=num, userId=request.user.id).exists():
        post = Post.objects.get(id=num)

        if request.POST.get('like') == '1':
            Like.objects.create(post_id=post, userId=request.user, like = True)
        else:
            Like.objects.create(post_id=post, userId=request.user, like = False)

        like = Like.objects.filter(post_id=post, like = 0)

        if like.count() >= 10:
            like.delete()
            post.delete()

            return HttpResponseRedirect('/')

    return HttpResponseRedirect('/showpost/' + num)

def about(request):
    return render(request, 'about.html', {'title': 'About'})