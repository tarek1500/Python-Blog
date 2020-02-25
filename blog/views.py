from django.shortcuts import render
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
        queryset_list=Post.objects.filter(Q(title__icontains=queryset)| Q(tags__tag__icontains=queryset))
        context = {'posts':queryset_list}
        return render(request,'blog/posts.html',context)

    else:
        return HttpResponse ("<h1> There is nothing </h1>")

def showpost(request,num):
    post = Post.objects.get(id=num)
    comments=Comments.objects.filter(post_id=post.id).order_by('-id')
    if request.method=='POST':
        comment_form=CommentForm(request.POST or None)
        if comment_form.is_valid():
            instance=comment_form.save(commit=False)
            # if request.method=='POST':
            #     reply=CommentForm(request.POST or None)
            #     if reply.is_valid:
            #         reply= reply.save(commit=False)
            #         reply.post_id= post
            #         reply.user_id=request.user
            #         reply.reply= Comments.objects.get(id=instance.id)
            #         reply.save()
            #         return HttpResponseRedirect('/blog/view/showpost/' + num)
            instance.user_id=request.user
            instance.post_id=post
            instance.save()
            return HttpResponseRedirect('/blog/view/showpost/' + num)
    else : 
        comment_form=CommentForm()
    context ={'post':post, 'comments':comments , 'comment_form':comment_form}
    return render(request,'blog/onePost.html',context)
