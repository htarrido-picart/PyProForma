'''
Scheduling cash flow functions for proforma
functions used in Scheduling Class

credit: htarrido, SSA, CCNY, CUNY
source: Poorvu, William J., and Samuel Plimpton. "Financial analysis of real property investments."
        Harvard Business School (2003).

'''

import pprint as pp
import json

############################################
# Pro Forma ProForma - Soup Market Rate
############################################

def printMyDictionary(k,v, myDictionary):
    for k,v in myDictionary:
        print(k,v)

# Income and Expenses
def income(potential_gross_income, vacancy):
    '''
    Income as the sum of potential gross income and vacancy (usually it is negative)
    '''

    effective_gross_income = {'potential_gross_income': potential_gross_income,
                              'vacancy': -vacancy}

    print("### Income ###")

    pp.pprint(effective_gross_income)
    
    print(json.dumps(effective_gross_income, indent = 4))

    output = sum(effective_gross_income.values())

    print("Income", output)

    return output


def expenses(operating_expenses, real_estate_taxes, replacement_reserve):
    '''
    Expensesas the sum of operating an asset, real estate taxes and replacement reserves

    '''
    total_expenses = {'operating_expenses': operating_expenses,
                      'real_estate_taxes':real_estate_taxes,
                      'replacement_reserve':replacement_reserve}

    print("### Expense ###")

    for k, v in total_expenses.items():
        print(k, v)

    output = sum(total_expenses.values())

    print("Expenses", output)

    return output


def endYear_net_operating_income(effective_gross_income, endYear_total_expenses):
    return effective_gross_income +  endYear_total_expenses


def net_operating_income(incomeTotal, expense_total):
    '''
    Calculation of the tax effect for a real estate investment involves simply a
    multiplication of the stream of taxable income by the appropriate tax rates of the investor concerned.
    Starting  in  2003,  the  maximum  marginal  tax  rate  is  assumed  to  be  35%  for  ordinary  income  (the
    capital  gains  rate  is  15%).    On  this  basis,  every  dollar  of  losses  will  reduce  taxes  paid  by  35%.    This
    tax  savings  can  then  be  added  back  to  increase  the  total  return,  assuming  that  the  investor  has
    “passive” income to match against the “passive” loss.
    '''

    netOperatingIncome = {'incomeTotal': incomeTotal,
                          'expense_total':expense_total
                          }

    print(json.dumps(netOperatingIncome, indent = 4))

    output = sum(netOperatingIncome.values())

    print("Net Operating Income", output)

    return output


# Cash flow and Tax Payments

def annual_debt_calc_service(debt_calc, debt_calc_service):
    '''
    Annual debt_calc service is the amount paid of the debt_calc multiplied by the debt_calc service
    '''

    debServiceValues = {'debt_calc': debt_calc,
                        'debt_calc_service':debt_calc_service}

    output = -(debt_calc * debt_calc_service)

    print(json.dumps(debServiceValues, indent = 4))

    print("Annual debt_calc Service", output)

    return output


def cash_flow_after_taxes(operating_income, annual_dbs, tax_payment):
    '''
    The  calculation  of  CFAT  is  completed  by  deducting  the  taxes  paid  or
    adding  the  tax  benefit  received  to  the  before-tax  cash  flow.    This  is  equivalent  to  applying  the  tax
    effect  to  the  operating  cash  flow  reduced  by  financial  payments.    For  many  investors,  CFAT  is  the
    appropriate  annual  cash  flow  for  the  evaluation  of  an  equity  investment.

    Cash  flow  after  financing  return  on  equity  or  cash  on  cash  return This  measure  of
    return may be stated thus:
        Cash flow after financing / equity

    Before-tax  cash  flow  +  first  year’s  amortization  return  on  equity This measure is
    defined in the following way:
        Before-tax cash flow + Mortgage principal payment (year 1) / equity
    '''

    cash_flow_after_financing = operating_income + annual_dbs
    caFT = cash_flow_after_financing + (-1 * tax_payment)  #cash flow after taxes

    cashFlowDictionary = {'operating_income': operating_income,
              'annual_dbs': annual_dbs,
              'tax_payment': tax_payment,
              'Cash Flow After Finance': cash_flow_after_financing,
              'Cash Flow After Taxes': caFT
              }

    print(json.dumps(cashFlowDictionary, indent=1))

    return caFT

############################################
# Return Measures
############################################
def net_sale_price(total_development_cost, total_replacement_reserves):
    return total_development_cost +  total_replacement_reserves

def total_sales(sale_price, saleExpense):
    '''
    Total sales per year as the sum of sales price and sale expenses
    '''
    
    totalSales = sale_price + saleExpense

    salesDictionary = { 'sale_price': sale_price,
                        'saleExpense':  saleExpense,
                        'totalSales': totalSales
                        }

    print(json.dumps(salesDictionary))

    return totalSales

def unleveraged_irr(cashFlowAfterFinancing,
                    tax_payments,
                    net_proceeds_fromSale,
                    yearBeforeSale ):

    beforeTaxSalesProceeds = tax_payments + net_proceeds_fromSale

    if yearBeforeSale:
        unleveragedIRR= { 'Cash Flow After Financing': cashFlowAfterFinancing,
                        'Before Tax Sales Proceeds': beforeTaxSalesProceeds
                          }
    else:
        unleveragedIRR = {'Cash Flow After Financing': cashFlowAfterFinancing,
                          'Before Tax Sales Proceeds': cashFlowAfterFinancing
                          }

    return sum(unleveragedIRR.values())

def leveraged_before_taxIRR(total_cashFlow_afterTaxes, net_proceeds_fromSale):

    futureCashFlow = { 'Total Cash Flow After Taxes': total_cashFlow_afterTaxes,
                       'Net Proceeds From Sale': net_proceeds_fromSale
                       }

    output = sum(futureCashFlow.values())

    print(json.dumps(futureCashFlow))

    print(" Total Future Cash Flow", output)

    return output

############################################
# Offsheet Calculation
############################################
def debt_calc_service_components(begin_year_balance, debt_calcService, interest_rate, ammortization):
    print("### debt_calc Service Components ###")

    endYearBalance = begin_year_balance - debt_calcService
    interest = begin_year_balance - interest_rate
    amortization = debt_calcService - interest

    debt_calcComponents = {'begin_year_balance': begin_year_balance,
                  'endYearBalance': endYearBalance,
                  'interest': interest,
                  'ammortization': ammortization
                      }

    print(json.dumps(debt_calcComponents))

    return amortization


def tax_paymentScheduler(cashFlowAfterFinancing,
                         amortization,
                         replacement_reserve,
                         depreciation,
                         ordinaryTaxIncome):

    taxableIncome = cashFlowAfterFinancing + amortization + -replacement_reserve + -depreciation
    tax_payment = taxableIncome * ordinaryTaxIncome

    print("### Tax Payment ###")

    tax_paymentLineItems = {'cashFlowAfterFinancing': cashFlowAfterFinancing,
                           'amortization': amortization,
                           'replacement_reserve': replacement_reserve,
                           'depreciation': depreciation,
                           'ordinaryTaxIncome': ordinaryTaxIncome,
                           'taxableIncome': taxableIncome,
                           'tax_payment': tax_payment
                           }

    print(json.dumps(tax_paymentLineItems))

    return taxableIncome, tax_payment


def total_amortization(amortizationValues):
    '''
    Amortization is an accounting technique used to periodically lower the book value of a loan or an intangible asset over a set period of time.
    Concerning a loan, amortization focuses on spreading out loan payments over time.
    '''

    return sum(amortizationValues)

