from django.shortcuts import redirect, render
from django.utils.text import slugify
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse


from .forms import *
from .models import *


# Create your views here.


def check_log(request):

    if (not request.user.is_authenticated
            or request.path == '/teacher/auth'
            or request.path == '/admin'
            or request.path == '/teacher/register'):
        return redirect('authentication')
    else:
        return redirect('home')


def log_page(request):
    auth_message = ""

    form = ConnexionForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user:
            if user.groups.filter(name="teacher").exists():
                login(request, user)
                return redirect('home')
        auth_message = "Invalid credential, only accessible to teachers"

    return render(request, 'teacher_access/auth_page.html', locals())


def log_out(request):
    logout(request)
    return redirect(reverse('authentication'))


def home_page(request):
    return render(request, 'teacher_access/home.html', {})


def evaluate(request):
    courses = Course.objects.filter(professors=request.user)
    form = EvaluationForm(request.POST or None, courses=courses)
    if form.is_valid():
        course = form.cleaned_data['course']
        return redirect('evaluate_course', course_slug=course.slug)

    return render(request, 'teacher_access/evaluation.html', locals())


def evaluate_course(request, course_slug):

    course = Course.objects.get(slug=course_slug)
    course_name = course.name

    sessions = Session.objects.filter(course__exact=course)
    students = User.objects.filter(courses_followed__exact=course, groups__name="student")
    skills = Skill.objects.filter(course__exact=course)

    form = EvaluateCourseForm(request.POST or None, sessions=sessions, students=students, skills=skills)
    if form.is_valid():
        session = form.cleaned_data['session']
        concerned = form.cleaned_data['concerned']
        skill = form.cleaned_data['skill']
        mark = form.cleaned_data['mark']

        skill.number_eval += 1
        skill.save()
        session.number_eval += 1
        session.save()

        Evaluation.objects.create(session=session, concerned=concerned, skill=skill, mark=mark, teacher=request.user)

        return redirect('home')

    return render(request, 'teacher_access/evaluate_course.html', locals())


def new_course(request):
    message = "Start a new course"
    form = CourseForm(request.POST or None)
    if form.is_valid():
        course = form.save(commit=False)
        course.slug = slugify(course.name)
        course.save()
        form.save_m2m()

        return redirect('courses')

    return render(request, "teacher_access/new_course.html", locals())


def all_courses(request):
    course_list = Course.objects.filter(
        professors=request.user).all()
    return render(request, 'teacher_access/all_courses.html', {'course_list': course_list})


def course_detail(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    skills = Skill.objects.filter(course__exact=course).all()
    sessions = Session.objects.filter(course__exact=course).all()
    students = User.objects.filter(courses_followed__exact=course).all()

    return render(request, 'teacher_access/course_detail.html', {
        "course_name": course.name,
        "course_slug": course_slug,
        "skills_list": skills,
        "sessions_list": sessions,
        "students_list": students
    })


def delete_course(request, course_slug):
    course = Course.objects.get(slug__exact=course_slug)
    course.delete()
    return redirect('courses')


def edit_course(request, course_slug):
    message = "Edit your course"
    course = Course.objects.get(slug=course_slug)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('courses')

    return render(request, "teacher_access/edit_course.html", locals())


def new_session(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    course_name = course.name

    form = SessionForm(request.POST or None)
    if form.is_valid():
        session = form.save(commit=False)
        session.slug = "session-" + str(session.date)
        session.course = course
        session.number_eval = 0
        session.save()
        form.save_m2m()

        return redirect('course', course_slug=course_slug)

    return render(request, "teacher_access/new_session.html", locals())


def delete_session(request, course_slug, session_slug):
    session = Session.objects.get(slug=session_slug, course__slug__exact=course_slug)
    session.delete()
    return redirect('course', course_slug)


def skill_detail(request, course_slug, skill_slug):
    course = Course.objects.get(slug=course_slug)
    skill = Skill.objects.get(slug=skill_slug)

    return render(request, 'teacher_access/skill_detail.html', {
        "course_name": course.name,
        "course_slug": course_slug,
        "skill_name": skill.name,
        "skill_slug": skill_slug,
        "insufficient": skill.insufficient,
        "weak": skill.weak,
        "aimed_at": skill.aimed_at,
        "beyond": skill.beyond,
    })


def new_skill(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    course_name = course.name

    form = SkillForm(request.POST or None)
    if form.is_valid():
        skill = form.save(commit=False)
        skill.slug = slugify(skill.name)
        skill.course = course
        skill.number_eval = 0
        skill.save()
        form.save_m2m()

        return redirect('course', course_slug=course_slug)

    return render(request, "teacher_access/new_skill.html", locals())


def delete_skill(request, course_slug, skill_slug):
    skill = Skill.objects.get(slug=skill_slug)
    skill.delete()
    return redirect('course', course_slug)


def edit_skill(request, course_slug, skill_slug):
    message = "Edit your skill"
    course = Course.objects.get(slug=course_slug)
    course_name = course.name

    skill = Skill.objects.get(slug=skill_slug)
    skill_name = skill.name

    form = SkillForm(request.POST or None, instance=skill)
    if form.is_valid():
        form.save()
        return redirect('course', course_slug=course_slug)

    return render(request, "teacher_access/edit_skill.html", locals())
