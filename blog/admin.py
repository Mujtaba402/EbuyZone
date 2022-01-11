from django.contrib import admin

from .models import Profile, Blogpost


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'dob', 'photo')
    list_filter = ('dob',)
    search_fields = ('author__username', 'dob')
    list_editable = ('photo',)
    date_hierarchy = ('dob')

class BlogpostAdmin(admin.ModelAdmin):
    list_display = ('title', 'head0', 'head1','head2','thumbnail','pub_date')
    # list_filter = ('pub_date',)
    search_fields = ('title', 'pub_date')
    list_editable = ('thumbnail',)
    date_hierarchy = ('pub_date')

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Blogpost, BlogpostAdmin)