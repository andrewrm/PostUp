from django.contrib import admin
from account.models import FriendInvite, AdminAccount, PostAccount


admin.site.register(PostAccount)
admin.site.register(FriendInvite)
admin.site.register(AdminAccount)


