from django.db import models

class Paper(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()                # URLに含まれる文字列
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True) # 日付を自動で追加

class Member(models.Model):
    name = models.CharField(max_length=100)
    name_roman = models.CharField(max_length=100)
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