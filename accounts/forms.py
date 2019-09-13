from django import forms
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from django.contrib.auth.models import User
from accounts.models import Profile

class RegistrationForm(UserCreationForm):

    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'password1',
            'password2'
        )

    def save(self,commit=True):
        user = super(RegistrationForm,self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']


        if commit:
            user.save()

            return user

class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = (
            'description',
            'location',
            'phone_number',
            'birth_date',

        )

    def save(self,commit=True):
        profile = super(ProfileForm,self).save(commit=False)
        profile.description = self.cleaned_data['description']
        profile.location = self.cleaned_data['location']
        profile.phone_number = self.cleaned_data['phone_number']
        profile.birth_date = self.cleaned_data['birth_date']
        id = User.objects.latest('date_joined')
        profile.user = id


        if commit:
            profile.save()


            return profile
