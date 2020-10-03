from django.contrib import admin
from .models import Question,Choices,Membership,Person,Group


class QuestionAdmin(admin.ModelAdmin):
	list_display = ('question_text','pub_date')


class ChoicesAdmin(admin.ModelAdmin):
	list_display = ('question','choice_text','votes')


class MembershipAdmin(admin.ModelAdmin):
	list_display = ('date_join','invite_reason')

admin.site.register(Question,QuestionAdmin)
admin.site.register(Choices,ChoicesAdmin)
admin.site.register(Group)
admin.site.register(Person)
admin.site.register(Membership,MembershipAdmin)