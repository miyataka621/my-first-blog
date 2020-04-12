from django.urls import path    #path関数をインポート
from . import views             #blogアプリの全てののviewをインポート

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    #post/<int:pk>/ の部分はURLパターンを指定
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]
