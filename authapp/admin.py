from django.contrib import admin
from authapp.models import Contact,Enrollment,Trainer,MembershipPlan,Gallery,Attendance
# Register your models here.
admin.site.register(Contact)
admin.site.register(Enrollment)
admin.site.register(Trainer)
admin.site.register(MembershipPlan)
admin.site.register(Gallery)
admin.site.register(Attendance)