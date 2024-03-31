from django.db import models

class Paper(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()                # URLに含まれる文字列
    body = models.TextField()
    posted_date = models.DateTimeField(auto_now_add=True) # 日付を自動で追加

    def __str__(self): #オブジェクトのタイトルの設定
        return self.title