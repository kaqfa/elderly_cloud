from django.contrib import admin
from .models import Article, Category

# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_category', 'author', 'modified', 'status']
    fields = ['title', 'category', 'content', 'photo', 'status']
    
    def save_model(self, request, obj, form, change):
        if getattr(obj, 'author', None) is None:
            obj.author = request.user
        obj.save()
        
    def get_category(self, obj):
        return ", ".join([c.name for c in obj.category.all()])
    get_category.allow_tags = True
    get_category.short_description = ("Kategori")

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
    fields = ['name', 'description']


admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)