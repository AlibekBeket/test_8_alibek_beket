from django.contrib import admin

# Register your models here.

from django.contrib import admin

from feedback.models import Product, Review


# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "category", "description", "picture")
    list_filter = ("id", "name", "category", "description", "picture")
    search_fields = ("id", "name", "category", "description", "picture")
    fields = ("name", "category", "description", "picture")
    readonly_fields = ("id",)


admin.site.register(Product, ProductAdmin)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "product", "review_text", "grade")
    list_filter = ("id", "author", "product", "review_text", "grade")
    search_fields = ("id", "author", "product", "review_text", "grade")
    fields = ("author", "product", "review_text", "grade")
    readonly_fields = ("id",)


admin.site.register(Review, ReviewAdmin)