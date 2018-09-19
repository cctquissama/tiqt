from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Ticket, Comentario, Departamento, Secretaria, Setor

# Register your models here.


class SetorInline(admin.TabularInline):
    model = Setor
    extra = 3


class SecretariaAdmin(admin.ModelAdmin):
    inlines = [SetorInline]


class ComentarioInline(admin.TabularInline):
    model = Comentario
    extra = 1


class TicketAdmin(admin.ModelAdmin):
    inlines = [ComentarioInline]


admin.site.register(User, UserAdmin)
admin.site.register(Ticket, TicketAdmin)
admin.site.register(Departamento)
admin.site.register(Secretaria, SecretariaAdmin)
