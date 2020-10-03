from django.urls import path,include
from .import views

urlpatterns = [
	path('',views.home,name='home'),
	path('about/',views.about,name='about'),
	path('signup/',views.signup,name='register'),
	path('formset/',views.formset,name='formset'),
	path('accounts/',include('django.contrib.auth.urls')),
  path('profile/',views.profile,name='profile'),
	path('add_todo/',views.add_todo,name='add_todo'),
]