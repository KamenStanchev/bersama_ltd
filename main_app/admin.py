from django.contrib import admin
from .models import Product, Category, Manufacturer

from django.db import models
from django_json_widget.widgets import JSONEditorWidget


admin.site.register(Category)
admin.site.register(Manufacturer)


@admin.register(Product)
class YourModelAdmin(admin.ModelAdmin):
    formfield_overrides = {
        # fields.JSONField: {'widget': JSONEditorWidget}, # if django < 3.1
        models.JSONField: {'widget': JSONEditorWidget},
    }




