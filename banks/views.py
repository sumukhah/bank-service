from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from .serializers import BankSerializer, BranchSerializer
from .models import Branches, Banks
from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework.views import APIView, Response
from rest_framework.response import Response
import json


class BranchDetailView(RetrieveAPIView):
    '''
    API for retrieve branch detail using ifsc
    '''
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer
    lookup_field = 'ifsc'


class BranchListView(APIView):
    '''
    API for retrieve branches list using bank name, city
    '''

    def get(self, request, format=None, *args, **kwargs):
        city = kwargs['city'].upper()
        bank_name = kwargs['bank'].upper().replace('_', ' ')

        branches = Branches.objects.filter(city=city, bank__name=bank_name)
        filtered_branches = BranchSerializer(branches, many=True)
        return Response(filtered_branches.data)
