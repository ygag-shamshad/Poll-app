from django.contrib import admin

from .models import Questions,Choice
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model=Choice
    extra=3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets=[
        ('Question',{'fields':['question_text']}),
        ('Date Information',{'fields':['pub_date'],'classes':['collapse']}),
    ]
    inlines=[ChoiceInline]
    list_display=('question_text','pub_date','was_published_recently')
    list_filter=['pub_date']
    search_fields=['question_text']

admin.site.register(Questions,QuestionAdmin)



# admin.site.register(Choice)