from django.shortcuts import render
from django.views import View
from . forms import RegisterationForm


class UserRegisterView(View):
    form_class = RegisterationForm
    def get(self,request):
        form = self.form_class
        return render(request,'home/register.html',{'form':form})

    def post(self,request):
        pass



