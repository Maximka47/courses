from tabnanny import verbose
from django.db import models

# Create your models here.
class Subject(models.Model):
    name = models.CharField(verbose_name="Name",
                            max_length=100,
                            blank=True,
                            null=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = "Subject"
        verbose_name_plural="Subjects"

class StudentGroup(models.Model):

    name = models.CharField(verbose_name="Name", max_length=100)

    students_number = models.DecimalField(max_digits=4, decimal_places=0,
                                                        verbose_name="Number of students",
                                                        blank=True,
                                                        null=True)
    
    subject = models.ForeignKey(Subject, verbose_name="Subject",
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name = "groups",
                                            blank=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name="Group of students"
        verbose_name_plural="Groups of students"

class Student(models.Model):

    SURNAME_CHOICES = (
        ("Petrenko","Петренко"),
        ("Shevchenko","Шевченко"),
    )

    name = models.CharField(verbose_name="Name",
                            max_length=100,
                            blank=True,
                            null=True)

    surname = models.CharField(verbose_name="Surname",
                                max_length=100,
                                blank=True,
                                null=True,
                                choices=SURNAME_CHOICES)

    birthday = models.DateField(verbose_name="Birthday",
                                blank=True,
                                null=True)

    group = models.ForeignKey(StudentGroup, verbose_name="Group",   #OneToOneField(one student in one group) ManyToManyField(many students and each of them can be in many groups)
                                            on_delete=models.SET_NULL,
                                            null=True,
                                            related_name = "students",
                                            blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.name += '111'
        super().save(*args, **kwargs)

    class Meta:
        verbose_name="Student"
        verbose_name_plural="Students"

