from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import *

# Register your models here.
admin.site.register(Embedding)
admin.site.register(Language)
admin.site.register(Library)
admin.site.register(UserLib)
admin.site.register(UserLang)
admin.site.register(User, UserAdmin)