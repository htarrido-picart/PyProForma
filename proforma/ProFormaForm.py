from proforma.Inputs import InputsAssumptions as Inputs
from proforma.Results import Results
from proforma.Schedule import ScheduleDataFrame as Schedule

class ProForma:
    '''
    This class builds a proforma using the following inputs:
    1. Property Information
    2. Assumptions About Cost and Capital Structure
    3. Projected Proceeds from Residential, Commercial and Manufacturing
    4. Tax, Capital and other specific types of rates
    ---

    It then calculates:
    1. Gross Income Totals
    2. A cost schedule
    3. Results including: Net Book Value, Gain on Sale, Tax Payment, Net proceed from sale
    4. Return Metrics: Net Present Value, Leveraged IRR After Tax, Capitalize Value, ROTA, Return on equity
    '''
    def __init__(self,
                 verbose: bool,
                 exportToExcel: bool,
                 yrs: int,
                 start_year: int,
                 lot_area: float,
                 equity: float,
                 landscape_gross_sqft: int,
                 existingBuildingFloorArea: float,
                 existingBuildingPurchase: int,
                 net_loss_factor: float,
                 residential_gross_sqft: float,
                 commercial_gross_sqft: float,
                 manufacturing_gross_sqft: float,
                 community_gross_sqft: float,
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

        self.yrs= yrs
        self.start_year= start_year
        self.lot_area= lot_area
        self.equity= equity
        self.landscape_gross_sqft = landscape_gross_sqft
        self.existingBuildingFloorArea= existingBuildingFloorArea
        self.existingBuildingPurchase= existingBuildingPurchase
        self.residential_gross_sqft= residential_gross_sqft
        self.commercial_gross_sqft= commercial_gross_sqft
        self.manufacturing_gross_sqft= manufacturing_gross_sqft
        self.community_gross_sqft= community_gross_sqft
        self.avgUnitSize_residential= avgUnitSize_residential
        self.avgUnitSize_commercial= avgUnitSize_commercial
        self.avgUnitSize_manufacturing= avgUnitSize_manufacturing
        self.avgUnitSize_community= avgUnitSize_community
        self.residential_cost= residential_cost
        self.commercial_cost= commercial_cost
        self.manufacturing_cost= manufacturing_cost
        self.community_cost= community_cost
        self.hard_cost= hard_cost
        self.soft_cost= soft_cost
        self.land_cost= land_cost
        self.landscape_cost = landscape_cost
        self.residential_rent = residential_rent
        self.residential_AMI = residential_AMI
        self.commercial_rent = commercial_rent
        self.manufacturing_rent = manufacturing_rent
        self.community_rent = community_rent
        self.residential_AMI = residential_AMI

        # 1. Property Information
        self.propertyInput = Inputs.MyInputsAssumptions(equity = equity,
                                                        net_loss_factor= net_loss_factor,
                                                        lot_area= lot_area,
                                                        existingBuildingFloorArea= existingBuildingFloorArea,
                                                        existingBuildingPurchase= existingBuildingPurchase,
                                                        landscape_gross_sqft = landscape_gross_sqft,
                                                        residential_gross_sqft= residential_gross_sqft,
                                                        commercial_gross_sqft= commercial_gross_sqft,
                                                        community_gross_sqft= community_gross_sqft,
                                                        manufacturing_gross_sqft= manufacturing_gross_sqft,
                                                        avgUnitSize_residential=avgUnitSize_residential,
                                                        avgUnitSize_commercial = avgUnitSize_commercial,
                                                        avgUnitSize_manufacturing = avgUnitSize_manufacturing,
                                                        avgUnitSize_community = avgUnitSize_community,
                                                        landscape_cost= landscape_cost,
                                                        residential_cost= residential_cost,
                                                        commercial_cost= commercial_cost,
                                                        manufacturing_cost= manufacturing_cost,
                                                        community_cost= community_cost,
                                                        hard_cost= hard_cost,
                                                        soft_cost=soft_cost,
                                                        land_cost= land_cost,
                                                        residential_rent= residential_rent,
                                                        commercial_rent= commercial_rent,
                                                        manufacturing_rent= manufacturing_rent,
                                                        community_rent= community_rent,
                                                        residential_AMI = residential_AMI
                                                        )

        # 3. Schedule
        self.schedule = Schedule.ScheduleGrid(yrs = yrs,
                                              start_year= start_year,
                                              total_gross_income= self.propertyInput.totals.total_Gross_Incomes,
                                              total_vacancy= -self.propertyInput.totals.total_vacancy,
                                              operating_expenses=  self.propertyInput.totals.total_Expenses,
                                              real_estate_taxes=  self.propertyInput.totals.total_property_real_estate_taxes,
                                              replacement_reserve=  self.propertyInput.totals.total_property_replacement_reserve,
                                              debt_calc=  self.propertyInput.capitalStructure.debt,
                                              equity = self.propertyInput.capitalStructure.equity,
                                              debt_calc_service=  self.propertyInput.capitalStructure.debt_service,
                                              debt_calc_service_rate= self.propertyInput.capitalStructure.debt_service_percent,
                                              begin_year_balance= self.propertyInput.capitalStructure.debt,
                                              interest_rate= self.propertyInput.rates.ratesDictionary['interest_rate'],
                                              annual_public_subsidy_increase = self.propertyInput.rates.ratesDictionary['annualPublicSubsidiesIncrease'],
                                              depreciation= self.propertyInput.totals.total_depreciation,
                                              odinary_tax_income= self.propertyInput.rates.ratesDictionary['ordinaryIncomeTax'],
                                              )

        # 4. Results
        debt_cash_flow_list = self.schedule.future_cashflow_list.values.tolist()
        debt_cash_flow_list.insert(0, -self.propertyInput.capitalStructure.equity)

        self.results = Results.Results(equity = self.propertyInput.capitalStructure.equity,
                                       net_operating_income= self.schedule.net_operating_income_atStart,
                                       debt_cash_flow_list= debt_cash_flow_list,
                                       cash_flow_after_taxes= self.schedule.cash_flow_after_taxes_atStart,
                                       total_net_operating_income= self.schedule.final_net_operating_income,
                                       total_development_cost= self.propertyInput.development_costs.total_development_cost,
                                       total_replacement_reserve= self.schedule.final_replacement_reserve,
                                       accumulated_depreciation= self.schedule.final_depreciation,
                                       mortgage_payoff= -self.schedule.mortage_payoff)



        # Show Both the Inputs and the Schedule table
        if verbose:
            print(self.schedule.df.to_string())
            print("\n")
            print(self.results.df.to_string())

        # TODO: Lastly, export results to an excel file
        if exportToExcel:
            pass