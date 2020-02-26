from django.urls import path , re_path
from blog import views
urlpatterns = [
    path('landpage', views.landpage),
    path('view/<cat>', views.categoryPosts),
    re_path(r'^[a-zA-Z]+/search',views.searchPost),
    path('view/showpost/<num>',views.showpost),
    path('showpost/<num>',views.showpost),
    # path('withtag/<num>',views.showPostsByTags),
    path('showpost/like/<num>',views.showpost)
]
