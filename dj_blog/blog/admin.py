from django.contrib import admin

from blog.models import Post, Comments, Rating


class PostAdminForm(admin.ModelAdmin):
    filter_horizontal = ('comments',)
    prepopulated_fields = {'slug': ('title', )}


admin.site.register(Post, PostAdminForm)
admin.site.register(Comments)
admin.site.register(Rating)
