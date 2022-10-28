
from django.shortcuts import render
from rest_framework.views import APIView
from tracker import serializers
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import User, Iou
from django.db.models import Q
from django.http import JsonResponse

# Create your views here.

class UserApiView(APIView):
    serializer_class = serializers.UserSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = serializer.validated_data.get('user')
            return Response({'user':user })
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class IOUApiView(APIView):
    serializer_class = serializers.IOUSerializer
    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            lender = serializer.validated_data.get('lender')
            borrower = serializer.validated_data.get('borrower')
            if (lender == borrower):
                return Response( {
                    "detail": 'Lender and borrower cannot be the same user' 
                },
                status=status.HTTP_400_BAD_REQUEST
                )
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )

class SettleupApiView(APIView):
    def get(self, request):
        payload = None
        if ( 'payload' in request.GET):
            payload = request.GET['payload']

        if (payload):
            #response = Iou.objects.select_related('lender').order_by('lender__user')
            response = User.objects.order_by('user')
            return Response({'users' : self.process_queryset(response)})

        else:
            response = User.objects.all()
            return Response({'users' : self.process_queryset(response)})

    def process_queryset(self, queryset):
        return map(self.extra, queryset) # Using map instead list you can save memory.

    def extra(self, obj):
        obj.user = obj.user
        debts = Iou.objects.order_by('lender_id', 'borrower_id').filter(Q(lender=obj.user) | Q(borrower=obj.user))
        owes = {}
        owed_by = {}
        sum_owes = 0
        sum_owed_by = 0
        for debt in debts:
            if (debt.borrower_id == obj.user):
                if (debt.lender_id in owes):
                    owes[debt.lender_id] = owes[debt.lender_id] + debt.amount
                else:
                    owes[debt.lender_id] = debt.amount
                sum_owes = sum_owes + debt.amount
            else:
                if (debt.borrower_id in owed_by):
                    owed_by[debt.borrower_id] = owed_by[debt.borrower_id] + debt.amount
                else:
                    owed_by[debt.borrower_id] = debt.amount
                sum_owed_by = sum_owed_by + debt.amount

        return {
            'name': obj.user,
            'owes': owes,
            'owed_by': owed_by,
            'balance': sum_owed_by - sum_owes
        }   
