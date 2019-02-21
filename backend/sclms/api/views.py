from rest_framework import viewsets, status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend

from .serializers import CLSerializers, AgentSerializers, CampaignSerializers, AddCampaignDetailsSerializers, \
    CampaignDetailsSerializers
from ..models import CL, Agent, Campaign, CampaignDetails


class CLViews(viewsets.ModelViewSet):
    queryset = CL.objects.all()
    serializer_class = CLSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('phone',)


class AgentViews(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializers


class CampaignViews(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializers


class AddCampaignDetailsViews(viewsets.ModelViewSet):
    queryset = CampaignDetails.objects.all()
    serializer_class = AddCampaignDetailsSerializers


class CampaignDetailsViews(viewsets.ModelViewSet):
    queryset = CampaignDetails.objects.all()
    serializer_class = CampaignDetailsSerializers
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('clId', 'campaignId',)
