from django.contrib import admin

from .models import EmailSubscription


# Register your models here.
class EmailSubscriptionAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_subscribed', 'created_at', 'updated_at')
    list_filter = ('is_subscribed', 'created_at', 'updated_at')
    search_fields = ('email',)
    ordering = ('-created_at',)
    readonly_fields = ('created_at', 'updated_at')


admin.site.register(EmailSubscription, EmailSubscriptionAdmin)
