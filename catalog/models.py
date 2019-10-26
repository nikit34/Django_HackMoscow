from django.db import models

# Create your models here.


from django.urls import reverse

# предмет
class Subject(models.Model):
    name = models.CharField(max_length=200, help_text='Enter a subject tasks')

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=200, help_text="Enter the teacher")

    def __str__(self):
        return self.name


class Task(models.Model):
    title = models.CharField(max_length=200)
    child = models.ForeignKey('Child', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(default='', max_length=10000, help_text='Enter a brief description of the task')
    isbn = models.CharField('ISBN', max_length=13, help_text='ID task')
    subject = models.ManyToManyField(Subject, help_text='Select subject for this tasks')
    teacher = models.ForeignKey('Teacher', on_delete=models.SET_NULL, null=True)
    cost = models.IntegerField(help_text="Enter the tasks cost")
    grade = models.IntegerField(default=0, help_text="Enter the tasks grade")

    def display_genre(self):
        return ', '.join([subject.name for subject in self.subject.all()[:3]])

    display_genre.short_description = 'Subject'

    def get_absolute_url(self):
        return reverse('task-detail', args=[str(self.id)])

    def __str__(self):
        return self.title


import uuid
from datetime import date
from django.contrib.auth.models import User

class TaskInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text='Unique ID for this particular task across whole registry')
    task = models.ForeignKey('Task', on_delete=models.SET_NULL, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def is_overdue(self):
        if self.due_back and date.today() > self.due_back:
            return True
        return False

    LOAN_STATUS = (
        ('p', 'Performance'), # выполнение
        ('d', 'Debt'), # долг
        ('a', 'Available'), # доступный
        ('r', 'Reserved'), # зарезервированный
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='p', help_text='Task availability')

    class Meta:
        ordering = ['due_back']
        permissions = (('can_mark_returned', 'task with drew from the contract'),)

    def __str__(self):
        return '{0} ({1})'.format(self.id, self.task.title)


class Child(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    group = models.CharField(max_length=100)

    class Meta:
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('child-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)



