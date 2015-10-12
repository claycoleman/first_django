from django.contrib import admin
from main.models import State, StateCapital, Area
# Register your models here.


class StateAdmin(admin.ModelAdmin):
    list_display = ('name', 'abbrev', 'statecapital')
    # model = StateCapital.state.through  


class CapitalAdmin(admin.ModelAdmin):
    list_display = ('name', 'population', 'state')


class AreaAdmin(admin.ModelAdmin):
    list_display = ('city', 'zip_code', 'state')
    search_fields = ['city']

admin.site.register(State, StateAdmin)
admin.site.register(StateCapital, CapitalAdmin)
admin.site.register(Area, AreaAdmin)