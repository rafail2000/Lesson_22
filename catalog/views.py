from django.shortcuts import render

def home(request):
    """
    Контроллер страницы home.html
    """

    return render(request, 'home.html')
