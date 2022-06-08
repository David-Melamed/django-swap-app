from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect


def signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            # log the user in
            return redirect('my_app_name:user_signup_details')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('my_app_name:userinfo')
    else:
        form = AuthenticationForm()

    return render(request, 'my_app_templates/main.html', {"form": form})


def admin_view(request):
    return redirect('/admin')


def logout_view(request):
    # if request.method == "POST":
    logout(request)
    return redirect('my_app_name:main')
