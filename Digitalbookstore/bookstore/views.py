from django.shortcuts import render
from django.http import HttpResponse
##写入上行代码
##该行代码的作用是从django.http模块中导入HttpResponse类
##httpResponse类是Django中用于处理HTTP响应的主要工具
##当你创建一个视图函数时，这个函数需要返回一个HttpResponse对象，这个HttpResponse对象包含了发送给客户端的HTTP响应。

from . models import Book, Author
from datetime import datetime
from django.shortcuts import get_object_or_404
from .models import Book
# Create your views here.
def home(request):
    return HttpResponse('<h1>Bookstore Home</h1>')

def about(request):
    return HttpResponse('<h1>Bookstore About</h1>')

##def是python中的关键字
##def承担着定义、接收参数、返回数值、递归、嵌套函数和装饰器等多种功能
##在Django这样的Python Web框架中，def通常用于定于视图函数，处理HTTP请求

def create_book(request):
    author = Author(name ='Author Name', works ='Author Works', contact = 'Author Contact')
    author.save()
    book = Book(title = 'Book Title', description = 'Book Description', pub_date = datetime, price =999.99)
    return render(request, 'bookstore/book_created.html')

#def update_book(request, book_id):
 #   book = get_object_or_404(Book, book_id = book_id)

 #   book.price = request.POST['price']
  #  book.pub_data = request.POST['pub_date']

 #   book.save()

