from django.http import HttpResponse

def index(request):
    return HttpResponse("神秘海域")

def login(request):
    return redirect("/index")
