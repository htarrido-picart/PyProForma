from proforma.Inputs import ProceedsHelper

class myProceeds:
    '''
    A generic proceeds class that can be used for any type of use:
    Residential, Commercial, Manufacturing
    '''

    # NYCHA Vacancy
    vacancy_rate = 0.05 #0.012
    income_escalation = 0.02 # 0.01

    #NYCHA Operation Costs
    operation_expense_persqft = 7 #USD
    realestate_taxes_persqft = 3 #0 #USD
    replacement_reserve_persqft = 1 #USD
    depreciation_yrs = 27.5   # in years

    income = 0
    vacancy = 0
    units = 0
    net_area = 0


    def __init__(self,
                 proceeds_type: str,
                 gross_floor_area: int,
                 avg_unit_size: float,
                 development_cost: int,
                 rent: int,
                 net_loss_factor: float,
                 ):

        self.development_cost = development_cost
        self.gross_floor_area = gross_floor_area
        self.avg_unit_size = avg_unit_size
        self.proceeds_type = proceeds_type
        self.rent = rent
        self.net_loss_factor = net_loss_factor

        #Proceeds
        common_circulation = ProceedsHelper.common_area_and_circulation(total_floor_area= gross_floor_area,
                                                                        net_loss_factor= self.net_loss_factor)

        self.net_area = ProceedsHelper.net_area(total_floor_area= gross_floor_area,
                                               common_area_and_circulation= gross_floor_area * self.net_loss_factor)

        self.units = ProceedsHelper.approximate_units(net_area= self.net_area,
                                                      avg_market_rate_unit_size= avg_unit_size)

        self.income = ProceedsHelper.total_income(approx_units= self.units,
                                                  rent_per_unit= self.rent)

        self.vacancy = ProceedsHelper.total_vacancy(vacancy_rate= self.vacancy_rate,
                                                    total_income= self.income)

        #Expenses
        self.operation_expense = ProceedsHelper.operational_expenses(net_area= self.net_area,
                                                                     operational_expenses= self.operation_expense_persqft)

        self.realestate_taxes = ProceedsHelper.real_estate_taxes(real_estate_taxes= self.realestate_taxes_persqft,
                                                                 net_area= self.net_area)

        self.replacement_reserve = ProceedsHelper.replacement_reserve(total_floor_area= gross_floor_area,
                                                                      replacement_reserve= self.replacement_reserve_persqft)

        #Depreciation

        self.depreciation = ProceedsHelper.depreciation(depreciation= self.depreciation_yrs,
                                                        use_sqft_total_cost= self.net_area * self.development_cost)

        print("\n")
        print("{} Proceeds".format(proceeds_type))
        print("Common Area and Circulation: {:,}".format(common_circulation))
        print("Net {} Area: {:,}".format(proceeds_type, self.net_area))
        print("Units: {}".format(self.units))
        print("{} Vacancy Rate: {:,}".format(proceeds_type, self.vacancy_rate))
        print("{} Market Rate Rent: ${:,}".format(proceeds_type, self.rent))
        print("{} Total Income: ${:,}".format(proceeds_type,self.income))
        print("{} Total Vacancy Cost: ${:,}".format(proceeds_type,self.vacancy))

        print("\n")
        print("{} Expenses".format(proceeds_type))
        print("{} Operational Expense per SqFt: ${:,}".format(proceeds_type, self.operation_expense_persqft))
        print("{} Real Estate Taxes per SqFt: ${:,}".format(proceeds_type, self.realestate_taxes_persqft))
        print("{} Replacement Reserve per SqFt: ${:,}".format(proceeds_type, self.replacement_reserve_persqft))
        print("{} Operational Expense Total: ${:,}".format(proceeds_type, self.operation_expense))
        print("{} Real Estate Taxes Total: ${:,}".format(proceeds_type, self.realestate_taxes))
        print("{} Replacement Reserve Total: ${:,}".format(proceeds_type, self.replacement_reserve))

        print("\n")
        print("{} Depreciation".format(proceeds_type))
        print("{} Depreciation in Yrs: {}".format(proceeds_type, self.depreciation_yrs))
        print("Total Depreciation: ${:,}".format(self.depreciation))