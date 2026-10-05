from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Producto
from .serializers import ProductoSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all().order_by('id')
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

#IsAuthenticatedOrReadOnly permite GET sin autenticación, 
# pero exige identidad válida para POST, PUT, PATCH y 
# DELETE. Esto separa autenticación de autorización y 
# aplica el control en el servidor.