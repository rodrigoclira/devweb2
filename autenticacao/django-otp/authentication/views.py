from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django_otp import user_has_device
from django_otp.decorators import otp_required
from django_otp.plugins.otp_totp.models import TOTPDevice
from django_otp.util import random_hex
import json

from .forms import CustomUserCreationForm, CustomAuthenticationForm, OTPVerificationForm, OTPSetupForm
from .models import UserProfile


def home(request):
    """Home page view"""
    return render(request, 'authentication/home.html')


def register(request):
    """User registration view"""
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'authentication/register.html', {'form': form})


def user_login(request):
    """User login view"""
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                # Check if user has OTP enabled
                try:
                    profile = UserProfile.objects.get(user=user)
                    if profile.is_otp_enabled:
                        # Store user in session for OTP verification
                        request.session['pre_otp_user_id'] = user.id
                        return redirect('otp_verify')
                    else:
                        login(request, user)
                        messages.success(request, f'Welcome back, {username}!')
                        return redirect('dashboard')
                except UserProfile.DoesNotExist:
                    # Create profile if it doesn't exist
                    UserProfile.objects.create(user=user)
                    login(request, user)
                    messages.success(request, f'Welcome back, {username}!')
                    return redirect('dashboard')
    else:
        form = CustomAuthenticationForm()
    return render(request, 'authentication/login.html', {'form': form})


def user_logout(request):
    """User logout view"""
    logout(request)
    messages.success(request, 'You have been logged out successfully.')
    return redirect('home')


@login_required
def dashboard(request):
    """User dashboard view"""
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    context = {
        'user': request.user,
        'profile': profile,
        'has_otp_device': user_has_device(request.user)
    }
    return render(request, 'authentication/dashboard.html', context)


@login_required
def otp_setup(request):
    """OTP setup view"""
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)
    
    if profile.is_otp_enabled:
        messages.info(request, 'OTP is already enabled for your account.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        form = OTPSetupForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['otp_token']
            
            # Get the TOTP device
            try:
                device = TOTPDevice.objects.get(user=request.user, name='default')
                if device.verify_token(token):
                    # Confirm the device and enable OTP
                    device.confirmed = True
                    device.save()
                    profile.is_otp_enabled = True
                    profile.save()
                    messages.success(request, 'OTP has been successfully enabled for your account!')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid OTP token. Please try again.')
            except TOTPDevice.DoesNotExist:
                messages.error(request, 'OTP device not found. Please try again.')
    else:
        form = OTPSetupForm()
    
    # Generate QR code
    qr_code_base64, secret_key = profile.get_qr_code()
    
    context = {
        'form': form,
        'qr_code': qr_code_base64,
        'secret_key': secret_key,
        'user': request.user
    }
    return render(request, 'authentication/otp_setup.html', context)


def otp_verify(request):
    """OTP verification view for login"""
    # Check if user is in session for OTP verification
    user_id = request.session.get('pre_otp_user_id')
    if not user_id:
        messages.error(request, 'Session expired. Please log in again.')
        return redirect('login')
    
    try:
        from django.contrib.auth.models import User
        user = User.objects.get(id=user_id)
    except User.DoesNotExist:
        messages.error(request, 'User not found. Please log in again.')
        return redirect('login')
    
    if request.method == 'POST':
        form = OTPVerificationForm(request.POST)
        if form.is_valid():
            token = form.cleaned_data['otp_token']
            
            # Verify OTP token
            try:
                device = TOTPDevice.objects.get(user=user, name='default', confirmed=True)
                if device.verify_token(token):
                    # Login the user and clear session
                    login(request, user)
                    del request.session['pre_otp_user_id']
                    messages.success(request, f'Welcome back, {user.username}!')
                    return redirect('dashboard')
                else:
                    messages.error(request, 'Invalid OTP token. Please try again.')
            except TOTPDevice.DoesNotExist:
                messages.error(request, 'OTP device not found. Please contact support.')
    else:
        form = OTPVerificationForm()
    
    context = {
        'form': form,
        'username': user.username
    }
    return render(request, 'authentication/otp_verify.html', context)


@login_required
def disable_otp(request):
    """Disable OTP for user"""
    if request.method == 'POST':
        try:
            profile = UserProfile.objects.get(user=request.user)
            # Delete TOTP devices
            TOTPDevice.objects.filter(user=request.user).delete()
            # Disable OTP in profile
            profile.is_otp_enabled = False
            profile.save()
            messages.success(request, 'OTP has been disabled for your account.')
        except UserProfile.DoesNotExist:
            messages.error(request, 'Profile not found.')
    
    return redirect('dashboard')


@otp_required
def secure_view(request):
    """A secure view that requires OTP verification"""
    return render(request, 'authentication/secure.html', {
        'user': request.user,
        'message': 'This is a secure area that requires OTP verification!'
    })

