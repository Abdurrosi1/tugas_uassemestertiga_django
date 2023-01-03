from django.contrib import admin
from home.models import dataMahasiswa

# Register your models here.
class MahasiswaAdmin(admin.ModelAdmin):
    list_display = ['npm','nama','alamat','gander','tetala', 'kelas','dosen']
    search_fields = ['npm','nama','alamat','gander','tetala', 'kelas','dosen']
    list_display = ['npm','nama','alamat','gander','tetala', 'kelas','dosen']
    list_per_page =9
    
admin.site.register(dataMahasiswa, MahasiswaAdmin)