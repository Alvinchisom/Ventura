from django.db import models
from django.templatetags.static import static

class AdminBored(models.Model):
    name = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='admin_bored/', null=True, blank=True)
    bio = models.TextField(max_length=200,null=True,blank=True)
    facebook_url = models.CharField(max_length=200, null=True, blank=True)
    twitter_url = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_image_url(self):
        if self.image:
            return self.image.url
        return static('image/user.png')
