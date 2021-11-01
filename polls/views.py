from django.http import HttpResponse


def index(request):
    return HttpResponse("Привет. Вы на странице опроса!")
