from django.shortcuts import render , redirect
from django.views import View
from . forms import RegisterationForm
from django.contrib import messages
from utils import send_otp_sms_code
from . models import OtpCode
import random


class UserRegisterView(View):
    form_class = RegisterationForm
    def get(self,request):
        form = self.form_class
        return render(request,'accounts/register.html',{'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            random_code = random.randint(1000,9999)
            send_otp_sms_code(form.cleaned_data['phone_number'] , random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'] , code=random_code )
            request.session['user_registeration_info'] = {
                'phone_number':form.cleaned_data['phone_number'],
                'email':form.cleaned_data['email'],
                'full_name':form.cleaned_data['full_name'],
                'password':form.cleaned_data['password']
            }
            messages.success(request,'successfully registered','success')
            return redirect('accounts:verify_code')
        return render(request , 'accounts/register.html' , {'form':form})





