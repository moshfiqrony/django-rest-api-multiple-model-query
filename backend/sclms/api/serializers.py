from rest_framework import serializers

from ..models import CL, Agent, Campaign, CampaignDetails


class CLSerializers(serializers.ModelSerializer):
    class Meta:
        model = CL
        fields = ('id', 'phone', 'password')


class AgentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ('id', 'phone', 'password')


class CampaignSerializers(serializers.ModelSerializer):
    class Meta:
        model = Campaign
        fields = ('id', 'name')


class AddCampaignDetailsSerializers(serializers.ModelSerializer):
    class Meta:
        model = CampaignDetails
        fields = ('id', 'clId', 'agentId', 'campaignId')


class CampaignDetailsSerializers(serializers.ModelSerializer):
    clId = CLSerializers(read_only=True,)
    agentId = AgentSerializers(read_only=True)
    campaignId = CampaignSerializers(read_only=True)
    class Meta:
        model = CampaignDetails
        fields = ('id', 'clId', 'agentId', 'campaignId')
