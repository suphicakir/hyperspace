from django.db import models
from django.utils.text import slugify


# Create your models here.

class Services (models.Model):
    Title=models.CharField(max_length=100)
    Description=models.TextField()
    IconClass=models.CharField(max_length=50)
    IsFeatured=models.BooleanField(default=False)
    Slug=models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.Title
    
    def save (self,*args, **kwargs):
        if not self.Slug:
            self.Sl=slugify(self.Title)
        
        super(Services,self).save(*args, **kwargs)

    class Meta:
        ordering=['Title']
        verbose_name='Service'
        verbose_name_plural='Services'



