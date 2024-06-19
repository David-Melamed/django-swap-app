from django.contrib.auth.decorators import login_required
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from django.shortcuts import render, redirect
from .models import all_items, users
from . import forms


def get_my_profile(request):
    active_user = request.user.username
    print("active user " + active_user)
    userinfo = users.objects.filter(username=active_user).values()
    return render(request, 'my_app_templates/my_profile.html', {'userinfo': userinfo})


def get_all_items(request):
    items = all_items.objects.all().order_by('date')
    return render(request, 'my_app_templates/all_items.html', {'all_items': items})


def get_item_details(request, slug):
    item_details = all_items.objects.filter(slug=slug).values()
    print("item_details:")
    print(item_details)
    return render(request, 'my_app_templates/item_details.html', {'item_details': item_details})


def login_page(request):
    form = AuthenticationForm()
    return render(request, 'my_app_templates/main.html', {"form": form})


def user_signup_details(request):
    if request.method == "POST":
        form = forms.SignupInformation(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username = request.user
            instance.save()
            return redirect('my_app_name:myprofile')
    else:
        form = forms.SignupInformation()
    return render(request, 'my_app_templates/user_signup_details.html', {"form": form})


@login_required(login_url="/")
def add_item(request):
    if request.method == "POST":
        form = forms.CreateItem(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('my_app_name:all_items')
    else:
        form = forms.CreateItem()
    return render(request, 'my_app_templates/add_item.html', {"form": form})
