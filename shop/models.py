from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse
from django.utils import timezone


class product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default="0")
    desc = models.TextField(max_length=1000)
    pub_date = models.DateField()
    image = models.ImageField(upload_to="shop/images", default="", blank=True)
    likes = models.ManyToManyField(User, related_name='Likes', blank=True)

    def __str__(self):
        return self.product_name

    def total_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse("shop:productview", args=[self.id])


class Comment(models.Model):
    post = models.ForeignKey(product, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    reply = models.ForeignKey('self', null=True, related_name='replies',
                              on_delete=models.CASCADE)  # 'Comment'= 'self' this is called recursive relationship
    content = models.TextField(max_length=160)
    timestamp = models.DateField(auto_now_add=True)  # when the object is first created auto now add means

    def __str__(self):
        return '{}-{}'.format(self.post.product_name, str(self.user.username))


class Orders(models.Model):
    order_id = models.BigAutoField(primary_key=True)
    items_details = models.TextField(max_length=5000, default="")
    items_json = models.CharField(max_length=1000, default="")
    amount = models.IntegerField(default="0")
    name = models.CharField(max_length=90)
    email = models.EmailField(null=False, default="@gmail.com")
    address = models.CharField(max_length=200)
    update_desc = models.CharField(max_length=20, default="")
    timestamp = models.DateField(default=timezone.now)
    phone = models.CharField(max_length=13)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.CharField(max_length=30)

    # OrderUpdateStatus


class OrderCome(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(
        auto_now_add=True)  # time when the object is first created and auto_now means every time the object is saved

    def __str__(self):
        return self.update_desc[:15] + "..."


class OrderReceived(models.Model):
    received_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    name = models.CharField(max_length=90)
    address = models.CharField(max_length=200)
    items_details = models.TextField(max_length=5000)
    amount = models.IntegerField()

    def __str__(self):
        return self.name


# class OrderDelivered(models.Model):
#     delivered_id    = models.AutoField(primary_key=True)
#     order_id        = models.IntegerField(default="")
#     name            = models.CharField(max_length=90)
#     address         = models.CharField(max_length=200)
#     items_details   = models.TextField(max_length=5000)
#     def __str__(self):
#         return self.name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50, default="")
    timestamp = models.DateTimeField(default=timezone.now)
    phone = models.CharField(max_length=13, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name
