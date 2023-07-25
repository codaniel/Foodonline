from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import UserForm

# Create your views here.
def registerUser(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('registerUser')
    else:
        form = UserForm()
        context = {
            'form': form
        }
        return render(request, 'account/registerUser.html',context)