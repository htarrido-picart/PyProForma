import numpy_financial as npf

#############################
# Return Metrics
#############################

# Net Present Value
def net_present_value_calculator(equity, debt_cash_flow_list,discount_rate):
    net_present_value = npf.npv(discount_rate, debt_cash_flow_list)
    return round(net_present_value,2)

# Leveraged after Internar Rate of Return
def leveraged_IRR_calculator(debt_cash_flow_list):
    leveraged_IRR = npf.irr(debt_cash_flow_list) * 100
    return round(leveraged_IRR,2)

# Capitalized Value
def capitalize_value_calculator(net_operating_income, cap_rate_atSale):
    capitalize_value = net_operating_income/ cap_rate_atSale
    return round(capitalize_value, 2)

# ROTA- Return on Total Assets
def return_onTotalAssets_calculator(net_operating_income_1yr, total_development_cost):
    return_onTotal_assets = (net_operating_income_1yr / total_development_cost) * 100
    return round(return_onTotal_assets, 2)

# Return on equity
def return_on_equity_calculator (equity, cash_flow_after_taxes):
    return_onEquity = (cash_flow_after_taxes / equity) * 100
    return round(return_onEquity, 2)
