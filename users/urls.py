from django.urls import path
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
	path('login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
	path('register/', user_views.register, name='register'),
	path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
	path('profile/', user_views.profile, name='profile')
]