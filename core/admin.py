from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from core.models import *

# Register your models here.
class EmbeddingAdmin(admin.ModelAdmin):
    model = Embedding
    list_display = ['id', 'text']
    search_fields = ['text']

class LanguageAdmin(admin.ModelAdmin):
    model = Language
    list_display = ['id', 'name', 'description', 'embed_id']
    search_fields = ['name']

class LibraryAdmin(admin.ModelAdmin):
    model = Library
    list_display = ['id', 'name', 'description', 'lang_id', 'embed_id']
    search_fields = ['name']

admin.site.register(Embedding, EmbeddingAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(User, UserAdmin)
