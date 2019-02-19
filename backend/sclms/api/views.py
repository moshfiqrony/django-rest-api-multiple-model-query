from rest_framework import viewsets, status
from rest_framework.response import Response

from .serializers import CLSerializers, AgentSerializers, CampaignSerializers, CampaignDetailsSerializers
from ..models import CL, Agent, Campaign, CampaignDetails


class CLViews(viewsets.ModelViewSet):
    serializer_class = CLSerializers

    def get_queryset(self):
        queryset = CL.objects.all()
        phone = self.request.query_params.get('phone')
        if phone is not None:
            queryset = CL.objects.filter(phone=phone)
            if queryset is None:
                Response(status=status.HTTP_404_NOT_FOUND)
        return queryset


class AgentViews(viewsets.ModelViewSet):
    queryset = Agent.objects.all()
    serializer_class = AgentSerializers


class CampaignViews(viewsets.ModelViewSet):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializers


class CampaignDetailsViews(viewsets.ModelViewSet):
    queryset = CampaignDetails.objects.all()
    serializer_class = CampaignDetailsSerializers
