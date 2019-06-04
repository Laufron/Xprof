from django.contrib import admin
from .models import *

# Register your models here.


class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'firstname', 'login')
    ordering = ('name', 'firstname')
    search_fields = ('name', 'firstname')

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Personal informations', {
            'fields': ('firstname', 'name', 'login', 'password')
        }),

    )


class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'firstname', 'login')
    ordering = ('name', 'firstname')
    search_fields = ('name', 'firstname')

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ('Personal informations', {
            'fields': ('firstname', 'name', 'login', 'password')
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
    list_display = ('name', 'slug')
    list_filter = ('professors',)
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


class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('concerned', 'skill', 'mark', 'session', 'teacher')
    list_filter = ('skill', 'session', 'teacher')
    ordering = ('concerned', 'skill', 'mark', 'session')
    search_fields = ('concerned', )

    fieldsets = (
        # Fieldset 1 : meta-info (titre, auteur…)
        ("Contenu de l'évaluation", {
            'classes': ["collapse", ],
            'fields': ('skill', 'session', 'concerned', 'mark', 'teacher')
        }),

    )


admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Student, StudentAdmin)
admin.site.register(Skill, SkillAdmin)
admin.site.register(Session, SessionAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(Evaluation, EvaluationAdmin)


