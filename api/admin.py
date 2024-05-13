from django.contrib import admin
from .models import activity


admin.site.register(activity)
class ActivityAdmin(admin.ModelAdmin):
    list_display = [ 'id', 'username', 'action', 'timestamp']
    search_fields = ['userName']


