from core.models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from core.models import AuthUser


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class UserInline(admin.StackedInline):
    model = AuthUser
    can_delete = False
    verbose_name_plural = "user"

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = [UserInline]

# Re-register UserAdmin
admin.site.register(Embedding)
admin.site.register(Language)
admin.site.register(Library)
admin.site.register(AuthUser)
