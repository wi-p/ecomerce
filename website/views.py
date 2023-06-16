from django.shortcuts import render,redirect
from .models import Book
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib import messages

# Create your views here.



def indexPage(request):
    return render(
        request,
        'website/index.html',
        {'newbooks':Book.objects.all()[:]}
    )

def resultsPage(request):
    return render(
        request,
        'website/results.html',
        {'results':Book.objects.filter(title__contains = request.POST.get('search'))}
    )

def bookPage(request, bk_isbn):
    return render(
        request,
        'website/book.html',
        {'book':Book.objects.get(isbn = bk_isbn)}
    )

def mostSellersPage(request):
    return render(
        request,
        'website/mostsellers.html',
        {'books':Book.objects.order_by('download_number')}
    )

def forKidsPage(request):
    return render(
        request,
        'website/forkids.html',
        {'books':Book.objects.filter(genre = 'kids')}
    )

def forAdultsPage(request):
    return render(
        request,
        'website/foradults.html',
        {'books':Book.objects.filter(age = '18')}
    )

def loginPage(request):
    if request.method == 'POST':
        user = authenticate(
            request,
            username = request.POST.get('username'),
            password = request.POST.get('password')
        )

        if user is not None:
            print(user.is_authenticated)
            login(request, user)

            return HttpResponseRedirect(reverse('website:index'))
        else:
            return render(request,'website/login.html',{'error':'User does not exist'})
    else:
        return render(
            request,
            'website/login.html',
            {}
        )

def signupPage(request):
    if request.method == 'POST':
        user = User.objects.create_user(
                username = request.POST.get('username'),
                password = request.POST.get('password'),
                first_name = request.POST.get('firstname'),
                last_name = request.POST.get('lastname'),
                email = request.POST.get('email')
        )

        user.save()

        return HttpResponseRedirect(reverse('website:index'))
    else:
        return render(
            request,
            'website/signup.html',
            {}
        )

def logoutPage(request):
    logout(request)

    return HttpResponseRedirect(reverse('website:login'))

