from django.contrib import admin
from .models import *

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'name', 'login', 'status')
    list_filter = ('status', )
    ordering = ('name', 'firstname', 'status')
    search_fields = ('name', 'firstname' )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Personal informations', {
            'fields': ('firstname', 'name', 'login', 'password', 'status' )
        }),

    )


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'course')
    list_filter = ('course', )
    ordering = ('name', 'course')
    search_fields = ('name', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('General', {
            'classes': ['collapse', ],
            'fields': ('name', 'course')
        }),
        # Fieldset 2 : subsidiaires
        ('This skill evaluates : ', {
            'fields': ('description', )
        }),
    )


class SessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'course')
    list_filter = ('course', )
    date_hierarchy = 'date'
    ordering = ('date', 'course')
    search_fields = ('course', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('General informations', {
            'fields': ('date', 'course')
        }),
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'professors.name')
    list_filter = ('professors',)
    ordering = ('name', )
    search_fields = ('name', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('General informations', {
            'classes': ['collapse', ],
            'fields': ('name', 'professors')
        }),
        # Fieldset 2 : subsidiaires
        ('List of students', {
            'fields': ('students',)
        }),
    )


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('concerned', 'skill', 'mark', 'session')
    list_filter = ('skill', 'session')
    ordering = ('concerned', 'skill', 'mark', 'session')
    search_fields = ('concerned', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ("Contenu de l'évaluation", {
            'classes': ["collapse", ],
            'fields': ('skill', 'session', 'concerned', 'mark')
        }),

    )


admin.site.register(User, UserAdmin)
admin.site.register(Skill)
admin.site.register(Session)
admin.site.register(Course)
admin.site.register(Evaluation)


