from django.contrib import admin
from lawdiff.models import Bill_File, Bill



class Bill_File_Admin(admin.ModelAdmin):
	pass

class Bill_Admin(admin.ModelAdmin):
        pass

admin.site.register(Bill_File, Bill_File_Admin)
admin.site.register(Bill, Bill_Admin)

