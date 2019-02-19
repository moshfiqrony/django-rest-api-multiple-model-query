from rest_framework.routers import DefaultRouter
from .views import CLViews, AgentViews, CampaignViews, CampaignDetailsViews

router = DefaultRouter()
router.register(r'cl', CLViews, base_name='ClViews')
router.register(r'agent', AgentViews, base_name='AgentViews')
router.register(r'campaign', CampaignViews, base_name='CampaignViews')
router.register(r'campaignDetails', CampaignDetailsViews, base_name='CampaignDetailsViews')
urlpatterns = router.urls
