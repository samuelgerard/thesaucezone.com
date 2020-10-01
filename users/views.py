from django.shortcuts import render, redirect
from django.contrib import messages #for things like flash message
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save() #automatically hashes password and other things in the background
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created, you can now login at anytime!')#flash message
            return redirect('login') #name given to URL patten for home page
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})

@login_required #<------
def profile(request):
    #sends in the new data
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST,instance = request.user) #populates the form with the current users information
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance =request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Profile Saved!')
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance = request.user) 
        p_form = ProfileUpdateForm(instance =request.user.profile)
    context ={
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)


#message.debug
#message.info
#message.success
#message.warning
#message.roor