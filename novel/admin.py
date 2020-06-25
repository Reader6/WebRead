from django.contrib import admin

# Register your models here.

from .models import Novels
from .models import Chart,Types
from login.models import User
# from .models import IMG

#
# class UserAdmin(admin.ModelAdmin):
#     list_display = ['name','email','ct_time']
#     list_filter = ['name']
#     search_fields = ['name']
#     list_per_page = 10

admin.site.register(Novels)
admin.site.register(Chart)
admin.site.register(Types)
# admin.site.register(IMG)
