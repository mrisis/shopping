from django.shortcuts import render , redirect
from django.views import View
from . forms import RegisterationForm , VerifyCodeForm , UserLoginForm , EditProfileForm
from django.contrib import messages
from utils import send_sms_otp_code
from . models import OtpCode , User
import random
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib.auth import views as auth_views

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



class UserLogout(LoginRequiredMixin,View):
    def get(self,request):
        logout(request)
        messages.success(request,'you successfully logged out' , 'success')
        return redirect('home:home')

class UserLoginView(View):
    form_class = UserLoginForm
    template_name = 'accounts/login.html'
    def get(self,request):
        form = self.form_class
        return render(request,self.template_name, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,phone_number=cd['phone_number'] , password=cd['password'])
            if user is not None:
                login(request,user)
                messages.success(request,'you successfully logged in','success')
                return redirect('home:home')
            messages.error(request,'phone number or password is wrong' , 'danger')
        return render(request,self.template_name,{'form':form})


class UserProfileView(LoginRequiredMixin,View):
    def get(selfself,request,user_id):
        user = User.objects.get(id=user_id)
        return render(request,'accounts/profile.html',{'user':user})


class UserPasswordResetView(auth_views.PasswordResetView):
    template_name = 'accounts/password_reset_form.html'
    success_url = reverse_lazy('accounts:password_reset_done')
    email_template_name = 'accounts/password_reset_email.html'

class UserPasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'accounts/password_reset_done.html'


class UserPasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/password_reset_confirm.html'
    success_url = reverse_lazy('accounts:password_reset_complete')


class UserPasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/password_reset_complete.html'


class ProfileEditView(LoginRequiredMixin,View):
    form_class = EditProfileForm
    def get(self,request):
        form = self.form_class(instance=request.user)
        return render(request , 'accounts/edit_profile.html',{'form':form})

    def post(self,request):
        form = self.form_class(data=request.POST ,files=request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request,'your profile successfully updated' , 'success')
            return redirect('accounts:user_profile' , request.user.id)
        return render(request , 'accounts/edit_profile.html' , {'form':form})























