from django.contrib import admin
from .models import *

# Register your models here.


class SkillAdmin(admin.ModelAdmin):
    list_display = ('name', 'insufficient', 'weak', 'aimed_at', 'beyond', 'course', 'number_eval', 'slug')
    list_filter = ('course', )
    ordering = ('name', 'course', 'number_eval')
    search_fields = ('name', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('General', {
            'classes': ['collapse', ],
            'fields': ('name', 'course', 'number_eval', 'slug')
        }),
        # Fieldset 2 : subsidiaires
        ('This skill evaluates : ', {
            'fields': ('insufficient', 'weak', 'aimed_at', 'beyond')
        }),
    )

    prepopulated_fields = {'slug': ('name',), }


class SessionAdmin(admin.ModelAdmin):
    list_display = ('date', 'course', 'number_eval', 'slug')
    list_filter = ('course', )
    date_hierarchy = 'date'
    ordering = ('date', 'course', 'number_eval')
    search_fields = ('course', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('General informations', {
            'fields': ('date', 'course', 'number_eval', 'slug')
        }),
    )


class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    list_filter = ('professors', 'students')
    ordering = ('name', )
    search_fields = ('name', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('General informations', {
            'classes': ['collapse', ],
            'fields': ('name', 'professors', 'slug')
        }),
        # Fieldset 2 : subsidiaires
        ('List of students', {
            'fields': ('students',)
        }),
    )

    prepopulated_fields = {'slug': ('name',), }


class SKillEvalAdmin(admin.ModelAdmin):
    list_display = ('skill', 'level', 'eval', 'comment')
    list_filter = ('skill',)
    ordering = ('level', 'skill')
    search_fields = ('skill', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ("Contenu de l'évaluation", {
            'classes': ["collapse", ],
            'fields': ('skill', 'level', 'eval', 'comment')
        }),

    )


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('session', 'concerned', 'general', 'teacher')
    list_filter = ('concerned', 'teacher')
    ordering = ('concerned', )
    search_fields = ('concerned', 'teacher')

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ("Contenu de l'évaluation", {
            'classes': ["collapse", ],
            'fields': ('session', 'concerned', 'general', 'teacher')
        }),
    )


admin.site.register(Skill, SkillAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(SkillEvaluation, SKillEvalAdmin)
admin.site.register(Evaluation, EvaluationAdmin)



