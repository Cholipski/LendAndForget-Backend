from rest_framework import generics, serializers, response, status
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from .models import ItemCategory, LoanStatus, Loan, MoneyLoan
from .serializers import ItemCategorySerializer, LoanStatusSerializer, LoanSerializer, MoneyLoanSerializer
from rest_framework.reverse import reverse
from rest_framework.response import Response
import json


# ----------------------------------------------------------------------------------------------------------------------
# Categories

class ItemCategoryList(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    name = 'item-category-list'


class ItemCategoryDetail(generics.RetrieveAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    name = 'item-category-detail'

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Statuses

class LoanStatusList(generics.ListCreateAPIView):
    queryset = LoanStatus.objects.all()
    serializer_class = LoanStatusSerializer
    name = 'loan-status-list'


class LoanStatusDetail(generics.RetrieveAPIView):
    queryset = LoanStatus.objects.all()
    serializer_class = LoanStatusSerializer
    name = 'loan-status-detail'

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Item Loan

class LoanList(generics.ListCreateAPIView):
    serializer_class = LoanSerializer
    name = 'loan-list'
    permission_classes = [IsAuthenticated]
    lenderID = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(lenderID=self.request.user, loanStatusID_id="1")

    def get_queryset(self):
        qs = Loan.objects.filter(lenderID=self.request.user) | Loan.objects.filter(borrowerID=self.request.user)
        return qs


class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    name = 'loan-detail'

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Money Loan

class MoneyLoanList(generics.ListCreateAPIView):
    serializer_class = MoneyLoanSerializer
    name = 'money-loan-list'
    permission_classes = [IsAuthenticated]
    lenderID = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    def perform_create(self, serializer):
        serializer.save(lenderID=self.request.user, loanStatusID_id="1")

    def get_queryset(self):
        qs = MoneyLoan.objects.filter(lenderID=self.request.user) | MoneyLoan.objects.filter(borrowerID=self.request.
                                                                                             user)
        return qs


class MoneyLoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyLoan.objects.all()
    serializer_class = MoneyLoanSerializer
    name = 'money-loan-detail'

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# ApiRoot view

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'ItemCategory': reverse(ItemCategoryList.name, request=request),
                         'LoanStatus': reverse(LoanStatusList.name, request=request),
                         'Loan': reverse(LoanList.name, request=request),
                         })


# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Return item

class ReturnLend(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            lend_id = json.loads(request.body)
            loan = Loan.objects.get(id=lend_id)
            loan.loanStatusID_id = 2
            loan.save()
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)

# ----------------------------------------------------------------------------------------------------------------------


# ----------------------------------------------------------------------------------------------------------------------
# Return money

class ReturnMoneyLend(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            lend_id = json.loads(request.body)
            loan = MoneyLoan.objects.get(id=lend_id)
            loan.loanStatusID_id = 2
            loan.save()
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)

# ----------------------------------------------------------------------------------------------------------------------
