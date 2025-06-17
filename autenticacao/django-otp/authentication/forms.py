from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from .models import UserProfile


class CustomUserCreationForm(UserCreationForm):
    """Custom user registration form with additional fields"""
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=15, required=False)
    
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password1", "password2")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            # Create user profile
            UserProfile.objects.create(
                user=user,
                phone_number=self.cleaned_data.get("phone_number", "")
            )
        return user


class CustomAuthenticationForm(AuthenticationForm):
    """Custom login form with styling"""
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Add CSS classes for styling
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label


class OTPVerificationForm(forms.Form):
    """Form for OTP token verification"""
    otp_token = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control text-center',
            'placeholder': 'Enter 6-digit code',
            'autocomplete': 'off',
            'style': 'font-size: 1.5em; letter-spacing: 0.5em;'
        })
    )
    
    def clean_otp_token(self):
        token = self.cleaned_data.get('otp_token')
        if not token.isdigit():
            raise forms.ValidationError("OTP must contain only digits.")
        return token


class OTPSetupForm(forms.Form):
    """Form for confirming OTP setup"""
    otp_token = forms.CharField(
        max_length=6,
        min_length=6,
        widget=forms.TextInput(attrs={
            'class': 'form-control text-center',
            'placeholder': 'Enter 6-digit code',
            'autocomplete': 'off',
            'style': 'font-size: 1.5em; letter-spacing: 0.5em;'
        })
    )
    
    def clean_otp_token(self):
        token = self.cleaned_data.get('otp_token')
        if not token.isdigit():
            raise forms.ValidationError("OTP must contain only digits.")
        return token

