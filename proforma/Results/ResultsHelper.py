

# Net Book Value
def net_book_value_calculator(development_cost, replacement_reserve, total_depreciation):
    """net_book_value is calculated as the original cost of an asset,
    minus any accumulated depreciation, accumulated depletion,
    accumulated amortization, and accumulated impairment"""

    net_book_value = development_cost + replacement_reserve + total_depreciation
    return round(net_book_value, 2)

# Gain On Sale
def gain_onSale_calculator (sale_price, sale_expenses,net_book_value):
    """Gain on Sale is the amount of money that is made when selling a property
    for more than its original value"""
    gain_onSale= sale_price - sale_expenses - net_book_value
    return round(gain_onSale, 2)

# Tax Payment
def tax_calculator(total_depreciation,
                   depreciation_recapture_tax,
                   gain_on_sale,
                   capital_gains_tax):
    """Capital Gains Tax is a federal fee paid on the profit made from selling a property"""
    cap_gainExcessOfDebt_calc = total_depreciation + gain_on_sale
    cap_gain_tax= cap_gainExcessOfDebt_calc * capital_gains_tax
    return round(cap_gain_tax, 2)


##################################################################################################
# Net Proceeds from Sale
def net_proceeds_fromSale_calculator(mortgage_payoff, sale_price, sale_expenses, tax_payment):
    """Net Proceeds from Sale is the amount received by the seller after deducting
    all costs and expenses from the gross proceeds"""
    net_proceeds_fromSale = sum([sale_price,sale_expenses, mortgage_payoff, tax_payment])
    return round(net_proceeds_fromSale, 2)




