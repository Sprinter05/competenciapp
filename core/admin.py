from django.contrib import admin
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


class UserLibAdmin(admin.ModelAdmin):
    model = UserLib
    list_display = ['u_id', 'lib_id']
    search_fields = ['u_id']

class UserLangAdmin(admin.ModelAdmin):
    model = UserLang
    list_display = ['u_id', 'lang_id']
    search_fields = ['u_id']

admin.site.register(Embedding, EmbeddingAdmin)
admin.site.register(Language, LanguageAdmin)
admin.site.register(Library, LibraryAdmin)
admin.site.register(UserLib, UserLibAdmin)
admin.site.register(UserLang, UserLangAdmin)
