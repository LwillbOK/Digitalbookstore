from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='bookstore-home'),
    path('about/', views.about, name='bookstore-about'),
]
##上述代码定义了一个URL模式，第一个参数是一个字符串
##该单引号之间没有任何字符，那么这个URL模式将匹配根URL,也就是网站的首页
##也就是说当用户访问网站的首页时，Django会调用views.home视图函数
##如果单引号之间有一个或多个空格，那么URL模式将匹配包含相应数量空格的URL
##然而实际的web开发中几乎没有用，因为URL通常不包含空格

##view.home是function 跳转到views.py