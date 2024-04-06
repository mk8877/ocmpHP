from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    name_roman = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True)
    research = models.CharField(max_length=100)
    comment = models.TextField()
    hometown = models.CharField(max_length=100)
    is_AssistantProfessor = models.BooleanField(default=False)
    is_Researcher = models.BooleanField(default=False)
    is_PhD = models.BooleanField(default=False)
    is_Master2 = models.BooleanField(default=False)
    is_Master1 = models.BooleanField(default=False)
    is_Bachelor = models.BooleanField(default=False)
    is_public = models.BooleanField(default=True)

    def __str__(self):
        return self.name