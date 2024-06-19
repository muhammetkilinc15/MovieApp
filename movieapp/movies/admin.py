from django.contrib import admin

from movies.models import Movie,Person,Video,Genre,Contact

class MovieAdmin(admin.ModelAdmin):
    list_display = ("title","isActive","is_hone",)
    prepopulated_fields= {"slug":("title",)}
    last_filter = ("genres","language",)
    search_fields = ("title","genres",)

class PersonAdmin(admin.ModelAdmin):
    list_display = ("full_name","gender","duty_type",)
    list_filter = ("gender","duty_type",)
    search_fields = ("first_name","last_name",)

admin.site.register(Person,PersonAdmin)
admin.site.register(Movie,MovieAdmin)
admin.site.register(Genre)
admin.site.register(Contact)
admin.site.register(Video)