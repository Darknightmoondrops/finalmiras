from django.urls import path
from . import api_views

app_name = 'ApiDerakhti'

urlpatterns = [
    path('contracts-add/',api_views.contracts_add.as_view(),name='contracts_add'),
    path('cards-add/',api_views.cards_add.as_view(),name='cards_add'),
    path('profile-update/',api_views.profile_update.as_view(),name='profile_update'),
    path('place-user-buy/',api_views.place_user_buy.as_view(),name='place_user_buy'),
    path('place-user-reservation/',api_views.place_user_reservation.as_view(),name='place_user_reservation'),
    path('check-identifier-code/',api_views.check_identifierـcode.as_view(),name='check_identifierـcode'),
    path('check-accses/',api_views.check_accses.as_view(),name='check_accses'),
    path('select-points/',api_views.select_points.as_view(),name='select_points'),
    path('sub-categories-number/',api_views.sub_categories_number.as_view(),name='sub_categories_number'),
    path('place-active-right-number/',api_views.place_active_right_number.as_view(),name='place_active_right_number'),
    path('place-active-left-number/',api_views.place_active_left_number.as_view(),name='place_active_left_number'),
    path('place-reservation-right-number/',api_views.place_reservation_right_number.as_view(),name='place_reservation_right_number'),
    path('place-reservation-left-number/',api_views.place_reservation_left_number.as_view(),name='place_reservation_left_number'),
    path('orders-list/',api_views.orders_list.as_view(),name='orders_list'),
    path('places-list/',api_views.places_list.as_view(),name='places_list'),
    path('places-list-filter/',api_views.places_list_filter.as_view(),name='places_list_filter'),
    path('user-info/',api_views.user_info.as_view(),name='user_info'),
    path('deposit-request/',api_views.deposit_request.as_view(),name='deposit_request'),
    path('product-canel/',api_views.product_canel.as_view(),name='product_canel'),


    path('carts/carts-add/', api_views.carts_add.as_view(), name='carts_add'),
    path('carts/carts-remove/', api_views.carts_remove.as_view(), name='carts_add'),
    path('carts/carts-list/', api_views.carts_list.as_view(), name='carts_list'),

    # Api Products
    path('products/products-list/', api_views.products_list.as_view(), name='products_list'),
    path('products/products-list-vocher/', api_views.products_list_vocher.as_view(), name='products_list'),
    path('products/products-comments-add/', api_views.products_comments_add.as_view(), name='products_comments_add'),
    path('products/products-comments-list/', api_views.products_comments_list.as_view(), name='products_comments_list'),
    path('products/products-filter-maincategory-list/', api_views.products_filter_maincategory_list.as_view(),name='products_filter_maincategory_list'),

    path('admin-panel/products/products-list/', api_views.admin_products_list.as_view(),name='admin_products_list'),
    path('admin-panel/products/products-main_categories/', api_views.admin_main_categories.as_view(),name='admin_main_categories'),
    path('admin-panel/products/products-sub_categories1/', api_views.admin_sub_categories1.as_view(),name='admin_sub_categories1'),
    path('admin-panel/products/products-sub_categories2/', api_views.admin_sub_categories2.as_view(),name='admin_sub_categories2'),
    path('admin-panel/products/products-purchased/', api_views.admin_products_purchased.as_view(),name='admin_products_purchased'),
    path('admin-panel/products/products-comments-list/', api_views.admin_products_comments_list.as_view(),name='admin_products_comments_list'),
    path('admin-panel/products/products-add/', api_views.admin_products_add.as_view(), name='admin_products_add'),
    path('admin-panel/products/products-update/', api_views.admin_products_update.as_view(),name='admin_products_update'),
    path('admin-panel/products/products-delete/', api_views.admin_products_delete.as_view(),name='admin_products_delete'),
]