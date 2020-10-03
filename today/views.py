from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import Article,Videos,PostProblem
from .forms import commentsform,postproblemform



def add_todo(request):
    title = request.POST["title"]
    content = request.POST["content"]
    solution = request.POST["solution"]
    solve = request.POST["solve"]
    image = request.POST["image"]
    created_obj = PostProblem.objects.create(content=content,title=title,solution=solution,solve=solve,image=image)
    return redirect("/")


"""
def signup(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        user = User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
        user.save();
        return redirect('/')
    else:
        return render(request,'register.html')
"""
def signup(request):
    if request.method == "POST":
        
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
    
        user=User.objects.create_user(first_name=first_name,last_name=last_name,email=email,username=username,password=password1)
        user.save()
        
        return redirect('login')
    else:
        return render(request,'register.html')    

def home(request):
    posts = PostProblem.objects.all()
    if request.method == 'GET':
        form = postproblemform()
    else:
        form = postproblemform(request.POST)
        if form.is_valid():
            form.save()
            postproblem_item = form.save(commit=False)
            postproblem_item.image = request.FILES['image']
            file_type = postproblem_item.image.url.split('.')[-1]
            file_type = file_type.lower()
            if file_type not in IMAGE_FILE_TYPES:
                context = {
                    'postproblem_item':postproblem_item,
                    'form':form
                }
            postproblem_item.save()
        else:
            form = postproblemform()
    videofile = Videos.objects.order_by('-id')
    yes = User.objects.count()
    a_list = Article.objects.all()
    return render(request,'home.html',{'title':'home','a_list':a_list,'yes':yes,'videofile':videofile,'form':form,'post':posts})

def about(request):
	return render(request,'about.html',{'title':'about'})


def formset(request):
    if request.method == 'GET':
        form = commentsform()
    else:
        form = commentsform(request.POST)
        if form.is_valid():
            form.save()
            comment_item = form.save(commit=False)
            comment_item.save()
        else:
            form = commentsform()
    return render(request,'formset.html',{'form':form})


def profile(request):
    return render(request,'profile.html')

    