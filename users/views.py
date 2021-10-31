from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisrationForm

def register(request):
    if request.method =='POST':
        form = UserRegisrationForm(request.POST)
        if form.is_valid():
            form.save() # save user to database
            username = form.cleaned_data.get('username') # cleaned_data is a dictionary
            messages.success(request, f'Your Account has been Created for! You now able to login') # f string
            return redirect('login')
        else:
            messages.error(request, 'Error')
    else:
        form = UserRegisrationForm()   # To show the form without request.
        
    return render(request, 'users/register.html' , {'form' : form})
