from django.contrib import admin
from core.models import *

# Register your models here.
admin.site.register(Embedding)
admin.site.register(Language)
admin.site.register(Library)
admin.site.register(UserLib)
admin.site.register(UserLang)