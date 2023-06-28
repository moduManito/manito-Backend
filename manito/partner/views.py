from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView


class PartnerListRetrieveAPIView(ListAPIView, RetrieveAPIView):
    pass
