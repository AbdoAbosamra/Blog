from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def register(request):
    if request.method =='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username') # cleaned_data is a dictionary
            messages.success(request, f'Account Created for {username}') # f string
            return redirect('home')
        else:
            print(messages.error(request, 'Error'))
    else:
        form = UserCreationForm()   # To show the form without request.
        
    return render(request, 'users/register.html' , {'form' : form})
