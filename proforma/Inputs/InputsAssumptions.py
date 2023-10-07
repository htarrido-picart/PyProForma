from proforma.Inputs import Inputs, Costs, CapitalStructure, Proceeds, OtherRates, Totals, OtherRates
from proforma.Inputs import inputs_dataframe_rows as df_row_titles
import pandas as pd

class MyInputsAssumptions:
    '''
    Input Assump


    '''
    def __init__(self,
                 equity: float,
                 net_loss_factor: float,
                 lot_area: int,
                 existingBuildingFloorArea: float,
                 existingBuildingPurchase: int,
                 landscape_gross_sqft: int,
                 residential_gross_sqft: int,
                 commercial_gross_sqft: int,
                 manufacturing_gross_sqft: int,
                 community_gross_sqft: int,
                 avgUnitSize_residential: int,
                 avgUnitSize_commercial: int,
                 avgUnitSize_manufacturing: int,
                 avgUnitSize_community: int,
                 residential_cost: int,
                 residential_rent: int,
                 residential_AMI: dict,
                 commercial_cost: int,
                 commercial_rent: int,
                 manufacturing_cost: int,
                 manufacturing_rent: int,
                 community_cost: int,
                 community_rent: int,
                 hard_cost: int,
                 soft_cost: int,
                 land_cost: int,
                 landscape_cost: int
                 ):

        self.lot_area = lot_area
        self.existinBuildingFloorArea = existingBuildingFloorArea
        self.existinBuildingPurchase = existingBuildingPurchase
        self.residential_gross_sqft = residential_gross_sqft
        self.commercial_gross_sqft = commercial_gross_sqft
        self.manufacturing_gross_sqft = manufacturing_gross_sqft
        self.community_gross_sqft = community_gross_sqft
        self.residential_rent = residential_rent
        self.commercial_rent = commercial_rent
        self.manufacturing_rent = manufacturing_rent
        self.community_rent = community_rent
        self.residential_AMI = residential_AMI
        self.residential_cost = residential_cost
        self.commercial_cost = commercial_cost
        self.manufacturing_cost = manufacturing_cost
        self.community_cost = community_cost
        self.hard_cost = hard_cost
        self.soft_cost = soft_cost
        self.land_cost = land_cost
        self.equity = equity
        self.net_loss_factor = net_loss_factor

        self.development = Inputs.PropertyInputs(net_loss_factor= net_loss_factor,
                                                 existingBuildingFloorArea = self.existinBuildingFloorArea,
                                                 residential_gross_sqft = self.residential_gross_sqft,
                                                 commercial_gross_sqft = self.commercial_gross_sqft,
                                                 manufacturing_gross_sqft= self.manufacturing_gross_sqft,
                                                 community_gross_sqft= self.community_gross_sqft)

        self.development_costs = Costs.development_costs( existingBuildingPurchase= existingBuildingPurchase,
                                                          lot_area= lot_area,
                                                          landscape_gross_sqft= landscape_gross_sqft,
                                                          residential_gross_sqft= self.development.residential_gross_sqft,
                                                          commercial_gross_sqft= self.development.commercial_gross_sqft,
                                                          manufacturing_gross_sqft= self.development.manufacturing_gross_sqft,
                                                          community_gross_sqft= self.development.community_gross_sqft,
                                                          landscape_cost= landscape_cost,
                                                          residential_cost = residential_cost,
                                                          commercial_cost= commercial_cost,
                                                          manufacturing_cost= manufacturing_cost,
                                                          community_cost= community_cost,
                                                          hard_cost= hard_cost,
                                                          soft_cost= soft_cost,
                                                          land_cost= land_cost)

        self.capitalStructure = CapitalStructure.CapitalStructure(debt_service_percent= OtherRates.OtherRates.ratesDictionary['constantRate'],
                                                                  total_development_cost= self.development_costs.total_development_cost,
                                                                  equity_percent = self.equity)

        self.residentialProceeds_incomeList = []

        for key,value in residential_AMI.items():
            ami_type = str(key)
            proceeds_type = ami_type + "% AMI " + value[0]
            ami_percent_of_development = value[1]
            ami_avg_unit_size = value[2]
            ami_rent = value[3]



            self.residentialProceeds_ami_income = Proceeds.myProceeds(proceeds_type= proceeds_type,
                                                                      rent = ami_rent,
                                                                      gross_floor_area= self.residential_gross_sqft * ami_percent_of_development,
                                                                      net_loss_factor=self.net_loss_factor,
                                                                      avg_unit_size=ami_avg_unit_size,
                                                                      development_cost= self.residential_cost)

            self.residentialProceeds_incomeList.append(self.residentialProceeds_ami_income.income)

        self.residentialProceeds_income = sum(self.residentialProceeds_incomeList)

        self.residentialProceeds = Proceeds.myProceeds(proceeds_type="Residential",
                                                       rent=residential_rent,
                                                       gross_floor_area=self.residential_gross_sqft,
                                                       net_loss_factor=self.net_loss_factor,
                                                       avg_unit_size=avgUnitSize_residential,
                                                       development_cost=self.residential_cost)

        self.commercialProceeds = Proceeds.myProceeds(proceeds_type="Commercial",
                                                      rent = commercial_rent,
                                                      gross_floor_area=self.commercial_gross_sqft,
                                                      net_loss_factor= self.net_loss_factor,
                                                      avg_unit_size= avgUnitSize_commercial,
                                                      development_cost=self.commercial_cost)

        self.manufacturingProceeds = Proceeds.myProceeds(proceeds_type="Manufacturing",
                                                         rent = manufacturing_rent,
                                                         gross_floor_area=self.manufacturing_gross_sqft,
                                                         net_loss_factor=self.net_loss_factor,
                                                         avg_unit_size= avgUnitSize_manufacturing,
                                                         development_cost= self.manufacturing_cost)

        self.communityProceeds = Proceeds.myProceeds(proceeds_type="Community Facility",
                                                     rent = commercial_rent,
                                                     gross_floor_area=self.community_gross_sqft,
                                                     net_loss_factor=self.net_loss_factor,
                                                     avg_unit_size= avgUnitSize_community,
                                                     development_cost=self.community_cost)

        self.rates = OtherRates.OtherRates

        self.total_property_operational_expenses = sum([self.residentialProceeds.operation_expense,
                                                        self.commercialProceeds.operation_expense,
                                                        self.manufacturingProceeds.operation_expense,
                                                        self.commercialProceeds.operation_expense])

        self.total_property_real_estate_taxes = sum([self.residentialProceeds.realestate_taxes,
                                                     self.commercialProceeds.realestate_taxes,
                                                     self.manufacturingProceeds.realestate_taxes,
                                                     self.communityProceeds.realestate_taxes])

        self.total_property_replacement_reserve = sum([self.residentialProceeds.replacement_reserve,
                                                       self.commercialProceeds.replacement_reserve,
                                                       self.manufacturingProceeds.replacement_reserve,
                                                       self.communityProceeds.replacement_reserve])

        self.totals = Totals.Totals(total_residential_income = self.residentialProceeds_income,
                                    total_residential_vacancy=self.residentialProceeds.vacancy,
                                    total_residential_depreciation=self.residentialProceeds.depreciation,
                                    total_commercial_income=self.commercialProceeds.income,
                                    total_commercial_vacancy=self.commercialProceeds.vacancy,
                                    total_commercial_depreciation=self.commercialProceeds.depreciation,
                                    total_manufacturing_income=self.manufacturingProceeds.income,
                                    total_manufacturing_vacancy=self.manufacturingProceeds.vacancy,
                                    total_manufacturing_depreciation=self.manufacturingProceeds.depreciation,
                                    total_community_income= self.communityProceeds.income,
                                    total_community_vacancy= self.communityProceeds.vacancy,
                                    total_community_depreciation= self.communityProceeds.depreciation,
                                    total_property_operational_expenses = self.total_property_operational_expenses ,
                                    total_property_real_estate_taxes= self.total_property_real_estate_taxes,
                                    total_property_replacement_reserve= self.total_property_replacement_reserve
                                    )

        #TODO: Create a dataframe for storing these values

        pd.set_option('display.float_format', '{:,.2f}'.format)

        df_row_titles.residentialProceeds