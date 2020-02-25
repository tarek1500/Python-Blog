from django.urls import path
from blog import views
urlpatterns = [
    path('landpage', views.landpage),
    path('view/<cat>', views.categoryPosts),
    path('search',views.searchPost),
    path('view/showpost/<num>',views.showpost),
    path('showpost/<num>',views.showpost),
   
]
