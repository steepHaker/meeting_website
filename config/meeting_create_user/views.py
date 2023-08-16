from django.views import View
from rest_framework import generics, status
from urllib import request
from django.shortcuts import  get_object_or_404, render, redirect
from .serializers import UserInfoSerializer
from .forms import RegistrationForms, LoginForm, UserInfoForm
from django.contrib.auth import authenticate, login
from .models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import UpdateAPIView
from rest_framework.response import Response
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

def UserRegistr(request):
    if request.method == 'POST':
        form = RegistrationForms(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            repeatpassword = form.cleaned_data['repeatpassword']

            if password == repeatpassword:
                user = User.objects.create_user(username=username, email=email, password=password)
                return redirect('login')  # Redirect to login page after successful registration
            else:
                # Passwords don't match, display an error message or handle it accordingly
                return render(request, 'reg&log/registration.html', {'form': form, 'error': 'Passwords do not match.'})
    else:
        form = RegistrationForms()
    return render(request, 'reg&log/registration.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                print("User successfully logged in.")

                # При успешном входе создаем запись UserInfo для пользователя, если ее нет
            return redirect('create_user_info')  # Redirect to content page after successful login    
            #     
            # else:
            #     # Invalid login credentials, display an error message or handle it accordingly
            #     return render(request, 'reg&log/login.html', {'form': form, 'error': 'Invalid login credentials'})
    else:
        form = LoginForm()
    return render(request, 'reg&log/login.html', {'form': form})

@login_required
def delete_account(request):
    if request.method == 'POST':
        # Удаляем аккаунт пользователя
        user = request.user
        user.delete()

        # Выполняем выход из аккаунта (логаут)
        logout(request)
        return redirect('registration') 
    else:
        return render(request, 'rest_framework/delete_account.html')

def user_logout(request):
    logout(request)
    return redirect('login')

class CreateUserInfoView(generics.CreateAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        userinfo, created = UserInfo.objects.get_or_create(myuser=user)

        form = UserInfoForm(instance=userinfo)
        context = {
            'form': form,
        }
        return render(request, 'rest_framework/create_user_info.html', context)

    def post(self, request, *args, **kwargs):
        user = request.user
        userinfo, created = UserInfo.objects.get_or_create(myuser=user)

        form = UserInfoForm(request.POST, request.FILES, instance=userinfo)  # Указываем request.FILES

        if form.is_valid():
            form.save()
            # Обновляем связь между User и UserInfo
            userinfo.myuser = user
            userinfo.save()
            return redirect('acquaintance')  # Перенаправление на страницу acquaintance после сохранения

        context = {
            'form': form,
        }
        return render(request, 'rest_framework/create_user_info.html', context)
    
class EditUserInfoView(UpdateAPIView):
    serializer_class = UserInfoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        # Возвращаем объекты UserInfo, связанные с текущим пользователем
        return UserInfo.objects.filter(myuser=self.request.user)

    def get(self, request, *args, **kwargs):
        userinfo = self.get_queryset().first()

        if userinfo:
            form = UserInfoForm(instance=userinfo)
            context = {
                'form': form,
            }
            return render(request, 'rest_framework/edit_user_info.html', context)
        else:
            return Response({'error': 'User info not found'}, status=status.HTTP_404_NOT_FOUND)

    def put(self, request, *args, **kwargs):
        userinfo = self.get_queryset().first()

        if userinfo:
            form = UserInfoForm(request.data, instance=userinfo)
            if form.is_valid():
                form.save()
                return redirect('acquaintance')
            else:
                context = {
                    'form': form,
                }
                return render(request, 'rest_framework/edit_user_info.html', context)
        else:
            return Response({'error': 'User info not found'}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, *args, **kwargs):
        # Обработка POST-запроса для сохранения отредактированных данных
        return self.put(request, *args, **kwargs)

def acquaintance_get(request):
    # Получаем список всех пользователей и их информацию
    all_users_info = UserInfo.objects.all()

    return render(request, 'rest_framework/acquaintance.html', {'all_users_info': all_users_info})

class ProfileView(View):
    template_name = 'rest_framework/profil.html'

    def get(self, request, *args, **kwargs):
        userinfo = UserInfo.objects.get(myuser=request.user)
        context = {
            'userinfo': userinfo
        }
        return render(request, self.template_name, context)

def user_details(request, user_id):
    userinfo = get_object_or_404(UserInfo, myuser_id=user_id)
    context = {
        'userinfo': userinfo
    }
    return render(request, 'rest_framework/user_details.html', context)























