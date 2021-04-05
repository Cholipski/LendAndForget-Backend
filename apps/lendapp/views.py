from rest_framework import generics, serializers
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import ItemCategory, LoanStatus, Loan
from .serializers import ItemCategorySerializer, LoanStatusSerializer, LoanSerializer
from rest_framework.reverse import reverse
from rest_framework.response import Response
import json


class ItemCategoryList(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    name = 'itemcategory-list'


class ItemCategoryDetail(generics.RetrieveAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    name = 'itemcategory-detail'


class LoanStatusList(generics.ListCreateAPIView):
    queryset = LoanStatus.objects.all()
    serializer_class = LoanStatusSerializer
    name = 'loanstatus-list'


class LoanStatusDetail(generics.RetrieveAPIView):
    queryset = LoanStatus.objects.all()
    serializer_class = LoanStatusSerializer
    name = 'loanstatus-detail'


class LoanList(generics.ListCreateAPIView):
    serializer_class = LoanSerializer
    name = 'loan-list'
    permission_classes = [IsAuthenticated]
    lenderID = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(lenderID=self.request.user)

    def get_queryset(self):
        qs = Loan.objects.filter(lenderID=self.request.user) | Loan.objects.filter(borrowerID=self.request.user)
        return qs

class LoanDetail(generics.RetrieveAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    name = 'loan-detail'


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'ItemCategory': reverse(ItemCategoryList.name, request=request),
                         'LoanStatus': reverse(LoanStatusList.name, request=request),
                         'Loan': reverse(LoanList.name, request=request),
                         })


class ReturnLend(generics.GenericAPIView):
    def post(self, request):
        response = {
            'status': 403,
        }
        try:
            lend_id = json.loads(request.body)
            loan = Loan.objects.get(id=lend_id)
            loan.loanStatusID_id = 2
            loan.save()
            response['status'] = 200
            return JsonResponse(response)
        except:
            return JsonResponse(response)
