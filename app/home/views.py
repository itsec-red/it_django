from django.http import HttpResponse


def index(request):
    return HttpResponse("My home page")