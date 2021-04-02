from rest_framework import generics
from .models import ItemCategory
from .serializers import ItemCategorySerializer
from rest_framework.reverse import reverse
from rest_framework.response import Response


class ItemCategoryList(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    name = 'ItemCategory-list'

class ItemCategoryDetail(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    name = 'ItemCategory-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({'ItemCategory': reverse(ItemCategoryList.name, request=request),
                         })
