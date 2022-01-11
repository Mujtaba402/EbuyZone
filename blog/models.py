from django.contrib.auth.models import User
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    dob = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to='blog/Profile',null=True, blank=True)

    def __str__(self):
        return "Profile of user {}".format(self.user.username)

class Blogpost(models.Model):
    post_id     = models.AutoField(primary_key=True)
    title       = models.CharField(max_length=50)
    head0       = models.CharField(max_length=500, default="")
    chead0      = models.TextField(max_length=5000, default="")
    head1       = models.CharField(max_length=500, default="")
    chead1      = models.TextField(max_length=5000, default="")
    head2       = models.CharField(max_length=500, default="")
    chead2      = models.TextField(max_length=5000, default="")
    pub_date    = models.DateField()
    thumbnail   = models.ImageField(upload_to='blog/post', default="")

    def __str__(self):
        return self.title