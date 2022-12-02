from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from . models import User


class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label='password',max_length=100 , widget=forms.PasswordInput)
    password2 = forms.CharField(label='confirm password' , max_length=100 , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','phone_number','full_name']

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2'] :
            raise ValidationError('password dont match')
        return cd['password']

    def cave(self):
        user = super().sava(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserchangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you can change password using <a href=\"../password/\" >this form</a>')
    class Meta:
        model = User
        fields = ['email','phone_number','full_name','password','last_login']
























