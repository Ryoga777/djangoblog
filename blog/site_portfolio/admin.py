from django.contrib import admin

# Register your models here.

from .models import Site_Portfolio

class Site_Portfolio_Admin(admin.ModelAdmin):

    list_display = ["nome"]
    list_filter = ["nome"]
    search_fields = ["nome"]
    prepopulated_fields = {"slug": ("nome",)}

    class Meta:
        model = Site_Portfolio

admin.site.register(Site_Portfolio, Site_Portfolio_Admin) 
