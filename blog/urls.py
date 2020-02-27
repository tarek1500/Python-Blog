from django.urls import path, re_path
from blog import views
urlpatterns = [
    path('landpage', views.landpage),
    path('subscribe/<num>', views.subscribe),
    path('view/<cat>', views.categoryPosts),
    re_path(r'^[a-zA-z/]*search',views.searchPost),
    path('view/showpost/<num>',views.showpost),
    path('showpost/showpost/<num>',views.showpost),
    path('showpost/<num>',views.showpost),
    path('withtag/<id>',views.showPostsByTags),
    path('showpost/like/<num>',views.like)
]
