from django.contrib import admin
from .models import Class,Sem,UserDetails,Subjects,Reval

# Register your models here.
class Class_admin(admin.ModelAdmin):
    list_display = ['class_id', 'class_name']

admin.site.register(Class,Class_admin)
admin.site.register(Sem)
admin.site.register(UserDetails)
admin.site.register(Subjects)
admin.site.register(Reval)

