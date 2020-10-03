from django.contrib import admin
from .models import Reporter,Article,Mytest,Comments,Profile,Videos,PostProblem


class ArticleAdmin(admin.ModelAdmin):
	list_display = ('content','headline','pub_date')



class CommentsAdmin(admin.ModelAdmin):
	list_display = ('name','email','message','gender')


class PostProblemAdmin(admin.ModelAdmin):
	list_display = ('title','content','date_created','solution','solve')



admin.site.register(Profile)
admin.site.register(Reporter)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Mytest)
admin.site.register(Videos)
admin.site.register(Comments,CommentsAdmin)
admin.site.register(PostProblem,PostProblemAdmin)


