from django.contrib import admin

from content.models import Movie, Category

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'view_movies')

admin.site.register(Category)
