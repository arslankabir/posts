from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.OneToOneField('Author', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='pics', null=False, blank=False)
    slug = models.SlugField()

    def __str__(self):
         return self.title

    def get_absolute_url(self):
        return "/posts/{}/".format(self.slug)

    def get_update_url(self):
        return "/posts/{}/update".format(self.slug)
    
    def get_delete_url(self):
        return "/posts/{}/delete".format(self.slug)

class Author(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    author_email = models.EmailField()
    cellphone_num = models.IntegerField()
    def __str__(self):
         return self.user.username