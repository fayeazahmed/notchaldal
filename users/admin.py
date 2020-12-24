from .models import User
from django.contrib import admin


class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email',
                    'is_superuser',)
    list_display_links = ('id', 'name', 'email',
                          'is_superuser',)
    search_fields = ('id', 'name', 'email',
                     'is_superuser',)


admin.site.register(User, UserAdmin)
