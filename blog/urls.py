from django.urls import path, re_path
from blog import views
urlpatterns = [
    path('', views.landpage,name='landpage'),
    path('view/<cat>', views.categoryPosts),
    path('search',views.searchPost),
    path('view/showpost/<num>',views.showpost),
    path('showpost/<num>',views.showpost),
    path('showpost/showpost/<num>',views.showpost),
    path('subscribe/<num>', views.subscribe),
    path('showpost/withtag/<id>',views.showPostsByTags),
    path('showpost/like/<num>',views.like),
    path('about/', views.about, name='about')
]
