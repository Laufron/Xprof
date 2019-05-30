from django.db import models

# Create your models here.


class User(models.Model):
    firstname = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    login = models.CharField(max_length=100, default='login')
    password = models.CharField(max_length=50, default='azerty')
    status = models.CharField(max_length=50, choices=[("T", "teacher"), ("S", "student")], default="T")

    def __str__(self):
        return "".join(self.firstname).join(" ").join(self.name)

    class Meta:
        verbose_name = "Teacher/Student"
        ordering = ['name']


class Course(models.Model):
    name = models.CharField(max_length=100, default='')
    professors = models.ManyToManyField(User, related_name='courses_given', blank=True)
    students = models.ManyToManyField(User, related_name='courses_followed', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        ordering = ['name']


class Session(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name+"_"+self.date.__str__()

    class Meta:
        verbose_name = "session"
        ordering = ['date']


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE,verbose_name="evaluated in")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "skill"
        ordering = ['name']


class Evaluation(models.Model):
    mark = models.IntegerField()
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    concerned = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.session.course.name+"_"+self.skill.name+"_"+self.session.date.__str__()

    class Meta:
        verbose_name = "evaluation"
        ordering = ['skill']


