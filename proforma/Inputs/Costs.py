from proforma.Inputs  import CostHelper


class development_costs():

    currency = "USD"
    total_development_cost = 0

    def __init__(self,
                 lot_area: int,
                 landscape_gross_sqft: int,
                 residential_gross_sqft: int,
                 commercial_gross_sqft: int,
                 manufacturing_gross_sqft: int,
                 community_gross_sqft: int,
                 landscape_cost: int,
                 residential_cost: int,
                 commercial_cost: int,
                 manufacturing_cost: int,
                 community_cost: int,
                 hard_cost: int,
                 soft_cost: int,
                 land_cost: int,
                 existingBuildingPurchase: int
                 ):

        # Development Costs
        self.lot_area = lot_area
        self.landscape_cost = landscape_cost
        self.residential_gross_sqft = residential_gross_sqft
        self.commerical_gross_sqft = commercial_gross_sqft
        self.manufacturing_gross_sqft = manufacturing_gross_sqft
        self.community_gross_sqft = community_gross_sqft
        self.residential_cost = residential_cost  # $ per sqft
        self.commercial_cost = commercial_cost  # $ per sqft
        self.manufacturing_cost = manufacturing_cost  # $ per sqft
        self.community_cost = community_cost
        self.hard_cost = hard_cost  # $ per sqft
        self.soft_cost = soft_cost  # $ per sqft
        self.land_cost = land_cost  # $ per sqft
        self.existingBuildingPurchase = existingBuildingPurchase # flat purchase price


        self.gross_sqft = sum([residential_gross_sqft,
                               commercial_gross_sqft,
                               manufacturing_gross_sqft,
                               community_gross_sqft])

        print("")
        print("My development costs ({})".format(self.currency))

        my_land_purchase_cost = CostHelper.use_cost_calculator(type='Land Purchase',
                                                               gross_sqft=lot_area,
                                                               cost_per_sqft= self.land_cost)

        my_landscape_cost = CostHelper.use_cost_calculator(type='Landscape',
                                                           gross_sqft= landscape_gross_sqft,
                                                           cost_per_sqft= self.landscape_cost)

        my_residential_costs = CostHelper.use_cost_calculator(type='Residential',
                                                              gross_sqft= residential_gross_sqft,
                                                              cost_per_sqft= self.residential_cost)

        my_commercial_costs = CostHelper.use_cost_calculator(type='Commercial',
                                                             gross_sqft= commercial_gross_sqft,
                                                             cost_per_sqft= self.commercial_cost)

        my_manufacturing_costs = CostHelper.use_cost_calculator(type='Manufacturing',
                                                                gross_sqft= manufacturing_gross_sqft,
                                                                cost_per_sqft= self.manufacturing_cost)

        my_community_costs = CostHelper.use_cost_calculator(type='Community',
                                                            gross_sqft = community_gross_sqft,
                                                            cost_per_sqft= self.community_cost)

        my_hard_costs = CostHelper.hard_cost(gross_sqft= self.gross_sqft,
                                             hard_cost= self.hard_cost)

        my_soft_costs = CostHelper.soft_cost(gross_sqft= self.gross_sqft,
                                             soft_cost= self.soft_cost)

        self.total_development_cost = CostHelper.total_development_cost(existing_building_purchase = self.existingBuildingPurchase,
                                                                        total_lot_purchase_cost = my_land_purchase_cost,
                                                                        total_landscape_cost = my_landscape_cost,
                                                                        total_residential_cost= my_residential_costs,
                                                                        total_commercial_cost= my_commercial_costs,
                                                                        total_manufacturing_cost= my_manufacturing_costs,
                                                                        total_community_cost= my_community_costs,
                                                                        total_hard_cost= my_hard_costs,
                                                                        total_soft_cost= my_soft_costs)


