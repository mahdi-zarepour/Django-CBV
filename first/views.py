from django.shortcuts import render



def home(request):
    return render(request=request, template_name='first/home.html')