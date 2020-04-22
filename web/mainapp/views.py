from django.contrib.auth import authenticate
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

def index(request):
    return render(request, 'mainapp/index2.html')

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
            return render(request, 'mainapp/index.html')

        else:
            print("실패")
            return HttpResponse(status=401)


    return render(request, 'mainapp/login.html')


def executepy(request):
    import subprocess
    import time

    for i in range(5):
        time.sleep(3)
        subprocess.call(['python', "./readtext.py"])
        print(i)

    return JsonResponse({
        'message': 'success',
    }, json_dumps_params={'ensure_ascii': False})


def kibana_page(request):
    return render(request, 'mainapp/index.html')
