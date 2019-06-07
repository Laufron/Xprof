from django import forms
from .models import *
from .widgets import FengyuanChenDatePickerInput


class AuthForm(forms.Form):
    login = forms.CharField(max_length=100, help_text="Enter your id")
    password = forms.CharField(max_length=100, widget=forms.PasswordInput, help_text="Enter password")


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = '__all__'


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        exclude = ('slug', )


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('name', 'description')


class SessionForm(forms.ModelForm):
    class Meta:
        model = Session
        fields = ('date', )
        widgets = {
            'date': FengyuanChenDatePickerInput()
        }

#passer directement la liste des cours depuis la vue et utiliser 'initial={courses=courses}


class EvaluationForm(forms.Form):

    def __init__(self, *args, **kwargs):
        session = kwargs.pop("session")

        super(EvaluationForm, self).__init__(*args, **kwargs)

        teacher = Teacher.objects.get(firstname=session["firstname"], name=session["name"])
        query = Course.objects.filter(professors__name__iexact=teacher.name,
                                      professors__firstname__iexact=teacher.firstname)

        self.fields['course'] = forms.ModelChoiceField(queryset=query)


class EvaluateCourseForm(forms.Form):

    def __init__(self, *args, **kwargs):
        course_slug = kwargs.pop("slug")
        super(EvaluateCourseForm, self).__init__(*args, **kwargs)

        course = Course.objects.get(slug__iexact=course_slug)
        sessions = Session.objects.filter(course=course)
        students = Student.objects.filter(courses_followed__exact=course)
        skills = Skill.objects.filter(course__exact=course)

        self.fields['session'] = forms.ModelChoiceField(queryset=sessions)
        self.fields['concerned'] = forms.ModelChoiceField(queryset=students)
        self.fields['skill'] = forms.ModelChoiceField(queryset=skills)
        self.fields['mark'] = forms.IntegerField()

    def clean_mark(self):
        mark = self.cleaned_data['mark']

        if mark < 0 or mark > 10:
            raise forms.ValidationError("La note doit être compris entre 0 et 10")

        return mark
