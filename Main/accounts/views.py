from django.shortcuts import render, redirect
from django.views import View

from accounts.forms import LoginRegister, CodeRegister, EditProfile
from accounts.models import User, Otp
from products.models import Like,Comment
import jdatetime
from random import randint
from django.contrib.auth import authenticate, login, logout
from utils.sms import send_code
from cart.cart import Cart

class LoginRegisterView(View):
    template_name = 'accounts/LoginRegister.html'
    form_class = LoginRegister
    def get(self, request):
        ctx = {
            'loginRegisterForm': self.form_class()
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if otps := Otp.objects.filter(phone_number=cd.get('phone_number')).first():
                # inst = otps.last()
                now = jdatetime.datetime.now()
                otpexpir = otps.created + jdatetime.timedelta(minutes=2)
                if now < otpexpir:
                    otps.delete()
                    return redirect('accounts:LoginRegister')
                code_random = randint(100000, 999999)
                Otp.objects.create(phone_number=cd.get('phone_number'), code=code_random)
                send_code(phone=cd.get('phone_number'), code=code_random)
                request.session['phone_number'] = {
                    'phone_number': cd.get('phone_number')
                }
                return redirect('accounts:LoginRegisterVerify')

            code_random = randint(100000, 999999)
            Otp.objects.create(phone_number=cd.get('phone_number'), code=code_random)
            send_code(phone=cd.get('phone_number'), code=code_random)
            request.session['phone_number'] = {
                'phone_number': cd.get('phone_number')
            }
            return redirect('accounts:LoginRegisterVerify')

        ctx = {
            'loginRegisterForm': form
        }
        return render(request, self.template_name, ctx)


class LoginRegisterVerifyView(View):
    template_name = 'accounts/LoginRegisterVerify.html'
    form_class = CodeRegister

    def get(self, request):
        ctx = {
            'phone_number': request.session.get('phone_number')['phone_number'],
            'codeForm': CodeRegister
        }
        return render(request, self.template_name, ctx)


    def post(self, request):
        form = self.form_class(request.POST)
        user_phone = request.session.get('phone_number')
        otp_instance = Otp.objects.filter(phone_number=user_phone.get('phone_number')).first()
        if form.is_valid():
            code = form.cleaned_data['code']
            if code != otp_instance:
                now = jdatetime.datetime.now()
                otpexpir = otp_instance.created + jdatetime.timedelta(minutes=2)
                if now < otpexpir:
                    otp_instance.delete()
                    del request.session['phone_number']
            if user := User.objects.filter(phone_number=otp_instance.phone_number).first():
                del otp_instance
                login(request, user)
                return redirect('Home:home')
            else:
                User.objects.create_user(phone_number=otp_instance.phone_number)
                otp_instance.delete()
                return redirect('Home:home')
        ctx = {
            'codeForm': form
        }
        return render(request, self.template_name, ctx)


class LogOutView(View):
    def get(self, request):
        logout(request)
        return redirect('Home:home')


class ProfileView(View):
    template_name = 'accounts/Profile.html'
    form_class = EditProfile

    def get(self, request):
        ctx = {
            'len_cart':Cart(request).__len__(),
            'cart': Cart(request),
            'comments':Comment.objects.filter(user=request.user),
            'likes': Like.objects.filter(user=request.user),
            'form': self.form_class(instance=request.user)
        }
        return render(request, self.template_name, ctx)

    def post(self, request):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:Profile')
        ctx = {
            'cart': Cart(request),
            'form': form
        }
        return render(request, self.template_name, ctx)
