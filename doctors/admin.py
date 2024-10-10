from django.contrib import admin

from doctors.models.doctor import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty', 'is_international', 'advertise', 'advertise_duration')
    search_fields = ('user__full_name', 'specialty')