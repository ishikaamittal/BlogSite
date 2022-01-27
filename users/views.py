from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, updateProfileForm,updateUserForm

# Create your views here.
def Register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your Account has  been created! You can Login now.')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, "register.html", {'form': form})

@login_required
def Profile(request):
    return render (request, 'users/Profile.html')

def profile(request):
    # if request.method == "POST":
    #     userForm = updateUserForm(request.POST, instance= request.user)
    #     profileForm = updateProfileForm(request.POST, 
    #                                     request.FILES,
    #                                     instance=request.user.profile)
    #     if userForm.is_valid() and profileForm.is_valid():
    #         userForm.save()
    #         profileForm.save()
    #         return redirect("profile")
    #     else:
    #         userForm = updateUserForm(instance= request.user)
    #         profileForm = updateProfileForm(instance=request.user.profile)
        
    #     context = {
    #         'userForm': userForm,
    #         'profileForm': profileForm,
    #     }
        return render(request, "Profile.html")