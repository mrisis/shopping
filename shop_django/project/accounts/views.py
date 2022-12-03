from django.shortcuts import render , redirect
from django.views import View
from . forms import RegisterationForm , VerifyCodeForm
from django.contrib import messages
from utils import send_sms_otp_code
from . models import OtpCode , User
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
            send_sms_otp_code(form.cleaned_data['phone_number'] , random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone_number'] , code=random_code )
            request.session['user_registeration_info'] = {
                'phone_number':form.cleaned_data['phone_number'],
                'email':form.cleaned_data['email'],
                'full_name':form.cleaned_data['full_name'],
                'password':form.cleaned_data['password']
            }
            messages.success(request,'successfully send otp code','success')
            return redirect('accounts:verify_code')
        return render(request , 'accounts/register.html' , {'form':form})



class UserRegisterVerifyView(View):
    form_class = VerifyCodeForm
    def get(self,request):
        form = self.form_class
        return render(request,'accounts/verify.html',{'form':form})

    def post(self,request):
        user_session = request.session['user_registeration_info']
        code_instance = OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['code'] == code_instance.code:
                User.objects.create_user(phone_number=user_session['phone_number'] , email=user_session['email'] ,
                                         full_name=user_session['full_name'] ,
                                         password=user_session['password'])
                code_instance.delete()
                messages.success(request , 'verify successfully ' , 'success')
                return redirect('home:home')
            else:
                messages.error(request,'this otp code is wrong' , 'danger')
                return redirect('accounts:verify_code')
            return redirect('home:home')

