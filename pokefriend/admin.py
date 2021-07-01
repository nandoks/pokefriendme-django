from django.contrib import admin

# Register your models here.
from pokefriend.models import Trainer

admin.site.register(
    Trainer,
)
