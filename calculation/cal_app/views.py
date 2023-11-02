from django.shortcuts import render, redirect
from .models import Cal

# Create your views here.
def main(request):
    return render(request, 'main.html')

def history(request):
    return render(request, 'history.html')

def output(request):
    return render(request, 'output.html')

# def new(request):
#     title = request.GET.get('title')
#     number1 = request.GET.get('number1')
#     oper = request.GET.get('oper')
#     number2 = request.GET.get('number2')

#     post = Cal()
#     post.title = title
#     post.number1 = number1
#     post.oper = oper
#     post.number2 = number2

#     return redirect(f'/cal_app/{cal.id}/')
