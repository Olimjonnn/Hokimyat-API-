from django.contrib import admin
from main.models import *
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext, gettext_lazy as _

@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'type', 'is_active']
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        (_('Personal info'), {'fields': ('first_name','last_name', 'email' )}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        (_('Extra'), {'fields': ('type', 'phone')}),
        (_('Important dates'), {'fields': ('last_login', 'date_joined')})
    )
admin.site.register(Slider)
admin.site.register(Logo)
admin.site.register(Category)
admin.site.register(News)
admin.site.register(Malumotlar)
admin.site.register(Video)
admin.site.register(VideoNews)
admin.site.register(Xabarlar)
admin.site.register(Reklama)
admin.site.register(FoydaliSaytlar)
admin.site.register(AndOrganing)
admin.site.register(Malumotlar2)
admin.site.register(TavsiyaVideo)
admin.site.register(Kerak)
admin.site.register(Loyiha1)
admin.site.register(Xizmatlar)
admin.site.register(Andijon)
admin.site.register(Loyiha2)
admin.site.register(InvsTarmoqlar)
admin.site.register(Hujjat)
admin.site.register(QoshimchaXizmat)
admin.site.register(Savol)
admin.site.register(Javob)
admin.site.register(Loyiha3)
admin.site.register(Info)
