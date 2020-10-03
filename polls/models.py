from django.db import models
from django.utils import timezone

class Question(models.Model):
	question_text = models.CharField(max_length=255)
	pub_date = models.DateTimeField('date published')
	def __str__(self):
		return self.question_text
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choices(models.Model):
	question = models.ForeignKey(Question,on_delete=models.CASCADE)
	choice_text = models.CharField(max_length=55)
	votes = models.IntegerField(default=0)
	def __str__(self):
		return self.choice_text


class Person(models.Model):
	name = models.CharField(max_length=100)
	def __str__(self):
		return self.name


class Group(models.Model):
	name = models.CharField(max_length=100)
	members = models.ManyToManyField(Person,through='Membership')
	def __str__(self):
		return self.name


class Membership(models.Model):
	person = models.ForeignKey(Person,on_delete=models.CASCADE)
	group = models.ForeignKey(Group,on_delete=models.CASCADE)
	date_join = models.DateTimeField()
	invite_reason = models.CharField(max_length=225)
	url = models.URLField()
	class Meta:
		verbose_name = None
	def __str__(self):
		return self.invite_reason



