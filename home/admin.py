from django.contrib import admin

# Register your models here.
from .models import BlogModel , Profile, Testimonial


admin.site.register(BlogModel)
admin.site.register(Profile)
admin.site.register(Testimonial)