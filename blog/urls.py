from django.urls import path    #path関数をインポート
from . import views             #blogアプリの全てののviewをインポート

urlpatterns = [
    path('', views.post_list, name='post_list'),
]
