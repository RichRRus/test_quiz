from django.contrib import admin

from . import models


class QuizAdmin(admin.ModelAdmin):
    readonly_fields = ('start_time',)


admin.site.register(models.Quiz, QuizAdmin)
admin.site.register(models.Question)
admin.site.register(models.PassedQuiz)
