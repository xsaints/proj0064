from django.contrib import admin

from .models import Category, Course


class CategoryAdmin(admin.ModelAdmin):
  list_display= ['name', 'slug']
  prepopulated_fields= {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)



class CourseAdmin(admin.ModelAdmin):
  list_display= ['title', 'slug', 'author', 'description', 'price']
  prepopulated_fields= {'slug': ('title',)}
admin.site.register(Course, CourseAdmin)
