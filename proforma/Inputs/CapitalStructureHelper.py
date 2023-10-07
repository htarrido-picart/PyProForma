# Helper methods to calculate capital structure

def equity(my_totaldev_cost, equity_percent):
    totalEq = my_totaldev_cost * equity_percent
    output = totalEq, equity_percent
    return totalEq

def debt_calc(my_totaldev_cost, debt_percent):
    totaldebt_calc = my_totaldev_cost* debt_percent
    output = totaldebt_calc, debt_percent
    return totaldebt_calc

def debt_calcService(my_total_debt, debt_service_percent):
    total_debt_service = my_total_debt * debt_service_percent
    output = total_debt_service, debt_service_percent
    return total_debt_service