from django.contrib import admin
from .models import Paper
from .models import Member

# Register your models here.
admin.site.register(Paper)
admin.site.register(Member)