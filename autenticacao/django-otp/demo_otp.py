#!/usr/bin/env python3
"""
Django OTP Demo Script

This script demonstrates how to generate and verify TOTP codes programmatically.
Useful for testing the OTP functionality without a physical authenticator app.

Usage:
    python demo_otp.py
"""

import pyotp
import qrcode
import io
import base64
from datetime import datetime

def generate_secret():
    """Generate a new TOTP secret key."""
    return pyotp.random_base32()

def generate_qr_code(secret, username="testuser", issuer="Django OTP Example"):
    """Generate QR code for TOTP setup."""
    totp = pyotp.TOTP(secret)
    provisioning_uri = totp.provisioning_uri(
        name=username,
        issuer_name=issuer
    )
    
    # Create QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(provisioning_uri)
    qr.make(fit=True)
    
    # Generate QR code image
    img = qr.make_image(fill_color="black", back_color="white")
    
    return provisioning_uri, img

def generate_totp_code(secret):
    """Generate current TOTP code."""
    totp = pyotp.TOTP(secret)
    return totp.now()

def verify_totp_code(secret, code):
    """Verify a TOTP code."""
    totp = pyotp.TOTP(secret)
    return totp.verify(code)

def demo():
    """Run the OTP demonstration."""
    print("=" * 60)
    print("Django OTP Demonstration")
    print("=" * 60)
    
    # Generate a secret key
    secret = generate_secret()
    print(f"Generated Secret Key: {secret}")
    print()
    
    # Generate QR code
    provisioning_uri, qr_img = generate_qr_code(secret)
    print(f"Provisioning URI: {provisioning_uri}")
    print()
    
    # Save QR code image
    qr_img.save("demo_qr_code.png")
    print("QR code saved as 'demo_qr_code.png'")
    print("You can scan this with your authenticator app for testing.")
    print()
    
    # Generate current TOTP code
    current_code = generate_totp_code(secret)
    print(f"Current TOTP Code: {current_code}")
    print(f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    # Verify the code
    is_valid = verify_totp_code(secret, current_code)
    print(f"Code Verification: {'✓ Valid' if is_valid else '✗ Invalid'}")
    print()
    
    # Show how to use in Django shell
    print("To test in Django shell:")
    print("=" * 40)
    print("python manage.py shell")
    print()
    print("from django_otp.plugins.otp_totp.models import TOTPDevice")
    print("from django.contrib.auth.models import User")
    print()
    print("# Get user")
    print("user = User.objects.get(username='testuser')")
    print()
    print("# Get or create TOTP device")
    print("device = TOTPDevice.objects.get(user=user, name='default')")
    print()
    print("# Verify code")
    print(f"device.verify_token('{current_code}')")
    print()
    
    print("Note: TOTP codes change every 30 seconds!")
    print("=" * 60)

if __name__ == "__main__":
    demo()

