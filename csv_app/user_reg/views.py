from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect

from .models import UserLoginForm


def homepage(request):
    return render(request, template_name='base.html')


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


'''def login_view(request):
    """ need to FIX
    https://docs.djangoproject.com/en/4.0/topics/auth/default/#how-to-log-a-user-in
    :param request:
    :return:
    """
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('home')
    else:
        # Return an 'invalid login' error message.
        return redirect('home')
'''