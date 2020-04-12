from django.urls import path    #path関数をインポート
from . import views             #blogアプリの全てののviewをインポート

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #post/<int:pk>/ の部分はURLパターンを指定
]
