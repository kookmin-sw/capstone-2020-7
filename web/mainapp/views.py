from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def index(request):
    return render(request, 'mainapp/index.html')

@csrf_exempt
def login(request):

    if request.method == 'POST':
        #print("리퀘스트 로그" + str(request.body))
        id = request.POST.get('userid','')
        pw = request.POST.get('userpw', '')
        #print("id = " + id + " pw = " + pw)

        result = authenticate(username=id, password=pw)

        if result :
            print("로그인 성공!")
            return HttpResponse(status=200)
        else:
            print("실패")
            return HttpResponse(status=401)


    return render(request, 'mainapp/login.html')