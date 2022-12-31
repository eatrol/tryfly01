from django.contrib import admin
from fly.models import *

# Register your models here.
class dbflyAdmin(admin.ModelAdmin):
 	list_display=('id','name','description','check','memo','phase','lesson')


class dblucyAdmin(admin.ModelAdmin):
 	list_display=('name','image','sound','bgcolor','textsize','type','status','data')
	
class dbtoeicAdmin(admin.ModelAdmin):
 	list_display=('item','name','chinese','relate','memo','level','toune','sound','wrong','standard')

admin.site.register(dblucy,dblucyAdmin)
admin.site.register(dbtoeic,dbtoeicAdmin)

admin.site.register(dbfly,dbflyAdmin)

