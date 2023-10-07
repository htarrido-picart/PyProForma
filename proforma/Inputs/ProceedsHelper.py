def common_area_and_circulation (total_floor_area, net_loss_factor):
    return total_floor_area * net_loss_factor

def net_area (total_floor_area, common_area_and_circulation):
    return total_floor_area - common_area_and_circulation

def approximate_units (net_area, avg_market_rate_unit_size):
    if avg_market_rate_unit_size:
        return net_area / avg_market_rate_unit_size

def total_income (approx_units, rent_per_unit):
    if approx_units:
        return approx_units * rent_per_unit * 12
    else:
        return 0

def total_vacancy (vacancy_rate, total_income):
    return vacancy_rate * total_income

def operational_expenses (operational_expenses, net_area):
    return operational_expenses * net_area

def real_estate_taxes (real_estate_taxes, net_area):
    return real_estate_taxes * net_area

def replacement_reserve (total_floor_area, replacement_reserve):
    return total_floor_area * replacement_reserve

def total_cost (net_area, dev_cost):
    return (net_area * dev_cost)

def depreciation (use_sqft_total_cost, depreciation):
    if depreciation:
        return (-1 * (use_sqft_total_cost/ depreciation))