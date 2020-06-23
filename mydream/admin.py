from django.contrib import admin
from .models import Destinations1,Destinations2,Cards,About

# Register your models here.
admin.site.site_header = 'Miltek Notes Admin'
admin.site.site_title = 'Miltek Notes Admin'

class Destinations1Admin(admin.ModelAdmin):
    list_display= ('age','date_modified','username','is_draft')
    search_fields = ('age',)
    list_filter = ('age', 'is_draft' )
    actions = ('set_blocks_to_published',)
    def set_blocks_to_published(self,request,queryset):
        queryset.update(is_draft=False)

admin.site.register(Destinations1,Destinations1Admin)
admin.site.register(Destinations2)
admin.site.register(Cards)
admin.site.register(About)

