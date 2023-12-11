from rest_framework import permissions
from rest_framework.generics import CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView, RetrieveAPIView

from product.models import Product
from product.serializer import ProductSerializer


class ProductCreateView(CreateAPIView):
    serializer_class = ProductSerializer
    permission_classes = permissions.IsAuthenticated


class ProductListView(ListAPIView):
    serializer_class = ProductSerializer
    permission_classes = permissions.IsAuthenticated
    queryset = Product.objects.all()


class ProductRetrieveView(RetrieveAPIView):
    serializer_class = ProductSerializer
    permission_classes = permissions.IsAuthenticated
    queryset = Product.objects.all()


class ProductUpdateView(UpdateAPIView):
    serializer_class = ProductSerializer
    permission_classes = permissions.IsAuthenticated
    queryset = Product.objects.all()


class ProductDeleteView(DestroyAPIView):
    serializer_class = ProductSerializer
    permission_classes = permissions.IsAuthenticated
    queryset = Product.objects.all()
