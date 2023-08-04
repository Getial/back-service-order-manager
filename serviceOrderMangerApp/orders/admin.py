from django.contrib import admin
from .models import Brand, Collaborator, Category, Reference, User, Order, Evidence

admin.site.register(Brand)
admin.site.register(Category)
admin.site.register(Reference)
admin.site.register(User)
admin.site.register(Collaborator)
admin.site.register(Order)
admin.site.register(Evidence)
