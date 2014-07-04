from django.contrib import admin
from shadowsocks.web.models import Account
from shadowsocks.web.models import Link
from shadowsocks.web.models import Flag

admin.site.register(Account)
admin.site.register(Link)
admin.site.register(Flag)
