from django.urls import path

from product import views

urlpatterns = [
    # List view (Read all)
    path('product/list/', views.ProductListView.as_view(), name='product-list'),

    # Create view
    path('product/create/', views.ProductCreateView.as_view(), name='product-create'),

    # Retrieve view (Read one)
    path('product/<int:pk>/', views.ProductRetrieveView.as_view(), name='product-retrieve'),

    # Update view
    path('product/<int:pk>/update/', views.ProductUpdateView.as_view(), name='product-update'),

    # Delete view
    path('product/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='product-destroy'),
]
