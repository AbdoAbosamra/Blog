from django.shortcuts import render , redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import Profile
from django.http import HttpResponse
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
@login_required
def profile(request):
    #Profile.objects.get_or_create(user=request.user) # get_or_create is a method of model
    u_form = UserUpdateForm()
    p_form = ProfileUpdateForm()

    context ={ 
        'u_form':u_form,
        'p_form':p_form,
        
    }
    
    return render(request , 'users/profile.html' , context)
'''''
def fixme(request):
    users = User.objects.all()
    for user in users:
        obj, created = Profile.objects.get_or_create(user=user)
        print(user.username,' : ',created)
    print("all done")
    return HttpResponse("It's done.")'''