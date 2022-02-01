from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(email=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password/password_reset_email.txt"
					c = {
					"email":user.email,
					'domain':'127.0.0.1:8000',
					'site_name': 'Website',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'admin@example.com' , [user.email], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					messages.success(request, 'A message with reset password instructions has been sent to your inbox.')
					return redirect ("blog-home")
			messages.error(request, 'An invalid email has been entered.')
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password/reset_password.html", context={"password_reset_form":password_reset_form})