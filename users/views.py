from django.shortcuts import render

def login():
    return render(request, 'users/login.html')

def logout():
    return render(request, 'users/logout.html')