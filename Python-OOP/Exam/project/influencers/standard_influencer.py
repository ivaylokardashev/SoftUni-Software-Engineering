from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.campaigns.base_campaign import BaseCampaign


class StandardInfluencer(BaseInfluencer):
    PAYMENT_PERCENTAGE = 0.45

    def __int__(self, username: str, followers: int, engagement_rate: float):
        super().__init__(username, followers, engagement_rate)

    def calculate_payment(self, campaign: BaseCampaign):
        payment = campaign.budget * StandardInfluencer.PAYMENT_PERCENTAGE

        return payment

    def reached_followers(self, campaign_type: str):
        followers_for_campaign = 0

        if campaign_type == "HighBudgetCampaign":
            followers_for_campaign = self.followers * self.engagement_rate * 1.2
        elif campaign_type == "LowBudgetCampaign":
            followers_for_campaign = self.followers * self.engagement_rate * 0.9

        return int(followers_for_campaign)