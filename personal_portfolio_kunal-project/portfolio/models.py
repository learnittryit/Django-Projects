from django.db import models

# Create your models here.
class Project(models.Model):
    title_updated=models.CharField(max_length=100) # you can keep on passing more arguments
    description=models.CharField(max_length=200)
    #image =models.ImageField(upload_to='yes')
    image = models.ImageField(upload_to='portfolio/images/')

    #url =models.URLField(max_length=200)
    url=models.URLField(blank=True) # this means it does not have a url , its a statuc
    #url_=models.URLField()
