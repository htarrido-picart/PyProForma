
from proforma.Results import ResultsMetricHelper, ResultsHelper
from proforma.Inputs import OtherRates as rates
import pandas as pd


class Results:
    discount_rate = rates.OtherRates.ratesDictionary['discountRate']
    cap_rate_atSale = rates.OtherRates.ratesDictionary['capRateAtSale']
    capital_gains_tax_rate = rates.OtherRates.ratesDictionary['capitalGainsTax']
    depreciation_recapture_rate =  rates.OtherRates.ratesDictionary['depreciationRecapture']
    sale_expense_rate =  rates.OtherRates.ratesDictionary['salesExpense']

    def __init__(self,
                 equity: int,
                 debt_cash_flow_list: list,
                 cash_flow_after_taxes: int,
                 total_net_operating_income: int,
                 total_development_cost: int,
                 total_replacement_reserve: int,
                 accumulated_depreciation: int,
                 mortgage_payoff: int,
                 net_operating_income: int
                 ):

        self.equity = equity
        self.debt_cash_flow_list = debt_cash_flow_list
        self.cash_flow_after_taxes = cash_flow_after_taxes
        self.total_net_operating_income = total_net_operating_income
        self.total_development_cost = total_development_cost
        self.total_replacement_reserve = total_replacement_reserve
        self.accumulated_depreciation = accumulated_depreciation
        self.mortgage_payoff = mortgage_payoff
        self.net_operating_income = net_operating_income

        depreciation_recapture_total = accumulated_depreciation * self.depreciation_recapture_rate

        #### Net Proceeds From Sale ###
        sale_price = total_net_operating_income / self.cap_rate_atSale
        sale_expenses = sale_price * self.sale_expense_rate

        net_book_value = ResultsHelper.net_book_value_calculator(development_cost=total_development_cost,
                                                              replacement_reserve=total_replacement_reserve,
                                                              total_depreciation=accumulated_depreciation)

        gain_on_sale = ResultsHelper.gain_onSale_calculator (sale_price=sale_price,
                                                          sale_expenses=sale_expenses,
                                                          net_book_value=net_book_value)

        capital_gains_tax = ResultsHelper.tax_calculator(capital_gains_tax=self.capital_gains_tax_rate,
                                                        total_depreciation=accumulated_depreciation,
                                                        depreciation_recapture_tax=depreciation_recapture_total,
                                                        gain_on_sale=gain_on_sale)

        net_proceeds_from_sale = ResultsHelper.net_proceeds_fromSale_calculator(mortgage_payoff=mortgage_payoff,
                                                                             sale_price=sale_price,
                                                                             sale_expenses= -sale_expenses,
                                                                             tax_payment= -(capital_gains_tax + abs(depreciation_recapture_total)))






        ### Return Metrics ###
        print('#' * 30)
        print('#' * 30)
        print('\n')
        # Net Present Value
        npv = ResultsMetricHelper.net_present_value_calculator(equity=equity,
                                                         debt_cash_flow_list=debt_cash_flow_list,
                                                         discount_rate=self.discount_rate)

        # Leveraged IRR after Taxes
        leverage_irr = ResultsMetricHelper.leveraged_IRR_calculator(debt_cash_flow_list=debt_cash_flow_list)

        # Capitalized Value
        capitalized_value =ResultsMetricHelper.capitalize_value_calculator(net_operating_income=net_operating_income,
                                                      cap_rate_atSale=self.cap_rate_atSale)

        # ROTA
        rota = ResultsMetricHelper.return_onTotalAssets_calculator(net_operating_income_1yr=net_operating_income,
                                                          total_development_cost=total_development_cost)

        # Return on equity
        return_on_equity = ResultsMetricHelper.return_on_equity_calculator(equity=equity,
                                                     cash_flow_after_taxes=cash_flow_after_taxes)

        resultsDictionary = {

        }

        # Create a dataFrame for this Class
        pd.set_option('display.float_format', '{:,.2f}'.format)

        rows = ['NET PROCEEDS FROM SALE',
                ''
                'Total Developemnt Cost',
                'Acc. Replacement Reserve',
                'Acc. Depreciation',
                'Net Book Value',
                '',
                'Sale Price',
                'Sale Expenses',
                'Net Book Value Deductible',
                'Gain on Sale',
                '',
                'Acc. Depreciation',
                'Depreciation Recapture Tax',
                'Capital Gain in Excess of Debt',
                'Capital Gains Tax',
                '',
                'Sale Price',
                'Sales Expenses',
                'Mortgage Payoff',
                'Tax Payment',
                'Net Proceeds from Sale',
                '',
                'RETURN METRICS',
                '',
                'Net Present Value',
                'Leveraged IRR',
                'Capitalized Value',
                'ROTA',
                'Return on equity'
                ]

        self.df = pd.DataFrame(index=rows, columns=['Values'])

        df = self.df

        # NET PROCEEDS FROM SALE payload
        df.loc['Total Developemnt Cost'] = float(total_development_cost)
        df.loc['Acc. Replacement Reserve'] = total_replacement_reserve
        df.loc['Acc. Depreciation'] = accumulated_depreciation
        df.loc['Net Book Value'] = net_book_value

        # Gain on sale payload
        df.loc['Sale Price'] = sale_price
        df.loc['Sale Expenses']= sale_expenses
        df.loc['Net Book Value Deductible'] = -net_book_value
        df.loc['Gain on Sale'] = gain_on_sale

        # Tax Payment payload
        df.loc['Depreciation Recapture Tax']= -depreciation_recapture_total
        df.loc['Capital Gain in Excess of Debt'] = gain_on_sale + accumulated_depreciation
        df.loc['Capital Gains Tax']= capital_gains_tax

        # Mortage Payoff
        df.loc['Sale Expense'] = sale_expenses
        df.loc['Mortgage Payoff']= mortgage_payoff
        df.loc['Tax Payment']= capital_gains_tax + depreciation_recapture_total
        df.loc['Net Proceeds from Sale']= net_proceeds_from_sale

        # Return Metrics dataframe

        df.loc['Net Present Value'] = npv
        df.loc['Leveraged IRR'] = leverage_irr
        df.loc['Capitalized Value'] = capitalized_value
        df.loc['ROTA'] = rota
        df.loc['Return on equity'] = return_on_equity

