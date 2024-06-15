from django.shortcuts import render, redirect
from .forms import RegisterUserForm
# Create your views here.
def signupView(request):
    if request.user.is_authenticated:
        return redirect('home')
    form = RegisterUserForm()
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    context = {'form':form}
    return render(request, 'users/register.html', context)
