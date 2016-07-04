from django.contrib import admin
import os
# Register your models here.
from .form import SingnUpForm
from .models import SignUp
class SignUPAdmin(admin.ModelAdmin):
    list_display = ["__str__","timestramp","updated"]
    form = SingnUpForm


admin.site.register(SignUp,SignUPAdmin)