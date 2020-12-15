from django.shortcuts import render,redirect
from .models import Users
import urllib, json


# Create your views here.
def index(request):

    exists = Users.objects.count()
    if "get" in request.POST:
        url = "http://jsonplaceholder.typicode.com/users"
        response = urllib.request.urlopen(url)
        data = json.loads(response.read())
        for d in data:
            name = d['name']
            username = d['username']
            email = d['email']
            catchphrase = d['company']['catchPhrase']
            new_user = Users(name=name,email=email,catchphrase=catchphrase,username=username)
            new_user.save()
        return redirect("/")
    elif "print" in request.POST:
        user_data = Users.objects.all()
    elif 'save' in request.POST:
        print("save")
        username = request.POST.get("username",None)
        catchphrase = request.POST.get("catchphrase",None)
        if username and catchphrase:
            new_user = Users(username=username,catchphrase=catchphrase)
            new_user.save()
    return render(request,"main/index.html",locals())
