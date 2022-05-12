from django.db import models

class Sliders(models.Model):
    image = models.ImageField(upload_to='SlidersImage',verbose_name='Image')
    url = models.CharField(max_length=999,verbose_name='URl')

    def __str__(self):
        return self.url