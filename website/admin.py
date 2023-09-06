from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    # fieldset = {
    #     ('Name', {'field': 'name'}),
    #     ('Subject', {'field': 'subject'})
    # }
    list_display = ['name', 'email', 'subject']

admin.site.register(Contact, ContactAdmin)
