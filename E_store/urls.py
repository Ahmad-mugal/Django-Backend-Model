from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.HOME , name = 'home'),
    path('base/', views.BASE , name= 'base'),
    path('products/', views.PRODUCT, name = 'products'),
    path('search/', views.SEARCH, name = 'search'),
    path("product/<str:id>", views.SINGLE_PRODUCT_PAGE, name='product_details'),
    path('contact/', views.CONTACT, name='contact'),
    path('registration/', views.HandleRegister, name = 'register'),
    path('login/', views.HandleLogin, name = 'login'),
    path('logout/', views.HandleLogOut, name = 'logout'),

    #cart

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',
         views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',
         views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart_detail/',views.cart_detail,name='cart_detail'),
    path('cart/check-out/', views.Check_out, name = "checkout"),
    path('cart/check-out/placeorder/', views.PLACE_ORDER, name = "place_order"),
    path('cart/check-out/placeorder/success', views.SUCCESS, name = 'success')


] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)


