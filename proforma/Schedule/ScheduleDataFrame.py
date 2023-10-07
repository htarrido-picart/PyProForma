import pandas as pd

class ScheduleGrid:

    def __init__(self,
                 yrs: int,
                 start_year: int,
                 total_gross_income: float,
                 total_vacancy: float,
                 operating_expenses: float,
                 real_estate_taxes: float,
                 replacement_reserve: float,
                 debt_calc: float,
                 equity: float,
                 debt_calc_service: float,
                 debt_calc_service_rate: float,
                 begin_year_balance: float,
                 interest_rate: float,
                 depreciation: float,
                 odinary_tax_income: float,
                 annual_public_subsidy_increase: float
                 ):

        self.yrs = yrs
        self.start_year = start_year
        schedule_dates = pd.Series(pd.date_range(start=str(self.start_year), periods=self.yrs, freq='YS')).dt.year

        # pd.options.display.float_format = '${:,}'.format

        rows = ['Income',
                'Potential Gross Income',
                'Vacancy',
                'Effective Gross Income',
                ' ',
                'Expenses',
                'Operating Expenses',
                'Real Estate Taxes',
                'Replacement Reserve',
                'Total Expenses',
                ' ',
                'NET OPERATING INCOME',
                ' ',
                'Annual debt_calc Service',
                'Cash flow after financing',
                'Tax Payment',
                'Cash flow after taxes',
                ' ',
                'RETURN MEASURES',
                'Unleveraged IRR', 'Cash Flow After Financing', 'Before Tax Sales Proceed',
                ' ',
                'Leverahed Before Tax IRR', 'Cash Flow After Taxes', 'Net Procceeds form Sale',
                'Total Future Cash Flow',
                ]

        offsheet_rows = [' ',
                         'OFFSHEET CALCLULATION',
                         'debt_calc Service Components',
                         'Beginning of Year Balance',
                         'End of Year Balance',
                         'Interest',
                         'Ammortization',
                         ' ',
                         'TAX PAYMENT',
                         'Cash Flow After Financing',
                         'Amortization',
                         'Replacement Reserve',
                         'Depreciation',
                         'Taxable Income',
                         'Tax Payment'
                         ]

        self.df = pd.DataFrame(index=rows, columns=schedule_dates)
        self.offsheet_df = pd.DataFrame(index=offsheet_rows, columns=schedule_dates)

        self.df.loc['Income', 'Expenses', 'RETURN MEASURES',
               'Unleveraged IRR', 'Leverahed Before Tax IRR', ' '] = ' '

        self.offsheet_df.loc['OFFSHEET CALCLULATION', 'debt_calc Service Components', 'TAX PAYMENT', ' '] = ' '

        for i in range(0, len(self.df.columns)):
            ### #FIRST ROW
            if i == 0:
                # Income
                self.df.iat[1, i] = total_gross_income
                self.df.iat[2, i] = total_vacancy
                self.df.iat[3, i] = sum([total_gross_income, total_vacancy])  # effective gross income

                # Expenses
                self.df.iat[6, i] = -operating_expenses
                self.df.iat[7, i] = -real_estate_taxes
                self.df.iat[8, i] = -replacement_reserve
                self.df.iat[9, i] = -sum([operating_expenses, real_estate_taxes, replacement_reserve])  # total expenses

                # Net Operating Income & Others
                net_operating_income = sum([self.df.iat[9, i], self.df.iat[3, i]])
                self.df.iat[11, i] = net_operating_income  # Net Operating Income

                annual_debt_calc_service = round(-(debt_calc * debt_calc_service_rate), 2)  # annual debt_calc service
                self.df.iat[13, i] = annual_debt_calc_service

                cash_flow_after_financing = round(sum([net_operating_income, annual_debt_calc_service]),
                                                  2)  # cash flow after financing
                self.df.iat[14, i] = cash_flow_after_financing

                # OffSheet Calculations
                self.offsheet_df.iat[3, i] = begin_year_balance  # begin of year balance

                end_year_balance = begin_year_balance - debt_calc_service  # end of year balance
                self.offsheet_df.iat[4, i] = end_year_balance

                interest = round(begin_year_balance * interest_rate, 2)  # interest
                self.offsheet_df.iat[5, i] = interest

                ammortization = round(debt_calc_service - interest, 2)
                self.offsheet_df.iat[6, i] = ammortization

                self.offsheet_df.iat[9, i] = cash_flow_after_financing
                self.offsheet_df.iat[10, i] = ammortization
                self.offsheet_df.iat[11, i] = replacement_reserve
                self.offsheet_df.iat[12, i] = depreciation

                taxable_income = round(
                    sum([cash_flow_after_financing, ammortization, replacement_reserve, depreciation]), 2)
                self.offsheet_df.iat[13, i] = taxable_income

                tax_payment = round(taxable_income * odinary_tax_income, 2)
                self.offsheet_df.iat[14, i] = tax_payment

                # Operatin Income Part 2
                self.df.iat[15, i] = tax_payment

                cash_flow_after_taxes = cash_flow_after_financing - tax_payment
                self.df.iat[16, i] = cash_flow_after_taxes

                # Return Measures
                # Unleveraged
                self.df.iat[20, i] = cash_flow_after_financing
                self.df.iat[21, i] = cash_flow_after_financing

                # Leveraged
                self.df.iat[24, i] = cash_flow_after_taxes
                self.df.iat[25, i] = 0
                self.df.iat[26, i] = sum([self.df.iat[24, i], self.df.iat[25, i]])

            else:
                #Other rows
                annual_subsidy_adjust = 1 + annual_public_subsidy_increase

                # Income
                self.df.iat[1, i] = round(self.df.iat[1, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[2, i] = round(self.df.iat[2, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[3, i] = round(sum([self.df.iat[1, i], self.df.iat[2, i]]), 2)  # effective gross incom

                #Expenses
                # Expenses
                self.df.iat[6, i] = round(self.df.iat[6, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[7, i] = round(self.df.iat[7, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[8, i] = round(self.df.iat[8, i - 1] * annual_subsidy_adjust, 2)
                self.df.iat[9, i] = round(sum([self.df.iat[6, i], self.df.iat[7, i], self.df.iat[8, i]]), 2)  # total expenses

                # Net Operating Income & Others
                net_operating_income = round(sum([self.df.iat[9, i], self.df.iat[3, i]]), 2)
                self.df.iat[11, i] = net_operating_income  # Net Operating Income

                annual_debt_calc_service = round(-(debt_calc * debt_calc_service_rate), 2)  # annual debt_calc service
                self.df.iat[13, i] = annual_debt_calc_service

                cash_flow_after_financing = round(sum([net_operating_income, annual_debt_calc_service]),
                                                  2)  # cash flow after financing

                self.df.iat[14, i] = cash_flow_after_financing

                # OffSheet Calculations
                begin_year_balance = self.offsheet_df.iat[4,i-1]
                self.offsheet_df.iat[3, i] = begin_year_balance # begin of year balance

                end_year_balance = begin_year_balance - debt_calc_service  # end of year balance
                self.offsheet_df.iat[4, i] = end_year_balance

                interest = round(begin_year_balance * interest_rate, 2)  # interest
                self.offsheet_df.iat[5, i] = interest

                ammortization = round(debt_calc_service - interest, 2)
                self.offsheet_df.iat[6, i] = ammortization

                self.offsheet_df.iat[9, i] = cash_flow_after_financing
                self.offsheet_df.iat[10, i] = ammortization

                replacement_reserve = round(self.offsheet_df.iat[11, i-1] * annual_subsidy_adjust, 2)
                self.offsheet_df.iat[11, i] = replacement_reserve
                self.offsheet_df.iat[12, i] = depreciation

                taxable_income = round(
                    sum([cash_flow_after_financing, ammortization, replacement_reserve, depreciation]), 2)
                self.offsheet_df.iat[13, i] = taxable_income

                tax_payment = round(taxable_income * odinary_tax_income, 2)
                self.offsheet_df.iat[14, i] = tax_payment

                # Operatin Income Part 2
                self.df.iat[15, i] = tax_payment

                cash_flow_after_taxes = round(cash_flow_after_financing - tax_payment, 2)
                self.df.iat[16, i] = cash_flow_after_taxes

                # Return Measures
                # Unleveraged
                self.df.iat[20, i] = cash_flow_after_financing
                self.df.iat[21, i] = cash_flow_after_financing

                # Leveraged
                self.df.iat[24, i] = cash_flow_after_taxes
                self.df.iat[25, i] = 0
                self.df.iat[26, i] = sum([self.df.iat[24, i], self.df.iat[25, i]])





        #Totals
        self.future_cashflow_list = self.df.loc['Total Future Cash Flow']

        self.cash_flow_after_taxes_atStart = self.df.iat[16,0]

        self.net_operating_income_atStart = self.df.iat[11,0]

        self.final_net_operating_income = self.df.iat[11, -1]

        self.total_amortization = sum(self.offsheet_df.loc['Amortization'])

        self.final_replacement_reserve = sum(self.offsheet_df.loc['Replacement Reserve'])

        self.final_depreciation = sum(self.offsheet_df.loc['Depreciation'])

        self.mortage_payoff = self.offsheet_df.iat[4,0] - self.total_amortization

        self.table = pd.concat([self.df, self.offsheet_df])

