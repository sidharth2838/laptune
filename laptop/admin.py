from django.contrib import admin
from .models import Laptop, Customization, Review, Purchase

class LaptopAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'base_price')
    search_fields = ('brand', 'model')
    list_filter = ('brand',)
    ordering = ('brand', 'model')

# class CustomizationAdmin(admin.ModelAdmin):

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'comment', 'rating')  # Fields to display in the list view
    ordering = ('rating',)  # Order by rating in ascending order
    list_filter = ('rating',)  # Filter by rating

    # def get_list_filter(self, request):
    #     """
    #     Customize the filter list to include rating filter with choices 0 to 5.
    #     """
    #     filters = super().get_list_filter(request)
    #     return filters + ('rating',)



class PurchaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'payment_method')
    search_fields = ('name', 'email', 'payment_method')
    list_filter = ('payment_method',)
    ordering = ('name',)

# Register your models with the admin site
admin.site.register(Laptop, LaptopAdmin)
# admin.site.register(Customization, CustomizationAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Purchase, PurchaseAdmin)
