from django.contrib import admin
from .models import Location, Booking, Comment, Horse, HorseCategory

admin.site.register(Location)
admin.site.register(Booking)
admin.site.register(Comment)
admin.site.register(Horse)
admin.site.register(HorseCategory)


