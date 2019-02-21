from django.db import models


class Districts(models.Model):
    name = models.CharField(max_length=30)


class CL(models.Model):
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30, null=True)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=30, null=True)


class Agent(models.Model):
    phone = models.CharField(max_length=20)
    password = models.CharField(max_length=30)
    name = models.CharField(max_length=30, null=True)
    district = models.ForeignKey(Districts, on_delete=models.CASCADE, null=True)
    address = models.CharField(max_length=30, null=True)

class Campaign(models.Model):
    name = models.CharField(max_length=30)


class CampaignDetails(models.Model):
    clId = models.ForeignKey(CL, on_delete=models.CASCADE)
    agentId = models.ForeignKey(Agent, on_delete=models.CASCADE)
    campaignId = models.ForeignKey(Campaign, on_delete=models.CASCADE)
