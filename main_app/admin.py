from django.contrib import admin

# Register your models here.
from .models import FamilyMember, LifeEvent, Comment

# Register the FamilyMember model
admin.site.register(FamilyMember)
admin.site.register(LifeEvent)
admin.site.register(Comment)
