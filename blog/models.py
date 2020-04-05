from django.conf import settings
from django.db import models
from django.utils import timezone

#モデルを定義する
class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
            #models.ForeignKey – これは他のモデルへのリンク
    title = models.CharField(max_length=200)
            #models.CharField – 文字数が制限されたテキストを定義するフィールド
    text = models.TextField()
            #models.TextField – これは制限無しの長いテキスト用
    created_date = models.DateTimeField(default=timezone.now)
            #models.DateTimeField – 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    #def publish(self): ブログを公開するメソッドそのもの
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
