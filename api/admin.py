from django.contrib import admin
from api.models import Student, StudentDetail, Color, RandomUser
# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'last_name', 'mobile_number')
    list_display = ('name', 'last_name')
    list_filter = ('last_name',)


admin.site.register(Student, StudentAdmin)
admin.site.register(StudentDetail)
admin.site.register(Color)
admin.site.register(RandomUser)
