from django.contrib import admin
from products.models import *


class ExtraImageInline(admin.TabularInline):
    model = GalleryProduct
    extra = 3

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'unit_price')

    prepopulated_fields = {
        'slug': ('name',)
    }
    inlines = [ExtraImageInline]
@admin.register(Category_one)
class Category_oneAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }


@admin.register(Category_two)
class Category_twoAdmin(admin.ModelAdmin):
    prepopulated_fields = {
        'slug': ('name',)
    }
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user','product','active','is_replay')

#'is_replay','replay_to'
# @admin.register(Oil)
# class OilAdmin(admin.ModelAdmin):
#     list_display = ('API',)
#
# @admin.register(Battery)
# class BatteryAdmin(admin.ModelAdmin):
#     list_display = ('Flow',)


admin.site.register(Brand)
# admin.site.register(Battery)
# admin.site.register(VolumeOil)
# admin.site.register(BrandBattery)
# admin.site.register(BrandOil)
# admin.site.register(Like)





