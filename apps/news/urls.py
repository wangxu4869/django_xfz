from django.urls import path
from . import views

app_name='news'
urlpatterns=[
    path('int:<news_id>/',views.news_detail,name='news_detail'),
    path('list/',views.news_list,name='news_list'),
    path('public_comment/',views.public_comment,name='public_comment'),
]
#第一个必须加int:,不然报错ValueError: invalid literal for int() with base 10

