from django.contrib import admin
from loginsys.models import *
from datetime import datetime


class UserSet(admin.ModelAdmin):
    fields = (('first_name', 'last_name'), 'email', 'birth_date', 'age')
    list_filter = ('birth_date',)
    list_display = ('last_name', 'first_name', 'email', 'birth_date', 'age', 'agecalculate')
    search_fields = ('first_name', 'last_name')
    list_per_page = 10

    def agecalculate(self, obj):
        d1 = obj.birth_date
        d2 = datetime.date(datetime.now())
        delta = d2 - d1
        return delta

# Register your models here.
admin.site.register(User, UserSet)