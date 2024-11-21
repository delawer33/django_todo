from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    model = User
    fields = ['email', 'username']
    list_display = ['email','password']

admin.site.register(User, UserAdmin)
