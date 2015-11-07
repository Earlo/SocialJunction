from django.contrib import admin

# Register your models here.
from .models import Project, Event

class EventInLine(admin.StackedInline):
    model = Event
    fieldsets = [
        ('Event Data',       {'fields': ['description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    extra = 0

class ProjectAdmin( admin.ModelAdmin ):
    fieldsets = [
        ('Project Name',       {'fields': ['name']}),
        ('Project Info',       {'fields': ['description']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [EventInLine]

admin.site.register(Project, ProjectAdmin)

list_filter = ['pub_date']
