from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('',views.index,name="index"),
    path('category/<slug:val>',views.CategoryView.as_view(),name='category'),
    path('productdetails/<int:pk>',views.ProductDetails.as_view(),name='productdetails'),
    path('contact',views.contact,name="contact"),
    path('about',views.about,name="about"),
    path('profile',views.ProfileView.as_view(),name="profile"),
    path('address',views.address,name="address"),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('cart/',views.show_cart,name="showcart"),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart,name="removecart"),
    path('payment', views.payment, name='payment'),
    path('success', views.success, name='success'),
    path("user", views.user, name="user"),
    path("signin", views.signin, name="signin"),
    path("signout",views.signout,name = "signout"),
]
urlpatterns+=static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)