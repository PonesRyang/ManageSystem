from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.exceptions import ValidationError

from port.models import User
from window.uilts import to_md5_hex


@api_view(['POST','GET'])
def login(request):
    try:
        if request.method == 'GET':
            return render(request, 'Load/login.html')
        else:
            name = request.data.get('name')
            password = request.data.get('password')
            user = User.objects.filter(username=name).first()
            password = to_md5_hex(password)
            if password == user.password:
                request.session['user'] = user
                return redirect('/')
            raise ValidationError('请输入正确的用户名或密码')
    except:
        data = {'code':400, 'mes':'请输入正确的用户名或密码'}
        return JsonResponse(data)


def get_index(request):
    return render(request,'User/user.html')


def sign(request):
    return render(request,'User/sign.html')


def check_event(request):
    return render(request, 'User/check_event.html')


def add_event(request):
    return render(request, 'User/add_event.html')
