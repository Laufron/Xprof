from django.db import models

# Create your models here.


class Teacher(models.Model):
    firstname = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    login = models.CharField(max_length=100, default='', unique=True)
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.firstname+" "+self.name

    class Meta:
        verbose_name = "Teacher"
        ordering = ['name']


class Student(models.Model):
    firstname = models.CharField(max_length=100, default='')
    name = models.CharField(max_length=100, default='')
    login = models.CharField(max_length=100, default='', unique=True)
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.firstname+" "+self.name

    class Meta:
        verbose_name = "Student"
        ordering = ['name']


class Course(models.Model):
    name = models.CharField(max_length=100, default='')
    professors = models.ManyToManyField(Teacher, related_name='courses_given', blank=True)
    students = models.ManyToManyField(Student, related_name='courses_followed', blank=True)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Course'
        ordering = ['name']


class Session(models.Model):
    date = models.DateField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return self.course.name+" _ "+self.date.__str__()

    class Meta:
        verbose_name = "session"
        ordering = ['date']


class Skill(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="evaluated in")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "skill"
        ordering = ['name']


class Evaluation(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    concerned = models.ForeignKey(Student, on_delete=models.CASCADE)
    skill = models.ForeignKey(Skill, on_delete=models.CASCADE)
    mark = models.IntegerField()
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="evaluated by")
    # Rajouter le champ commentaire

    def __str__(self):
        return self.session.course.name+"_"+self.skill.name+"_"+self.session.date.__str__()

    class Meta:
        verbose_name = "evaluation"
        ordering = ['skill']


