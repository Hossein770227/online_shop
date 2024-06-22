import random
from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from django.utils.translation import gettext as _
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

from datetime import datetime, timedelta, timezone
import pytz


from .forms import UserRegisterForm, VerifyCodeForm
from utils import send_otp_code
from .models import OtpCode, MyUser

class UserRegisterView(View):
    form_class = UserRegisterForm
    def get(self, request):
        form= self.form_class
        return render(request, 'registration/user_register.html', {'form':form})
    
    def post(self, request):
        form =self.form_class(request.POST)
        if form.is_valid():
            otp = OtpCode.objects.filter(phone_number = form.cleaned_data['phone'])
            if otp.exists():
                messages.error(request, _('we send your code alreedy'))
                return redirect('accounts:verify_code')
            random_code = random.randint(1000, 9999)
            send_otp_code(form.cleaned_data['phone'], random_code)
            OtpCode.objects.create(phone_number=form.cleaned_data['phone'], code=random_code)
            request.session['user_registration_info']={
                'phone_number':form.cleaned_data['phone'],
                'full_name':form.cleaned_data['full_name'],
                'password':form.cleaned_data['password2'],
            }
            messages.success(request, _('we sent you a code'))
            return redirect('accounts:verify_code')
        return render(request, 'registration/user_register.html', {'form':form})



class UserRegisterCodeView(View):
    form_class=VerifyCodeForm
    def get(self, request):
        form = self.form_class
        return render(request, 'registration/verify_code.html', {'form':form})

    def post(self, request):
        user_session = request.session['user_registration_info']
        code_instance =OtpCode.objects.get(phone_number=user_session['phone_number'])
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            now = datetime.now(tz=pytz.timezone('Asia/Tehran'))
            expired_time = code_instance.date_time_created + timedelta (minutes=2)
            if OtpCode:
                if now > expired_time:
                    code_instance.delete()
                    messages.error(request, _('your code time is out'))
                    return redirect ('accounts:user_register')          
            if now > expired_time:
                code_instance.delete()
                messages.error(request, _('your code time is out'))
                return redirect ('accounts:verify_code')
            
            if cd['code']==code_instance.code:
                user=MyUser.objects.create_user(user_session['phone_number'], user_session['full_name'], user_session['password'])
                code_instance.delete()
                messages.success(request, _('you register'))
                login(request, user)
                return redirect('pages:home')
            else:
                messages.error(request, _('this code is wrong'))
                return redirect('accounts:verify_code')
        return redirect('pages:home')
    


def login_view(request):
    if request.method =='POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user =form.get_user()
            login(request, user)
            messages.success(request, _('you successfully login'))
            return redirect('products:product_list')
    form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form':form})


def logout_view(request):
    if request.method =='POST':
        logout(request)
        messages.error(request, _('you successfully logouted'))
        return redirect('products:product_list')

# password change

def password_change_view(request):
    if request.method =='POST':
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request, _('your password sucessfully changed'))
            return redirect('pages:home')
        return redirect('accounts:change_password')
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'registration/password_change.html',{'form':form})