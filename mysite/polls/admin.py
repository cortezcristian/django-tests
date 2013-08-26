from django.contrib import admin
from polls.models import Choice, Poll
#from polls.models import Choice
#admin.site.register(Choice)

#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

#class PollAdmin(admin.ModelAdmin):
#    fields = ['pub_date', 'question']

class PollAdmin(admin.ModelAdmin):
    #list_display = ('question', 'pub_date')
    list_display = ('question', 'pub_date', 'was_published_recently')
    fieldsets = [
        (None,               {'fields': ['question']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
