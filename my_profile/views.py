from django.shortcuts import render


# Create your views here.
def my_profile(request):
    return render(request, 'my_profile/index.html')
