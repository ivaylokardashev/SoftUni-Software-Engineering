from project.campaigns.base_campaign import BaseCampaign


class HighBudgetCampaign(BaseCampaign):
    budget = 5000.0

    def __init__(self, campaign_id: int, brand: str, required_engagement: float):
        super().__init__(campaign_id, brand, HighBudgetCampaign.budget, required_engagement)

    def check_eligibility(self, engagement_rate: float):
        required_engagement_rate = self.required_engagement * 1.2

        if engagement_rate >= required_engagement_rate:
            return True

        return False