from django.db import models
from django.contrib.auth.models import User
from django_otp.models import Device
import qrcode
import io
import base64


class UserProfile(models.Model):
    """Extended user profile to store additional information"""
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_otp_enabled = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.username} - OTP: {self.is_otp_enabled}"

    def get_qr_code(self):
        """Generate QR code for TOTP setup"""
        from django_otp.plugins.otp_totp.models import TOTPDevice
        
        # Get or create TOTP device for this user
        device, created = TOTPDevice.objects.get_or_create(
            user=self.user,
            name='default',
            defaults={'confirmed': False}
        )
        
        if not device.confirmed:
            # Generate QR code URL
            qr_url = device.config_url
            
            # Create QR code
            qr = qrcode.QRCode(version=1, box_size=10, border=5)
            qr.add_data(qr_url)
            qr.make(fit=True)
            
            # Create QR code image
            img = qr.make_image(fill_color="black", back_color="white")
            
            # Convert to base64 for display in template
            buffer = io.BytesIO()
            img.save(buffer, format='PNG')
            buffer.seek(0)
            qr_code_base64 = base64.b64encode(buffer.getvalue()).decode()
            
            return qr_code_base64, device.key
        
        return None, None

