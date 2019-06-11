from django import forms
from .models import *
from .widgets import FengyuanChenDatePickerInput


class ConnexionForm(forms.Form):
    username = forms.CharField(max_length=30, help_text="Enter your id")
    password = forms.CharField(max_length=30, widget=forms.PasswordInput, help_text="Enter password")


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('slug',)

    def __init__(self, *args, **kwargs):
        super(CourseForm, self).__init__(*args, **kwargs)
        teachers = User.objects.filter(groups__name="teacher")
        self.fields['professors'] = forms.ModelMultipleChoiceField(queryset=teachers)
        students = User.objects.filter(groups__name="student")
        self.fields['students'] = forms.ModelMultipleChoiceField(queryset=students)


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'insufficient', 'weak', 'aimed_at', 'beyond')


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('date',)
        widgets = {

            'date': FengyuanChenDatePickerInput()
        }

    # passer directement la liste des cours depuis la vue et utiliser 'initial={courses=courses}


class EvaluationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        courses = kwargs.pop("courses")
        super(EvaluationForm, self).__init__(*args, **kwargs)

        self.fields['course'] = forms.ModelChoiceField(queryset=courses)


class EvaluateCourseForm(forms.Form):

    def __init__(self, *args, **kwargs):

        sessions = kwargs.pop("sessions")
        students = kwargs.pop("students")
        skills = kwargs.pop("skills")

        super(EvaluateCourseForm, self).__init__(*args, **kwargs)

        self.fields['session'] = forms.ModelChoiceField(queryset=sessions)
        self.fields['concerned'] = forms.ModelChoiceField(queryset=students)
        self.fields['skill'] = forms.ModelChoiceField(queryset=skills)
        self.fields['mark'] = forms.IntegerField()
