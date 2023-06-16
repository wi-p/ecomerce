from django.contrib import admin
from .models import Book, User, UserCart, UserComment

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(UserCart)
admin.site.register(UserComment)

