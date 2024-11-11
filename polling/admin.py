from django.contrib import admin

from polling.models import Poll
admin.site.register(Poll)
# creates an interface that will allow us to interact with the poll table