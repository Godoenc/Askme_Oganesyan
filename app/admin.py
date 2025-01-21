from django.contrib import admin

from app import models

admin.site.register(models.Question)
admin.site.register(models.Answer)
admin.site.register(models.Tag)
admin.site.register(models.Likes_Of_Answers)
admin.site.register(models.Likes_Of_Question)
admin.site.register(models.Profile)

