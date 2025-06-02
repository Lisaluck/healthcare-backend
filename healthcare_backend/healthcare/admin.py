from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Patient, Doctor, PatientDoctorMapping

# Custom User Admin
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'username', 'is_patient', 'is_doctor', 'is_staff')
    list_filter = ('is_patient', 'is_doctor', 'is_staff', 'is_superuser')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('username', 'first_name', 'last_name')}),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'is_patient', 'is_doctor', 'groups', 'user_permissions'),
        }),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'username', 'password1', 'password2', 'is_patient', 'is_doctor'),
        }),
    )
    search_fields = ('email', 'username')
    ordering = ('email',)
    filter_horizontal = ('groups', 'user_permissions',)

# Patient Admin
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'date_of_birth', 'gender', 'phone_number', 'created_by')
    list_filter = ('gender', 'created_at', 'updated_at')
    search_fields = ('name', 'user__email', 'phone_number')
    raw_id_fields = ('user', 'created_by')
    date_hierarchy = 'created_at'

# Doctor Admin
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'specialization', 'hospital', 'contact_number', 'created_by')
    list_filter = ('specialization', 'hospital', 'created_at')
    search_fields = ('name', 'user__email', 'specialization', 'contact_number')
    raw_id_fields = ('user', 'created_by')

# Patient-Doctor Mapping Admin
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ('patient', 'doctor', 'created_at')
    list_filter = ('created_at',)
    search_fields = ('patient__name', 'doctor__name')
    raw_id_fields = ('patient', 'doctor')
    date_hierarchy = 'created_at'

# Register models
admin.site.register(User, CustomUserAdmin)
admin.site.register(Patient, PatientAdmin)
admin.site.register(Doctor, DoctorAdmin)
admin.site.register(PatientDoctorMapping, PatientDoctorMappingAdmin)