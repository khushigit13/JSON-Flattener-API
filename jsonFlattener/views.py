from django.http import HttpResponse

def homePage(req):
    return HttpResponse("Hello World!")
