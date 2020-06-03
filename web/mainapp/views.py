from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):

    if request.method == 'POST':
        id = request.POST.get('userid','')
        pw = request.POST.get('userpw', '')

        result = authenticate(username=id, password=pw)

        if result :
            print("로그인 성공!")
            return render(request, 'mainapp/index.html')

        else:
            print("실패")
            return render(request, 'mainapp/login.html')


    return render(request, 'mainapp/login.html')


def kibana_page(request):
    return render(request, 'mainapp/index.html')

def kibana_page2(request):
    return render(request, 'mainapp/index_for_dashboard2.html')

def Login(request):

    if request.method == 'POST':
        id = request.POST.get('userid','')
        pw = request.POST.get('userpw', '')

        result = authenticate(username=id, password=pw)

        if result :
            print("로그인 성공!")
            return render(request, 'mainapp/index.html')

        else:
            print("실패")
            return render(request, 'mainapp/Login.html')


    return render(request, 'mainapp/Login.html')
