from django.urls import path
from blog import views

urlpatterns = [
	path('word', views.wordIndex),
	path('word/create', views.wordCreate),
	path('word/show/<id>', views.wordShow),
	path('word/edit/<id>', views.wordEdit),
	path('word/delete/<id>', views.wordDelete),

	path('reply', views.replyIndex),
	path('reply/create', views.replyCreate),
	path('reply/show/<id>', views.replyShow),
	path('reply/edit/<id>', views.replyEdit),
	path('reply/delete/<id>', views.replyDelete)
]