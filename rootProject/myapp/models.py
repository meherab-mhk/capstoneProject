from django.db import models

# Create your models here.

class A_home_slide(models.Model):
    title = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    slide_img = models.ImageField(upload_to='slide_img')

class B_about(models.Model):
    about_title = models.CharField(max_length=1000)
    about_desc = models.CharField(max_length=1000)
    about_img = models.ImageField(upload_to='about_img')


class C_course(models.Model):
    course_img =  models.ImageField(upload_to='course_img')
    btn_subject = models.CharField(max_length=1000)
    subject_name = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    def __str__(self) -> str:
        return self.subject_name


class D_advisor(models.Model):
    name = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='advisors')    
    img_title = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name


class E_events(models.Model):
    img = models.ImageField(upload_to='events')
    date = models.CharField(max_length=1000)
    date_m_y = models.CharField(max_length=1000, default="")
    event_name =  models.CharField(max_length=1000)
    time = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    speaker = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.event_name


class F_news(models.Model):
    date = models.CharField(max_length=1000)
    title = models.CharField(max_length=1000)
    desc = models.CharField(max_length=1000)
    img = models.ImageField(upload_to='news')
    
    def __str__(self) -> str:
        return self.date



class G_shop(models.Model):
    img = models.ImageField(upload_to='bookShop')    
    book_name = models.CharField(max_length=1000)
    writer = models.CharField(max_length=1000)
    price = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.book_name


class H_subscriber(models.Model):
    email = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.email


class I_question(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    subject = models.CharField(max_length=1000)
    experience = models.CharField(max_length=1000)
    message = models.CharField(max_length=1000)        
    
    def __str__(self) -> str:
        return self.name
    