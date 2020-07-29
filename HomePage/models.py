from django.db import models
from datetime import *

class Banner_Image(models.Model):
    Banner_Image1 = models.ImageField(upload_to="homepage_images/banner_images",null=True,blank=True)
    Banner_Image1_caption_heading = models.CharField(max_length=40,null=True,blank=True)
    Banner_Image1_caption = models.CharField(max_length=40,null=True,blank=True)
    Banner_status1 = models.CharField(max_length=40,null = True, default="active")

    Banner_Image2 = models.ImageField(upload_to='homepage_images/banner_images',null=True,blank=True)
    Banner_Image2_caption_heading = models.CharField(max_length=40,null=True,blank=True)
    Banner_Image2_caption = models.CharField(max_length=40,null=True,blank=True)
    Banner_status2 = models.CharField(max_length=40, null=True, default="")

    Banner_Image3 = models.ImageField(upload_to='homepage_images/banner_images',null=True,blank=True)
    Banner_Image3_caption_heading = models.CharField(max_length=40,null=True,blank=True)
    Banner_Image3_caption = models.CharField(max_length=40,null=True,blank=True)
    Banner_status3 = models.CharField(max_length=40, null=True, default="")

    Banner_Image4 = models.ImageField(upload_to='homepage_images/banner_images',null=True,blank=True)
    Banner_Image4_caption_heading = models.CharField(max_length=40,null=True,blank=True)
    Banner_Image4_caption = models.CharField(max_length=40,null=True,blank=True)
    Banner_status4 = models.CharField(max_length=40, null=True, default="")

    Banner_Image5 = models.ImageField(upload_to='homepage_images/banner_images',null=True,blank=True)
    Banner_Image5_caption_heading = models.CharField(max_length=40,null=True,blank=True)
    Banner_Image5_caption = models.CharField(max_length=40,null=True,blank=True)
    Banner_status5 = models.CharField(max_length=40, null=True, default="")

    Banner_Image6 = models.ImageField(upload_to='homepage_images/banner_images',null=True,blank=True)
    Banner_Image6_caption_heading = models.CharField(max_length=40,null=True,blank=True)
    Banner_Image6_caption = models.CharField(max_length=40,null=True,blank=True)
    Banner_status6 = models.CharField(max_length=40, null=True, default="")


class Principal_Section(models.Model):
    principal_image = models.ImageField(upload_to='homepage_images/principal_images')
    principal_message = models.TextField()

class Notice(models.Model):
    text_notice = models.TextField(null=True,blank=True)
    image_notice = models.ImageField(null=True,blank=True,upload_to='homepage_images/notice_images')
    date_created = models.DateField(default=date.today)
    status = models.CharField(max_length=20,default="Active")


class Marquee(models.Model):
    marquee_text = models.TextField()
    date_created = models.DateField(default=date.today)
    status = models.CharField(max_length=10,default="Active")
    def __str__(self):
        return self.marquee_text

class Other_Section(models.Model):
    image = models.ImageField(upload_to='homepage_images/other_images',null=True,blank=True)
    title =  models.CharField(max_length=30,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    status = models.CharField(max_length=30,default="Active")

class About_School(models.Model):
    image = models.ImageField(upload_to='homepage_images/about_school')
    text = models.TextField()
    def __str__(self):
        return self.text
