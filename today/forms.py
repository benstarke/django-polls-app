from .models import Comments,PostProblem
from django import forms
from django.forms import ModelForm


class commentsform(ModelForm):
	class Meta:
		model = Comments
		fields = ['email','message','gender','name']


class postproblemform(ModelForm):
	class Meta:
		model = PostProblem
		fields = ['title','image','content','solution','solve']