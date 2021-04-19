from django.contrib import admin
from .models import Category, Trending, Style, New, Top, Recommend


admin.site.register(Category)
admin.site.register(Trending)
admin.site.register(Style)
admin.site.register(New)
admin.site.register(Top)
admin.site.register(Recommend)