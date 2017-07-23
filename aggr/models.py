from django.db import models
from django.contrib import admin


class Post(models.Model):
    url = models.TextField()
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.description[:20]

class PostAdmin(admin.ModelAdmin):
    list_display = ('description', 'url', 'created')
    list_filter = ['created', 'description']
    search_fields = ['description', 'url']
    date_hierarchy = 'created'


