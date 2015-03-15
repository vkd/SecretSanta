from django.shortcuts import render

# Create your views here.


def rooms(request):
    context = {'nbar': 'rooms'}
    return render(request, 'members.html', context)


def members(request):
    context = {'nbar': 'members'}
    return render(request, 'members.html', context)


def signin(request):
    context = {'nbar': 'signin'}
    return render(request, 'signin.html', context)
