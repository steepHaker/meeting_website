from django.contrib import admin
from .models import *

# # Затем, чтобы получить доступ к модели UserInfo, импортируем ее после определения модели User
# from .models import UserInfo
 
admin.site.register(UserInfo)
admin.site.register(Smoking)
admin.site.register(Children)
admin.site.register(Gender)
admin.site.register(Country)

admin.site.register(Horoscope)
admin.site.register(Ethnicity)
admin.site.register(City)
admin.site.register(User)
admin.site.register(Alcohol)

