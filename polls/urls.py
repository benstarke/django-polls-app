from django.urls import path
from .import views

urlpatterns = [
	path('polls_details/',views.polls_details,name='polls_details'),
	path('polls_results/<int:question_id>/',views.polls_results,name='polls_results'),
	path('polls_votes/<int:question_id>',views.polls_votes,name='polls_votes'),
	#path('register/',views.register,name='register'),
]