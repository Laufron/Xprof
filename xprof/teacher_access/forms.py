from django import forms
from .models import *
from .widgets import FengyuanChenDatePickerInput


def get_full_name(self):
    return self.first_name + ' ' + self.last_name


User.add_to_class("__str__", get_full_name)


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

        self.fields['session'] = forms.ModelChoiceField(queryset=sessions,
                                                        widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['concerned'] = forms.ModelChoiceField(queryset=students,
                                                          widget=forms.Select(attrs={'class': 'form-control'}))
        self.fields['general'] = forms.CharField(required=False, max_length=400, label="General comment on the session",
                                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
