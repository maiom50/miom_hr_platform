from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Resume

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'email', 'role', 'is_staff')
    fieldsets = UserAdmin.fieldsets + (
        ('Роль', {'fields': ('role',)}),
    )

@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created_at')
    list_filter = ('owner__role', 'created_at')
    search_fields = ('title', 'owner__username')

admin.site.register(User, CustomUserAdmin)