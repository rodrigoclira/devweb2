from django.contrib import admin
from .models import Professor
# Register your models here.

admin.site.register(Professor)
admin.site.index_template = 'memcache_status/admin_index.html'


