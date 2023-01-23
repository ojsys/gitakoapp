from django.contrib import admin
from .models import FarmBudget, FarmBlock, CropCalendar
# Register your models here.


admin.site.register(FarmBudget)
admin.site.register(FarmBlock)
admin.site.register(CropCalendar)