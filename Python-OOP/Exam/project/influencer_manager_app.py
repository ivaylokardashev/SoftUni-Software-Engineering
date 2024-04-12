from typing import List
from project.campaigns.high_budget_campaign import HighBudgetCampaign
from project.campaigns.low_budget_campaign import LowBudgetCampaign
from project.influencers.base_influencer import BaseInfluencer
from project.campaigns.base_campaign import BaseCampaign
from project.influencers.premium_influencer import PremiumInfluencer
from project.influencers.standard_influencer import StandardInfluencer


class InfluencerManagerApp:
    INFLUENCER_DICT = {"PremiumInfluencer": PremiumInfluencer, "StandardInfluencer": StandardInfluencer}
    CAMPAIGN_DICT = {"HighBudgetCampaign": HighBudgetCampaign, "LowBudgetCampaign": LowBudgetCampaign}

    def __init__(self):
        self.influencers: List[BaseInfluencer] = []
        self.campaigns: List[BaseCampaign] = []

    def register_influencer(self, influencer_type: str, username: str, followers: int, engagement_rate: float):
        if influencer_type not in InfluencerManagerApp.INFLUENCER_DICT:
            return f"{influencer_type} is not an allowed influencer type."

        try:
            influencer = next(filter(lambda i: i.username == username, self.influencers))
            return f"{influencer.username} is already registered."
        except StopIteration:
            new_influencer = InfluencerManagerApp.INFLUENCER_DICT[influencer_type](username, followers, engagement_rate)
            self.influencers.append(new_influencer)
            return f"{username} is successfully registered as a {influencer_type}."

    def create_campaign(self, campaign_type: str, campaign_id: int, brand: str, required_engagement: float):
        if campaign_type not in InfluencerManagerApp.CAMPAIGN_DICT:
            return f"{campaign_type} is not a valid campaign type."

        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
            return f"Campaign ID {campaign.campaign_id} has already been created."
        except StopIteration:
            new_campaign = InfluencerManagerApp.CAMPAIGN_DICT[campaign_type](campaign_id, brand, required_engagement)
            self.campaigns.append(new_campaign)
            return f"Campaign ID {campaign_id} for {brand} is successfully created as a {campaign_type}."

    def participate_in_campaign(self, influencer_username: str, campaign_id: int):
        try:
            influencer = next(filter(lambda i: i.username == influencer_username, self.influencers))
        except StopIteration:
            return f"Influencer '{influencer_username}' not found."
        try:
            campaign = next(filter(lambda c: c.campaign_id == campaign_id, self.campaigns))
        except StopIteration:
            return f"Campaign with ID {campaign_id} not found."

        if not campaign.check_eligibility(influencer.engagement_rate):
            return f"Influencer '{influencer_username}' does not meet the eligibility criteria for the campaign " \
                   f"with ID {campaign_id}."

        if influencer.calculate_payment(campaign) > 0.0:
            campaign.approved_influencers.append(influencer)
            campaign.budget -= influencer.calculate_payment(campaign)
            influencer.campaigns_participated.append(campaign)
            return f"Influencer '{influencer_username}' has successfully " \
                   f"participated in the campaign with ID {campaign_id}."

    def calculate_total_reached_followers(self):
        result = {}
        for c in self.campaigns:
            result[c] = 0
            for i in c.approved_influencers:
                result[c] += i.reached_followers(c.__class__.__name__)

        return result

    def influencer_campaign_report(self, username: str):
        influencer = next(filter(lambda i: i.username == username, self.influencers))
        return influencer.display_campaigns_participated()

    def campaign_statistics(self):
        sorted_campaigns = sorted(self.calculate_total_reached_followers(), key=lambda c: (len(c.approved_influencers), -c.budget))
        result = "$$ Campaign Statistics $$\n"
        result += "  * "
        result += '\n  * '.join(f"Brand: {c.brand}, Total influencers: {len(c.approved_influencers)}, "
                                f"Total budget: ${c.budget:.2f},"
                                f" Total reached followers: "
                                f"{sum(influencer.reached_followers(c.__class__.__name__) for influencer in c.approved_influencers)}"
                                for c in sorted_campaigns)

        return result

