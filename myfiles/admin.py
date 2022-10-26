from django.contrib import admin
from myfiles.models import Service, Murojat


# Register your models here.

class AdminServer(admin.ModelAdmin):
    list_display = ['id', 'nomi', 'old_price', 'new_price', 'manzili', 'rooms', 'rasm', 'vaqt']

admin.site.register(Service,AdminServer)



class AdminM(admin.ModelAdmin):
    list_display = ['id', 'ism', 'mail', 'vaqt', 'subject', 'massage']

admin.site.register(Murojat, AdminM)
