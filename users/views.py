from django.shortcuts import redirect, render

from .forms import RegisterForm


def sign_up(request):
    if request.method == "GET":
        form = RegisterForm()
        return render(request, "registration/register.html", {"form": form})
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            return redirect("login")
        else:
            return render(request, "registration/register.html", {"form": form})
