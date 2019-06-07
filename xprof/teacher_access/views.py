from django.shortcuts import redirect, render
from django.utils.text import slugify


from .forms import *
from .models import *

# Create your views here.


def check_log(request):
    if 'logged' not in request.session:
        request.session['logged'] = False

    if not (request.session['logged']
            or request.path == '/teacher/auth'
            or request.path == '/admin'
            or request.path == '/teacher/register'):
        return redirect('authentication')
    else:
        return redirect('home')

#utiliser authenticate et login de contrib.auth import authenticate, login
#regarder la class user de django


def log_page(request):
    auth_error = False

    form = AuthForm(request.POST or None)

    if form.is_valid():
        login = form.cleaned_data['login']
        password = form.cleaned_data['password']

        auth_check = Teacher.objects.filter(login=login, password=password)

        if not auth_check.exists():
            auth_error = True
        else:
            request.session['firstname'] = auth_check[0].firstname
            request.session['name'] = auth_check[0].name
            request.session['logged'] = True
            return redirect('home')

    return render(request, 'teacher_access/auth_page.html', locals())


def new_user(request):
    form = TeacherForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('authentication')

    return render(request, "teacher_access/register.html", locals())


def log_out(request):
    request.session['firstname'] = ''
    request.session['name'] = ''
    request.session['logged'] = False
    return redirect('authentication')


def home_page(request):
    return render(request, 'teacher_access/home.html', {"firstname": request.session['firstname'], "name": request.session['name']})


def evaluate(request):
    form = EvaluationForm(request.POST or None, session=request.session)
    if form.is_valid():
        course = form.cleaned_data['course']
        return redirect('evaluate_course', course_slug=course.slug)

    return render(request, 'teacher_access/evaluation.html', locals())


def evaluate_course(request, course_slug):

    form = EvaluateCourseForm(request.POST or None, slug=course_slug)
    if form.is_valid():
        teacher = Teacher.objects.get(name=request.session['name'], firstname=request.session['firstname'])
        session = form.cleaned_data['session']
        concerned = form.cleaned_data['concerned']
        skill = form.cleaned_data['skill']
        mark = form.cleaned_data['mark']

        skill.number_eval += 1
        skill.save()
        session.number_eval += 1
        session.save()

        Evaluation.objects.create(session=session, concerned=concerned, skill=skill, mark=mark, teacher=teacher)

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
        professors__name__iexact=request.session['name'],
        professors__firstname__iexact=request.session['firstname']).all()
    return render(request, 'teacher_access/all_courses.html', {'course_list': course_list})


def course_detail(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    skills = Skill.objects.filter(course__exact=course).all()
    sessions = Session.objects.filter(course__exact=course).all()
    students = Student.objects.filter(courses_followed__exact=course).all()

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


def new_session(request, course_slug):
    course = Course.objects.get(slug=course_slug)
    course_name = course.name

    form = SessionForm(request.POST or None)
    if form.is_valid():
        session = form.save(commit=False)
        session.slug = "session-"+str(session.date)
        session.course = course
        session.number_eval = 0
        session.save()
        form.save_m2m()

        return redirect('course', course_slug=course_slug)

    return render(request, "teacher_access/new_session.html", locals())


def skill_detail(request, course_slug, skill_slug):
    course = Course.objects.get(slug=course_slug)
    skill = Skill.objects.get(slug=skill_slug)

    return render(request, 'teacher_access/skill_detail.html', {
        "course_name": course.name,
        "course_slug": course_slug,
        "skill_name": skill.name,
        "skill_slug": skill_slug
    })


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
