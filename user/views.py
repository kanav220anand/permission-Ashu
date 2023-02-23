from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import createUserform
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from rest_framework import permissions

# from .decorators import unauthenticated_user,allowed_user

from django.views.generic import TemplateView


class IndexPageView(TemplateView):
    template_name = 'index.html'

class ProductPageView(TemplateView):
    template_name = 'products.html'

class Page2PageView(TemplateView):
    permissions = ("user.can_view_page2", permissions.IsAuthenticated)
    template_name = 'page2.html'

class Page3PageView(TemplateView):
    template_name = 'page3.html'

class Page4PageView(TemplateView):
    template_name = 'page4.html'

class Page5PageView(TemplateView):
    template_name = 'page5.html'


# class ChangeLanguageView(TemplateView):
#     template_name = 'main/change_language.html'


# @unauthenticated_user
def register(request):
    form =  createUserform()
    
    if request.method == "POST":
        form =  createUserform(request.POST)
        if form.is_valid():
            user =form.save()
            group = Group.objects.get_or_create(name="customer")
            user.groups.add(group)
            return redirect('login')
    context  = {'form':form}
    return render(request,"register.html",context)



def loginPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username =username,password= password )
        if user is not None:
            login(request,user)
            return redirect('home')
    return render(request,"login.html")


def logoutUser(request):
    logout(request)
    return redirect('login')


