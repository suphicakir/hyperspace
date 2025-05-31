from django.db import models
from django.utils.text import slugify


# Create your models here.
#_title
#_description
#_iconClass
#_isFutured
#_slug

class Services (models.Model):
    _title=models.CharField(max_length=100)
    _description=models.TextField()
    _iconClass=models.CharField(max_length=50)
    _isFutured=models.BooleanField(default=False)
    _slug=models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self._title
    
    def save (self,*args, **kwargs):
        if not self._slug:
            self._slug=slugify(self._title)
        
        super(Services,self).save(*args, **kwargs)

    class Meta:
        ordering=['_title']
        verbose_name='Service'
        verbose_name_plural='Services'



