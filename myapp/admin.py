from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, Address, UserProfile, Contact , Wishlist


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=True, refund_granted=True)
make_refund_accepted.short_description = 'Update orders to refund granted'



def order_delivered_to_customer(modeladmin, request, queryset):
    queryset.update(being_delivered=False, received=True)
order_delivered_to_customer.short_description = 'Update orders to received'



class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user' ,
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted , order_delivered_to_customer]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


admin.site.register(Item)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(Address, AddressAdmin)
admin.site.register(UserProfile)
admin.site.register(Contact)
admin.site.register(Wishlist)