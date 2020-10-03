from django.db import models
from django.contrib.auth.models import User


class PostProblem(models.Model):
    title = models.CharField(max_length=55)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    image = models.FileField(upload_to='post_pics')
    solution = models.TextField()
    solve = models.TextField()
    def __str__(self):
        return self.title

        

class Reporter(models.Model):
	GENDER = [('1','male'),('2','female'),('3','intersex')	]
	city_pick = models.TextChoices('city_pick','London kenya uganda')
	full_name = models.CharField(max_length=55)
	city = models.CharField(blank=True,choices=city_pick.choices,max_length=20)
	gender = models.CharField(max_length=1,choices=GENDER)
	
	


	def __str__(self):
		return self.full_name

class Article(models.Model):
	reporter = models.ForeignKey(Reporter,on_delete=models.CASCADE)
	content = models.TextField()
	headline = models.CharField(max_length=100,)
	pub_date = models.DateTimeField(auto_now_add=False)
	def __str__(self):
		return self.headline

class Mytest(models.Model):
	repo = models.ManyToManyField(Article
	)

class Comments(models.Model):
	GENDER = [('1','male'),('2','female'),('3','intersex')]
	name = models.CharField(max_length=55)
	email = models.EmailField()
	message = models.TextField()
	gender = models.CharField(max_length=1,choices=GENDER)
	def __str__(self):
		return self.email


class Profile(models.Model):
	user = models.OneToOneField(User,on_delete=models.CASCADE)
	user_image = models.ImageField(default='default.jpg',upload_to='profile_pics')
	def __str__(self):
		return f' {self.user.username} Profile'


class Videos(models.Model):
    name = models.CharField(max_length=55)
    videofile = models.FileField(upload_to='videos',null=True,verbose_name="")
    def __str__(self):
        return self.name + ":" + str(self.videofile)

