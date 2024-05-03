from django.urls import path , include
from .views import HomeView, product, add_to_cart, addremovewishlist, showwishlist, remove_from_cart, ProductsView, Trackorder, OrderSummaryView, ContactView, remove_single_item_from_cart, CheckoutView, PaymentView, RequestRefundView, AddCouponView, about_us, search_feature, filter_shirts, filter_pants, filter_shoes
app_name = 'myapp'
urlpatterns = [
    path('', HomeView.as_view() , name = "home"),
    path('order-summary/', OrderSummaryView.as_view(), name='order-summary'),
    path("checkout", CheckoutView.as_view() , name = "checkout"),
    path("allproducts/", ProductsView.as_view() , name = "allproducts"),
    path("product/<slug>/", product.as_view() , name = "product"),
    path("add-to-cart/<slug>/", add_to_cart , name = "add-to-cart"),
    path("remove-from-cart/<slug>/", remove_from_cart , name = "remove-from-cart"),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove-single-item-from-cart'),
    path('payment/<payment_option>/', PaymentView.as_view(), name='payment'),
    path('add-coupon/', AddCouponView.as_view(), name='add-coupon'),
    path('Track-order/', Trackorder, name='Track-order'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path("contactus/", ContactView.as_view() , name = "contactus"),
    path("aboutus/", about_us.as_view() , name = "aboutus"),
    path('search/', search_feature, name='search'),
    path('filter//<type>/', filter_shirts, name='filter-shirts'),
    path('filter/<type>/', filter_pants, name='filter-pants'),
    path('filter/<type>/', filter_shoes, name='filter-shoes'),
    path('add_remove_wishlist/<slug>/', addremovewishlist, name='add_remove_wishlist'),
    path('show_wishlist', showwishlist, name='show_wishlist'),
    ]