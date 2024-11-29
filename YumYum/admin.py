from django.contrib import admin
from .models import book,Dessert,Gelato,Mocktail,Shake,Starter,Indian, Chinese, American, Review, Cart

admin.site.register(book)
admin.site.register(Dessert)
admin.site.register(Gelato)
admin.site.register(Mocktail)
admin.site.register(Shake)
admin.site.register(Starter)
admin.site.register(Indian)
admin.site.register(Chinese)
admin.site.register(American)
admin.site.register(Cart)

class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message', 'created_at')
    search_fields = ('name', 'email', 'message')
    list_filter = ('created_at',)

admin.site.register(Review, ReviewAdmin)
