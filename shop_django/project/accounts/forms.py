from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from . models import User , OtpCode
from django.utils.translation import gettext_lazy as _

class UserCreationForm(forms.ModelForm):
    password1=forms.CharField(label=_('password'),max_length=100 , widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('confirm password') , max_length=100 , widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email','phone_number','full_name']

    def clean_password2(self):
        cd=self.cleaned_data
        if cd['password1'] and cd['password2'] and cd['password1'] != cd['password2'] :
            raise ValidationError(_('password dont match'))
        return cd['password2']

    def save(self,commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserchangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField(help_text='you can change password using <a href=\"../password/\" >this form</a>')
    class Meta:
        model = User
        fields = ['email','phone_number','full_name','password','last_login']


class RegisterationForm(forms.Form):
    email = forms.EmailField(label='',widget=forms.TextInput(attrs={'class':'form-control','placeholder':_('Email')}))
    full_name=forms.CharField(label='',max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':_('Full Name')}))
    phone_number = forms.CharField(label='',max_length=11,widget=forms.TextInput(attrs={'class':'form-control','placeholder':_('Phone Number')}))
    password = forms.CharField(label='',widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':_('Password')}))


    def clean_email(self):
        email = self.cleaned_data['email']
        user = User.objects.filter(email=email)
        if user :
            raise ValidationError(_('this email already exist'))
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data['phone_number']
        user = User.objects.filter(phone_number=phone_number)
        if user :
            raise ValidationError(_('this phone number already exist'))
        OtpCode.objects.filter(phone_number=phone_number).delete()
        return phone_number





class VerifyCodeForm(forms.Form):
    code = forms.IntegerField(widget=forms.PasswordInput(attrs={'class':'form-control','palceholder':_('code')}))


class UserLoginForm(forms.Form):
    phone_number = forms.CharField(label='' , widget=forms.TextInput(attrs={'class':'form-control','placeholder':_('Phone Number OR Email')}))
    password = forms.CharField(label='',max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control' , 'placeholder':_('password')}))


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields=('email','phone_number' , 'full_name','image')
        widgets = {
            'email':forms.TextInput(attrs={'class':'form-control','placeholder':_('Email')}),
            'phone_number':forms.TextInput(attrs={'class':'form-control','placeholder':_('Phone Number')}),
            'full_name':forms.TextInput(attrs={'class':'form-control','placeholder':_('Full Name')}),
            'image':forms.FileInput(attrs={'class':'form-control','placeholder':_('Image')}),
        }

        labels = {
            'email':_('Email'),
            'phone_number':_('Phone Number'),
            'full_name':_('Full Name'),
            'image':_('Image'),
        }


















