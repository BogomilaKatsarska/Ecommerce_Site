from django.contrib import admin

from shop.models import Product, Order

admin.site.site_header = "E-commerce Site"
admin.site.site_title = "ABC Shopping"
admin.site.index_title = "Manage ABC Shopping"


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'price', 'category']
    search_fields = ['title']
    actions = ('change_category_to_default',)
    # fields = ['title', 'price']
    list_editable = ['price', 'category']

    def change_category_to_default(self, request, queryset):
        queryset.update(category='default')

    change_category_to_default.short_description = 'Default Category'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass

