from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from blog.models import Category ,Post , Comments 
from .forms import *
from django.db.models import Q

# Create your views here.
def landpage(request):
    category = Category.objects.all()
    post= Post.objects.all().order_by('-created_on')[:5]
    current_user=request.user
    subscribed=Category.objects.filter( subscribe=current_user.id )
    context ={'category':category , 'post':post , 'sub':subscribed}
    return render(request, 'blog/landpage.html', context)


def categoryPosts(request,cat):
    posts=Post.objects.filter(category_name=cat).order_by('-created_on')
    context = {'posts':posts}
    return render(request,'blog/posts.html',context)

def unsubscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = Category.objects.get(id = cat_id)
    subscribed_cats.user.remove(current_user)
    return HttpResponseRedirect('blog/landpage')

def subscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = Category.objects.get(id = cat_id)
    subscribed_cats.user.add(current_user)
    #confirmSubscription(current_user.email,subscribed_cats.cat_title)
    return HttpResponseRedirect('blog/landpage')

def searchPost(request):
    queryset= request.GET.get("query")
    if queryset:
        queryset_list=Post.objects.filter(Q(title__icontains=queryset)| Q(tags__tag__icontains=queryset)).distinct()
        context = {'posts':queryset_list}
        return render(request,'blog/posts.html',context)

    else:
        return HttpResponse ("<h1> There is nothing </h1>")

def showpost(request,num):
    post = Post.objects.get(id=num)
    # is_liked=False
    # if post.likes.filter(id=request.user.id).exists():
    #     post.likes.remove(request.user)
    #     is_liked=False
    # else:
    #     # post.likes.add(request.user)
    #     is_liked=True
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
    context ={'post':post, 'comments':comments , 'comment_form':comment_form}
    return render(request,'blog/onePost.html',context)

# def Like(request,num):
#     post=Post.objects.get(id=num)
#     post.likes.add(request.user)
#     return HttpResponseRedirect('blog/onePost.html')


# def showPostsByTags(request,num):
#     post