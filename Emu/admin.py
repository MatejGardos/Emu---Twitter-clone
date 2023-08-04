from django.contrib import admin
from django.contrib.auth.models import Group, User
from .models import Profile, Tweet

# Unregister Groups
admin.site.unregister(Group)

# Mix profile info into user info
class ProfileInLine(admin.StackedInline):
    model = Profile

# Extedn User model
class UserAdmin(admin.ModelAdmin):
    model = User
    # Display only username fields on admin page
    fields = ["username"]
    inlines = [ProfileInLine]

# Unregister initial User
admin.site.unregister(User)

# Reregister User and Profile
admin.site.register(User, UserAdmin)

# Register tweets
admin.site.register(Tweet)
