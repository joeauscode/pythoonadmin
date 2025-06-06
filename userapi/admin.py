from django.contrib import admin
from .models import Account, DepositHistory, WithdrawalHistory, Investment, InvestmentHistory
from django.utils.html import format_html

# Customizing the display of the Account model in the admin panel
@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = (
        'user', 'balance', 'bitcoin_balance', 'ethereum_balance', 
        'tron_balance', 'doge_balance', 'bitcoin_cash_balance', 'usdt_trc20_balance',
        'bnb_balance', 'litecoin_balance', 'usdt_erc20_balance', 'binance_usd_balance',
        'avatar_preview', 'date_created', 'last_updated', 'gold_balance', 'steel_balance', 
        'iron_ore_balance', 'lithium_balance',        
    )
    search_fields = ('user__username',)
    list_filter = ('date_created',)
    ordering = ('-date_created',)
    fields = (
        'user', 'balance', 'bitcoin_balance', 'ethereum_balance', 
        'tron_balance', 'doge_balance', 'bitcoin_cash_balance', 'usdt_trc20_balance',
        'bnb_balance', 'litecoin_balance', 'usdt_erc20_balance', 'binance_usd_balance', 'avatar'
    )


    def avatar_preview(self, obj):
        if obj.avatar:
            return format_html('<img src="{}" width="50" height="50" style="object-fit: cover; border-radius: 50%;" />', obj.avatar.url)
        return "-"
    avatar_preview.short_description = 'Avatar Preview'



@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'earnings', 'total_profit', 'activation_date', 'end_date', 'status')
    list_filter = ('status', 'payment_method')
    search_fields = ('user__username', 'payment_method')
    readonly_fields = ()  # Optional


@admin.register(DepositHistory)
class DepositHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'crypto', 'amount', 'timestamp', 'description')
    list_filter = ('crypto', 'timestamp')
    search_fields = ('account__fullname', 'crypto', 'description')
    readonly_fields = ('timestamp',)
    fieldsets = (
        (None, {
            'fields': ('account', 'crypto', 'amount', 'description', 'timestamp'),
        }),
    )


@admin.register(WithdrawalHistory)
class WithdrawalHistoryAdmin(admin.ModelAdmin):
    list_display = ('account', 'crypto', 'amount', 'timestamp', 'description')
    list_filter = ('crypto', 'timestamp')
    search_fields = ('account__fullname', 'crypto', 'description')
    readonly_fields = ('timestamp',)
    fieldsets = (
        (None, {
            'fields': ('account', 'crypto', 'amount', 'description', 'timestamp'),
        }),
    )








@admin.register(InvestmentHistory)
class InvestmentHistoryAdmin(admin.ModelAdmin):
    list_display = ('user', 'payment_method', 'amount', 'status', 'date')
    list_filter = ('status', 'payment_method', 'date')
    search_fields = ('user__username', 'payment_method')
    readonly_fields = ('date',)