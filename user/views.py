from django.http.response import JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import Users

def index(request):
    if request.method == 'GET':
        if 'id' in request.session:
            if request.session['id'] != 0:
                return redirect(reverse('details'))
        return render(request, "login.html")
    else:
        email = request.POST['email']
        password = request.POST['pass']
        if Users.objects.filter(email=email, password=password).exists():
            request.session.set_expiry(300)
            request.session['id'] = Users.objects.get(email=email, password=password).id
            return redirect(reverse('details'))
        else:
            return render(request, "login.html", {'msg': 'Wrong Username and/or Password'})

def signup(request):
    if request.method == 'GET':
        return render(request, "signup.html")
    
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['pass']
        address = request.POST['address']

        if Users.objects.filter(username=username).exists():
            return render(request, "signup.html", {'msg': 'Choose Other Username'})

        elif Users.objects.filter(email=email).exists():
            return render(request, "signup.html", {'msg': 'Email Already Register'})

        else:
            obj = Users(username=username, email=email, password=password, address=address)
            obj.save()
            return redirect(reverse('login'))

def logout(request):
    del(request.session['id'])
    return redirect(reverse('login'))

def user_details(request):
    if 'id' not in request.session:
        return redirect(reverse('login'))
    if request.method == 'GET':
        users = Users.objects.all()
        return render(request, "details.html", {'users':users})

def get_user_details(request, id):
    if request.method == "GET":
        obj = Users.objects.get(pk=id)
        json = {'username':obj.username, 'email':obj.email, 'address':obj.address}
        return JsonResponse(json)

def edit_user_details(request):
    if request.method == "POST":
        username = request.POST['username']
        id = request.POST['id']
        address = request.POST['address']
        email = request.POST['email']

        if Users.objects.filter(username=username).exclude(id=id).exists() or Users.objects.filter(email=email).exclude(id=id).exists():
            users = Users.objects.all()
            return redirect(reverse('details'))

        else:
            Users.objects.filter(id=id).update(username=username, email=email, address=address)
            return redirect(reverse('details'))

def delete_user_details(request, id):
    if request.method == "GET":
        user = Users.objects.get(pk=id)
        user.delete()
        return redirect(reverse('details'))