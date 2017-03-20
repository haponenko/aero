from django.contrib import admin

from booking.models import Country, State, City


class BookingAdmin(admin.ModelAdmin):
    list_filter = ['date_out']


admin.site.register(Country)
admin.site.register(State)
admin.site.register(City)