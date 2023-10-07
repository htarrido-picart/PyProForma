class Totals:
    def __init__(self,
                 total_residential_income: int,
                 total_commercial_income: int,
                 total_manufacturing_income: int,
                 total_community_income: int,
                 total_residential_vacancy: int,
                 total_commercial_vacancy: int,
                 total_manufacturing_vacancy: int,
                 total_community_vacancy: int,
                 total_property_operational_expenses: int,
                 total_property_real_estate_taxes: int,
                 total_property_replacement_reserve: int,
                 total_residential_depreciation: int,
                 total_commercial_depreciation: int,
                 total_manufacturing_depreciation: int,
                 total_community_depreciation: int):

        self.total_residential_income = total_residential_income
        self.total_commercial_income = total_commercial_income
        self.total_manufacturing_income = total_manufacturing_income
        self.total_community_income = total_community_income

        self.total_residential_vacancy = total_residential_vacancy
        self.total_commercial_vacancy = total_commercial_vacancy
        self.total_manufacturing_vacancy = total_manufacturing_vacancy
        self.total_community_vacancy = total_community_vacancy

        self.total_property_operational_expenses = total_property_operational_expenses
        self.total_property_real_estate_taxes = total_property_real_estate_taxes
        self.total_property_replacement_reserve = total_property_replacement_reserve

        self.total_residential_depreciation = total_residential_depreciation
        self.total_commercial_depreciation = total_commercial_depreciation
        self.total_manufacturing_depreciation = total_manufacturing_depreciation
        self.total_community_depreciation = total_community_depreciation

        print("\n")
        print("#" * 10)

        self.total_Gross_Incomes = sum([total_residential_income,
                                   total_commercial_income,
                                   total_manufacturing_income,
                                   total_community_income])
        print("\n")
        print("Total Residential Income: ${:,}".format(self.total_residential_income))
        print("Total Commercial Income: ${:,}".format(self.total_commercial_income))
        print("Total Manufacturing Income: ${:,}".format(self.total_manufacturing_income))
        print("Total Gross Income: ${:,}".format(self.total_Gross_Incomes))

        self.total_vacancy = sum([self.total_residential_vacancy,
                                  self.total_commercial_vacancy,
                                  self.total_manufacturing_vacancy,
                                  self.total_community_vacancy])

        print("\n")
        print("Total Residential Vacancy: ${:,}".format(self.total_residential_vacancy))
        print("Total Commercial Vacancy: ${:,}".format(self.total_commercial_vacancy))
        print("Total Manufacturing Vacancy: ${:,}".format(self.total_manufacturing_vacancy))
        print("Total Vacancy: ${:,}".format(self.total_vacancy))


        self.total_Expenses = sum([self.total_property_operational_expenses,
                              self.total_property_real_estate_taxes,
                              self.total_property_replacement_reserve])

        print("\n")
        print("Total Property Operational Expenses: ${:,}".format(self.total_property_operational_expenses))
        print("Total Property Real Estate Tax: ${:,}".format(self.total_property_real_estate_taxes))
        print("Total Property Replacement Reserve: ${:,}".format(self.total_property_replacement_reserve))
        print("Total Expenses: ${:,}".format(self.total_Expenses))

        self.total_depreciation = sum([self.total_residential_depreciation,
                                  self.total_commercial_depreciation,
                                  self.total_manufacturing_depreciation,
                                  self.total_community_depreciation ])

        print("\n")
        print("Total Residential Depreciation: ${:,}".format(self.total_residential_depreciation))
        print("Total Commercial Depreciation: ${:,}".format(self.total_commercial_depreciation))
        print("Total Manufacturing Depreciation: ${:,}".format(self.total_manufacturing_depreciation))
        print("Total Depreciation: ${:,}".format(self.total_depreciation))
        print("\n")