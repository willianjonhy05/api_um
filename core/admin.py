from django.contrib import admin
from .models import *

@admin.register(Livro)
class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor')
    list_filter = ('titulo', 'autor')
    search_fields = ('titulo', 'autor')


admin.site.register(Autor)
