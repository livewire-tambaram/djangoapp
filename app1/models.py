from django.db import models

# Create your models here.
class Enquiry(models.Model):
    name = models.CharField(max_length=30, help_text='Name should be within 30 letters',verbose_name='Enter Name')
    email = models.EmailField(help_text='Email should contain @ symbol',verbose_name='Enter Email Id')
    phone = models.IntegerField(help_text='Phone Number should contain 10 digits',verbose_name='Enter Mobile Number')
    course = models.CharField(max_length=20,verbose_name='Preffered Course', choices=[
        ('Java','Java'),
        ('Python','Python'),
        ('C','C'),('C++','C++'),
        ('Django','Django'),
        ('Full Stack','Full Stack'),
        ('Others','Others')
    ],default='Java')
