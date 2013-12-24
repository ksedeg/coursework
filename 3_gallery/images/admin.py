from images.models import Image
from django.contrib import admin


# Register your models here.
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'desc', 'file')

admin.site.register(Image, ImageAdmin)
