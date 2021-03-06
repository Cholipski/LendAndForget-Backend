import datetime
import json

from django.core.exceptions import ObjectDoesNotExist

from .models import ItemCategory, LoanStatus, Loan, MoneyLoan, Notification, Contact
from .serializers import ItemCategorySerializer, LoanStatusSerializer, LoanSerializer, MoneyLoanSerializer, \
    NotificationSerializer, ContactSerializer

from django.contrib.auth.models import User
from django.http import JsonResponse
from rest_framework import generics, serializers, response, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.reverse import reverse
from rest_framework.response import Response

# <editor-fold desc="Categories">


class ItemCategoryList(generics.ListCreateAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    name = 'itemcategory-list'


class ItemCategoryDetail(generics.RetrieveAPIView):
    queryset = ItemCategory.objects.all()
    serializer_class = ItemCategorySerializer
    name = 'itemcategory-detail'
# </editor-fold>
# <editor-fold desc="Statuses">


class LoanStatusList(generics.ListCreateAPIView):
    queryset = LoanStatus.objects.all()
    serializer_class = LoanStatusSerializer
    name = 'loan-status-list'


class LoanStatusDetail(generics.RetrieveAPIView):
    queryset = LoanStatus.objects.all()
    serializer_class = LoanStatusSerializer
    name = 'loan-status-detail'
# </editor-fold>
# <editor-fold desc="Item loan">


class LoanList(generics.ListCreateAPIView):
    serializer_class = LoanSerializer
    name = 'loan-list'
    permission_classes = [IsAuthenticated]
    lender_id = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    def create(self, request, *args, **kwargs):
        data = self.request.data
        try:
            borrower = User.objects.get(email=data['borrower_id'])
            if self.request.user != borrower:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'borrower_id': 'You can not lend item for yourself'},
                                status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'borrower_id': 'Object with email=' + data['borrower_id'] + ' does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(lender_id=self.request.user, loan_status_id_id="1")

    def get_queryset(self):
        qs = Loan.objects.filter(lender_id=self.request.user) | Loan.objects.filter(borrower_id=self.request.user)
        return qs


class LoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
    name = 'loan-detail'

    def destroy(self, *args, **kwargs):
        self.get_object().create_notification_on_delete()
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return Response(serializer.data, status=status.HTTP_200_OK)


# </editor-fold>
# <editor-fold desc="Money loan">


class MoneyLoanList(generics.ListCreateAPIView):
    serializer_class = MoneyLoanSerializer
    name = 'moneyloan-list'
    permission_classes = [IsAuthenticated]
    lender_id = serializers.PrimaryKeyRelatedField(
        read_only=True,
    )

    def create(self, request, *args, **kwargs):
        data = self.request.data
        try:
            borrower = User.objects.get(email=data['borrower_id'])
            if self.request.user != borrower:
                serializer = self.get_serializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                self.perform_create(serializer)
                headers = self.get_success_headers(serializer.data)
                return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
            else:
                return Response({'borrower_id': 'You can not lend item for yourself'},
                                status=status.HTTP_400_BAD_REQUEST)
        except ObjectDoesNotExist:
            return Response({'borrower_id': 'Object with email=' + data['borrower_id'] + ' does not exist.'},
                            status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        serializer.save(lender_id=self.request.user, loan_status_id_id="1")

    def get_queryset(self):
        qs = MoneyLoan.objects.filter(lender_id=self.request.user) | MoneyLoan.objects.filter(borrower_id=self.request.
                                                                                              user)
        return qs


class MoneyLoanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = MoneyLoan.objects.all()
    serializer_class = MoneyLoanSerializer
    name = 'moneyloan-detail'

    def destroy(self, *args, **kwargs):
        self.get_object().create_notification_on_delete()
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)
# </editor-fold>
# <editor-fold desc="API ROOT">


class ApiRoot(generics.GenericAPIView):
    name = 'api-root'

    def get(self, request, *args, **kwargs):
        return Response({'item_category': reverse(ItemCategoryList.name, request=request),
                         'loan_status': reverse(LoanStatusList.name, request=request),
                         'loan': reverse(LoanList.name, request=request),
                         })
# </editor-fold>
# <editor-fold desc="Returns">


class ReturnLend(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            lend_id = json.loads(request.body)
            loan = Loan.objects.get(id=lend_id)
            loan.loan_status_id_id = 2
            loan.create_notification_on_return()
            loan.save()
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)


class ReturnMoneyLend(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            lend_id = json.loads(request.body)
            loan = MoneyLoan.objects.get(id=lend_id)
            loan.loan_status_id_id = 2
            loan.create_notification_on_return()
            loan.save()
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)

# </editor-fold>
# <editor-fold desc="Notifications">


