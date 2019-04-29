from django.db import models

# Create your models here.

class Post(models.Model):
    title=models.CharField(max_length=100)
    published=models.DateTimeField()
    image=models.ImageField(upload_to="media/")
    body=models.TextField()

    def __str__(self): # __は中で内部のみで参照するとき(外部の参照を受けないもの）
        return self.title
    # 管理サイトの名前が変わるため関数だから、外部からは参照されることはない

    def summary(self): # __は中で内部のみで参照するとき(外部の参照を受けないもの）
        return self.body[:3]

