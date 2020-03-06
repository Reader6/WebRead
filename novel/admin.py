from django.contrib import admin

# Register your models here.

from .models import Novels
from .models import Chart
admin.site.register(Novels)
admin.site.register(Chart)