class NotificationList(generics.ListCreateAPIView):
    serializer_class = NotificationSerializer
    name = 'notification-list'
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        qs = Notification.objects.filter(receiver_id=self.request.user, show_date__lte=datetime.date.today())
        return qs


class NotificationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Loan.objects.all()
    serializer_class = NotificationSerializer
    name = 'notification-detail'

    def destroy(self, *args, **kwargs):
        serializer = self.get_serializer(self.get_object())
        super().destroy(*args, **kwargs)
        return response.Response(serializer.data, status=status.HTTP_200_OK)

# <editor-fold desc="Requests and reminders">


class RequestLongerMoneyReturnTime(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            data = json.loads(request.body)
            loan = MoneyLoan.objects.get(id=data['id'])
            loan.create_notification_ask_for_longer_return(data['date'])
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)


class RequestEarlierMoneyReturn(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            data = json.loads(request.body)
            loan = MoneyLoan.objects.get(id=data['id'])
            loan.create_notification_ask_for_return(data['date'])
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)


class SetMoneyNotification(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
            'exist': 0
        }
        try:
            data = json.loads(request.body)
            loan = MoneyLoan.objects.get(id=data['id'])
            exist = Notification.objects.filter(show_date=data['date']).filter(title__startswith="Przypomnienie") \
                .filter(frontend_url__endswith=str("loan-money/" + str(loan.pk)))
            if exist.count() == 0:
                loan.create_notification(data['date'])
                return_response['status'] = 200
            else:
                return_response['status'] = 400
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)


class RequestLongerItemReturnTime(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            data = json.loads(request.body)
            loan = Loan.objects.get(id=data['id'])
            loan.create_notification_ask_for_longer_return(data['date'])
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)


class RequestEarlierItemReturn(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            data = json.loads(request.body)
            loan = Loan.objects.get(id=data['id'])
            loan.create_notification_ask_for_return(data['date'])
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)


class SetItemNotification(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            data = json.loads(request.body)
            loan = Loan.objects.get(id=data['id'])
            exist = Notification.objects.filter(show_date=data['date']).filter(title__startswith="Przypomnienie") \
                .filter(frontend_url__endswith=str("loan-items/" + str(loan.pk)))
            if exist.count() == 0:
                loan.create_notification(data['date'])
                return_response['status'] = 200
            else:
                return_response['status'] = 400
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)
# </editor-fold>
# <editor-fold desc="Seen">


class SetAsSeen(generics.GenericAPIView):
    def post(self, request):
        return_response = {
            'status': 403,
        }
        try:
            notification_id = json.loads(request.body)
            notification = Notification.objects.get(id=notification_id)
            notification.is_seen = True
            notification.save()
            return_response['status'] = 200
            return JsonResponse(return_response)
        except Exception:
            return JsonResponse(return_response)


class SetAllAsSeen(generics.GenericAPIView):
    def post(self, request):
        try:
            notification = Notification.objects.filter(receiver_id_id=self.request.user,
                                                       show_date__lte=datetime.date.today())
            for i in notification:
                i.is_seen = True
                i.save()
            return response.Response("Successfully set all notification as seen", status=status.HTTP_200_OK)
        except:
            return response.Response("Notification not found", status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>
# <editor-fold desc="Delete">


class DeleteNotification(generics.GenericAPIView):
    def delete(self, request):
        try:
            notification_id = json.loads(request.body)
            notification = Notification.objects.get(id=notification_id , receiver_id_id=self.request.user)
            notification.delete()
            return response.Response("Successfully notification deleted", status=status.HTTP_200_OK)

        except Exception:
            return response.Response("Notification not found", status=status.HTTP_400_BAD_REQUEST)


class DeleteAllNotification(generics.GenericAPIView):
    def delete(self, request):
        try:

            notification = Notification.objects.filter(receiver_id_id=self.request.user,
                                                       show_date__lte=datetime.date.today())
            notification.delete()
            return response.Response("Successfully all notification deleted", status=status.HTTP_200_OK)

        except Exception:
            return response.Response("No notifications were found for this user", status=status.HTTP_400_BAD_REQUEST)
# </editor-fold>
# </editor-fold>
# <editor-fold desc="Contact list">


class ContactList(generics.ListCreateAPIView):
    serializer_class = ContactSerializer
    name = 'contact-list'

    def get_queryset(self):
        qs = Contact.objects.filter(user_id=self.request.user)
        return qs

    def delete(self, request):
        try:
            friend_id = json.loads(request.body)
            friend = Contact.objects.get(id=friend_id, user_id_id=self.request.user)
            friend.delete()
            return response.Response("Successfully friend deleted", status=status.HTTP_200_OK)
        except Exception:
            return response.Response("Friend not found", status=status.HTTP_400_BAD_REQUEST)


class ContactDetail(generics.RetrieveAPIView):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    name = 'contact-detail'
# </editor-fold>
