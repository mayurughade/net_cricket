from django.db import models

# Create your models here.

# class MyModel(models.Model):
#     field1 = models.CharField(max_length=100)
#     field2 = models.IntegerField()

#     class Meta:
#         db_table = 'users_data'
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.TextField()
    message = models.TextField()
    class Meta:
      db_table = "contact"

class Tieup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True)
    message = models.TextField(null=True)
    mobile = models.TextField(null=True)
    profile = models.TextField(null=True)
    instagram_id = models.TextField(null=True)
    class Meta:
      db_table = "tieup"

