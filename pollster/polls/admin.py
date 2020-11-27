from django.contrib import admin
from .models import Question, Choice

#admin.site.register( Question )
#admin.site.register( Choice )

admin.site.site_header = "Pollster Admin"
admin.site.site_title = "Pollster Admin Area"
admin.site.index_title = "Welcome to the Pollster admin area"


class ChoiceInline( admin.TabularInline ) :
    model = Choice
    extra = 3

class QuestionAdmin( admin.ModelAdmin) :
    #Options for inline editing of model instances.
    fieldsets = [(None, {'fields':['question_text']}),('Date Information', {'fields':['date_pub'], 'classes':['collapse']}), ]
    inlines = [ChoiceInline]
    
admin.site.register(Question, QuestionAdmin)
    