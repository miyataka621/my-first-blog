from django.contrib import admin
from .models import Post
#前回定義したPostモデルをimport

#Adminページ（管理画面）上で見えるようにするため、admin.site.register(Post)でモデルを登録する
admin.site.register(Post)
