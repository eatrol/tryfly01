from django.contrib import admin
from fly.models import *

# Register your models here.
class dbflyAdmin(admin.ModelAdmin):
 	list_display=('id','name','description','check','memo','phase','lesson')


admin.site.register(dbfly,dbflyAdmin)
