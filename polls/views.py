from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Question,Choices


def polls_details(request):
	return render(request,'polls/details.html',{'title':'polls_details'})


def polls_results(request,question_id):
	res = Question.objects.all()
	return render(request,'polls/results.html',{'title':'polls_results','question_id':question_id,'res':res})


def polls_votes(request,question_id):
	return render(request,'polls/votes.html',{'title':'polls_votes','question_id':question_id})
"""
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.create_user(username=username,email=email,password=password)
        user.save()
        return redirect("/")

    else:
        return render(request,'register.html')
"""