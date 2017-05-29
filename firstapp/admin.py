from django.contrib import admin
from firstapp.models import Person, Article, Comment

# Register your models here.
admin.site.register(Person)
admin.site.register(Article)
admin.site.register(Comment)
