from django.contrib import admin
from .models import Product, Category, Manufacture, Campaign

from django.db import models
from django_json_widget.widgets import JSONEditorWidget


admin.site.register(Category)
admin.site.register(Manufacture)
admin.site.register(Campaign)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.JSONField: {'widget': JSONEditorWidget},
    }




