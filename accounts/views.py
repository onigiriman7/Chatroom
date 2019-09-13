from django.shortcuts import render,redirect
from django.urls import reverse
from accounts.forms import RegistrationForm,ProfileForm
from django.forms.models import inlineformset_factory
from accounts.models import Profile
from django.contrib.auth.models import User

def register(request):
    # RegisterInLineFormset = inlineformset_factory(User, Profile, form = ProfileForm,fields = (
    #     'description',
    #     'location',
    #     'phone_number',
    #     'birth_date' ),
    #     can_delete=False)
    if request.method == 'POST':
        userform = RegistrationForm(request.POST)
        profileform = ProfileForm(request.POST)
        # reg_form = RegistrationForm(request.POST)
        if userform.is_valid() and profileform.is_valid() :
            form1 = userform.save()
            form2 = profileform.save()
            # if registerFormset.is_valid():
            #     registerFormset.save()
            return redirect(reverse('accounts:login'))
    else:
        userform = RegistrationForm()
        profileform = ProfileForm()
    args = {'form1':userform, 'form2':profileform}

    return render(request,'accounts/reg_form.html',args)
