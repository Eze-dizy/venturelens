class InvestmentThesis:
    def __init__(self, fund_name, preferred_geographies, preferred_sectors, excluded_sectors,
                 preferred_stage, typical_investment, minimum_revenue, preferred_revenue_model,
                 growth_expectations, preferred_customer_type, market_characteristics,
                 business_model_preferences, team_preferences, other_criteria):
        self.fund_name = fund_name
        self.preferred_geographies = preferred_geographies
        self.preferred_sectors = preferred_sectors
        self.excluded_sectors = excluded_sectors
        self.preferred_stage = preferred_stage
        self.typical_investment = typical_investment
        self.minimum_revenue = minimum_revenue
        self.preferred_revenue_model = preferred_revenue_model
        self.growth_expectations = growth_expectations
        self.preferred_customer_type = preferred_customer_type
        self.market_characteristics = market_characteristics
        self.business_model_preferences = business_model_preferences
        self.team_preferences = team_preferences
        self.other_criteria = other_criteria

    @classmethod
    def empty(cls):
        return cls("", [], [], [], "", 0, 0, "", "", "", "", [], [], [])

    def to_dict(self):
        return {
            "fund_name": self.fund_name,
            "preferred_geographies": self.preferred_geographies,
            "preferred_sectors": self.preferred_sectors,
            "excluded_sectors": self.excluded_sectors,
            "preferred_stage": self.preferred_stage,
            "typical_investment": self.typical_investment,
            "minimum_revenue": self.minimum_revenue,
            "preferred_revenue_model": self.preferred_revenue_model,
            "growth_expectations": self.growth_expectations,
            "preferred_customer_type": self.preferred_customer_type,
            "market_characteristics": self.market_characteristics,
            "business_model_preferences": self.business_model_preferences,
            "team_preferences": self.team_preferences,
            "other_criteria": self.other_criteria
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            fund_name=data.get("fund_name"),
            preferred_geographies=data.get("preferred_geographies"),
            preferred_sectors=data.get("preferred_sectors"),
            excluded_sectors=data.get("excluded_sectors"),
            preferred_stage=data.get("preferred_stage"),
            typical_investment=data.get("typical_investment"),
            minimum_revenue=data.get("minimum_revenue"),
            preferred_revenue_model=data.get("preferred_revenue_model"),
            growth_expectations=data.get("growth_expectations"),
            preferred_customer_type=data.get("preferred_customer_type"),
            market_characteristics=data.get("market_characteristics"),
            business_model_preferences=data.get("business_model_preferences"),
            team_preferences=data.get("team_preferences"),
            other_criteria=data.get("other_criteria")
        )