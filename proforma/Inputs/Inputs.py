
class PropertyInputs():

    total_floor_area = 0

    def __init__(self,
                 existingBuildingFloorArea,
                 net_loss_factor,
                 residential_gross_sqft,
                 commercial_gross_sqft,
                 manufacturing_gross_sqft,
                 community_gross_sqft
                 ):

        # Starting Assumptions Constants
        self.existingBuildingFloorArea = existingBuildingFloorArea
        self.net_loss_factor = net_loss_factor
        self.residential_gross_sqft = residential_gross_sqft
        self.commercial_gross_sqft = commercial_gross_sqft
        self.manufacturing_gross_sqft = manufacturing_gross_sqft
        self.community_gross_sqft = community_gross_sqft


        self.total_floor_area = sum([self.residential_gross_sqft,
                                     self.commercial_gross_sqft,
                                     self.manufacturing_gross_sqft,
                                     self.community_gross_sqft])

        net_floor_area = self.total_floor_area - (self.total_floor_area * self.net_loss_factor)



