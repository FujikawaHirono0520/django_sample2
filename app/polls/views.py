from django.http import HttpResponse


def index(request):
    return HttpResponse("HELLO!!!!!!!!WHO ARE YOU?")