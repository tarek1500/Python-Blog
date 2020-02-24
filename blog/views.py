from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect
from blog.models import Category ,Post
from django.db.models import Q

# Create your views here.
def landpage(request):
    category = Category.objects.all()
    post= Post.objects.all().order_by('-created_on')
    context ={'category':category}
    return render(request, 'blog/landpage.html', context)


def categoryPosts(request,cat):
    posts=Post.objects.filter(category_name=cat).order_by('-created_on')
    context = {'posts':posts}
    return render(request,'blog/posts.html',context)

def unsubscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = Category.objects.get(id = cat_id)
    subscribed_cats.user.remove(current_user)
    return HttpResponseRedirect('/home')

def subscribe(request, cat_id):
    current_user = request.user
    subscribed_cats = Category.objects.get(id = cat_id)
    subscribed_cats.user.add(current_user)
    #confirmSubscription(current_user.email,subscribed_cats.cat_title)
    return HttpResponseRedirect('/home')

def searchPost(request):
    queryset= request.GET.get("query")
    if queryset:
        queryset_list=Post.objects.filter(Q(title__icontains=queryset)| Q(tags__tag__icontains=queryset))
        context = {'posts':queryset_list}
        return render(request,'blog/posts.html',context)

    else:
        return HttpResponse ("<h1> There is nothing </h1>")