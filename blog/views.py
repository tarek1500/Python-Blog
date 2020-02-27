from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from blog.models import Category ,Post , Comments , Likes, Tags
from .forms import *
from django.db.models import Q

def landpage(request):
    category = Category.objects.all()

    if request.user.is_authenticated:
        subscribed = category.filter(subscribe = request.user)
        post = Post.objects.filter(category_name__in = subscribed).order_by('-created_on')[:5]

        context = {'category': category, 'post': post, 'sub': subscribed}
    else:
        post = Post.objects.all().order_by('-created_on')[:5]
        context = {'category': category, 'post': post}

    return render(request, 'index.html', context)


def subscribe(request, num):
    category = Category.objects.get(id = num)

    if request.POST.get('subscribe') == '0':
        category.subscribe.remove(request.user)
    else:
        category.subscribe.add(request.user)

    return HttpResponseRedirect('/blog/landpage')

def categoryPosts(request, cat):
    posts = Post.objects.filter(category_name = cat).order_by('-created_on')
    context = {'posts': posts}

    return render(request, 'blog/posts.html', context)

def searchPost(request):
    queryset= request.GET.get("query")
    if queryset:
        queryset_list=Post.objects.filter(Q(title__icontains=queryset)| Q(tags__tag__icontains=queryset))
        context = {'posts':queryset_list}
        return render(request,'blog/posts.html',context)

    else:
        return HttpResponse ("<h1> There is nothing </h1>")

def showPostsByTags(request, id):
    tag = Tags.objects.get(id = id)
    posts = Post.objects.filter(tags = tag).order_by('-created_on')
    context = {'posts': posts}

    return render(request, 'blog/posts.html', context)

def showpost(request, num):
    is_liked=None
    post = Post.objects.get(id=num)
    like = Likes.objects.filter(post_id=post)

    post_likes = like.filter(like = True).count()
    post_dislikes = like.filter(like = False).count()

    if request.user.is_authenticated:
        like = Likes.objects.filter(post_id=post, userId=request.user)

        if like.exists():
            if like.get().like == True:
                is_liked=True
            else:
                is_liked=False

    comments=Comments.objects.filter(post_id=post.id , reply=None).order_by('-id')
    if request.method =='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            content=request.POST.get('content')
            reply_id=request.POST.get('comment_id')
            comment_qs=None
            if reply_id:
                comment_qs=Comments.objects.get(id=reply_id)
            comment=Comments.objects.create(post_id=post,user_id=request.user , content=content , reply=comment_qs)
            comment.save()
            comment_form = CommentForm()
        

            # return HttpResponseRedirect('/blog/view/showpost/' + num)
    else : 
        comment_form=CommentForm()  
    context ={'post':post, 'is_liked': is_liked, 'post_likes': post_likes, 'post_dislikes': post_dislikes, 'comments':comments , 'comment_form':comment_form}
    return render(request,'onePost.html',context)

def like(request,num):
    if not Likes.objects.filter(post_id=num, userId=request.user.id).exists():
        post = Post.objects.get(id=num)

        if request.POST.get('like') == '1':
            Likes.objects.create(post_id=post, userId=request.user, like = True)
        else:
            Likes.objects.create(post_id=post, userId=request.user, like = False)

        like = Likes.objects.filter(post_id=post, like = 0)

        if like.count() >= 10:
            like.delete()
            post.delete()

            return HttpResponseRedirect('/blog/landpage/')

    return HttpResponseRedirect('/blog/showpost/' + num)
