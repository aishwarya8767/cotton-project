from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),   #home page
    path('about/', views.about, name='about'),  #abot page
    path('enquire/', views.enquire, name='enquire'),  # Enquire page

    # Main product page
    path('products/', views.products, name='products'),

    # Individual product category pages
    path('products/surgical/', views.Absorbent_Cotton, name='Absorbent_Cotton'),
    path('products/medical/', views.Absorbent_Gauze_Bandage, name='Absorbent_Gauze_Bandage'),
    path('products/syringe/', views.Syringe_and_Needles, name='Syringe_and_Needles'),
    path('products/gloves/', views.Hand_Gloves, name='Hand_Gloves'),
    path('products/tubes/', views.Blood_Collection_Tubes, name='Blood_Collection_Tubes'),
    path('products/cotton/', views.zig_zag_cotton, name='zig_zag_cotton'),
    path('products/cloth/', views.Gauze_Cloth_Than, name='Gauze_Cloth_Than'),
    path('products/other/', views.Other_Products, name='Other_Products'),

    # Product detail (optional)
    path('product/<int:id>/', views.products, name='product_detail'),

    path('contact/', views.contact, name='contact'),
]

