from django.contrib import admin
from .models import (CityParams,
                     City,
                     Task,
                     Person,
                     Event,
                     Token,
                     ExternalUser,
                     ExternalQuery)


admin.site.register(City)
admin.site.register(CityParams)
admin.site.register(Task)
admin.site.register(Person)
admin.site.register(Event)
admin.site.register(Token)
admin.site.register(ExternalUser)
admin.site.register(ExternalQuery)
