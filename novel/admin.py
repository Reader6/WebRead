from django.contrib import admin

# Register your models here.

from .models import Novels
from .models import Chart
from .models import IMG
admin.site.register(Novels)
admin.site.register(Chart)
admin.site.register(IMG)
