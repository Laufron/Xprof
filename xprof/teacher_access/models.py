from django.db import models
from django.contrib.auth.models import User
from django.core.validators import int_list_validator

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=100, default='')
    professors = models.ManyToManyField(User, related_name='courses_given', blank=True)
    students = models.ManyToManyField(User, related_name='courses_followed', blank=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        ordering = ['name']


class Session(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    number_eval = models.IntegerField(default=0, verbose_name="number of evaluations on this date")
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.course.name+" _ "+self.date.__str__()

    class Meta:
        verbose_name = "session"
        ordering = ['date']


class Skill(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="evaluated in")
    slug = models.SlugField(max_length=100)
    number_eval = models.IntegerField(default=0)
    insufficient = models.CharField(max_length=300)
    weak = models.CharField(max_length=300)
    aimed_at = models.CharField(max_length=300)
    beyond = models.CharField(max_length=300)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "skill"
        ordering = ['name']


class Evaluation(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    concerned = models.ForeignKey(User, on_delete=models.CASCADE, related_name="concerned")
    general = models.CharField(max_length=250)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="evaluated by", related_name="teacher")

    def __str__(self):
        return self.session.course.name+"_"+self.session.date.__str__()

    class Meta:
        verbose_name = "evaluation"
        ordering = ['session__date']


class SkillEvaluation(models.Model):
    comment = models.CharField(max_length=150)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    eval = models.ForeignKey(Evaluation, on_delete=models.CASCADE)

    def __str__(self):
        return self.skill.name+"_eval"

    class Meta:
        verbose_name = "skill evaluation"
        ordering = ['skill']



