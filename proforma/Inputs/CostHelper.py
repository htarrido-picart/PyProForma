# Helpers to calculate development cost summaries

def use_cost_calculator(type, gross_sqft, cost_per_sqft):
    total_cost_per_sqft = gross_sqft * cost_per_sqft
    print("---")
    print("{type} Cost per SqFt: ${amount:,}".format(type = type, amount=cost_per_sqft))
    print("Total {type} Area Cost: ${amount:,}".format(type = type, amount=total_cost_per_sqft))
    return total_cost_per_sqft


def hard_cost(gross_sqft, hard_cost):
    total_hard_cost = gross_sqft * hard_cost
    print("---")
    print("Hard Costs per SqFf: ${:,}".format(hard_cost))
    print("Total Hard Costs: ${:,}".format(total_hard_cost))
    return total_hard_cost

def soft_cost(gross_sqft, soft_cost):
    total_soft_cost = gross_sqft * soft_cost
    print("---")
    print("Soft Costs per SqFf: ${:,}".format(soft_cost))
    print("Total Soft Costs: ${:,}".format(total_soft_cost))
    return total_soft_cost

def total_development_cost(existing_building_purchase,
                           total_lot_purchase_cost,
                           total_landscape_cost,
                           total_residential_cost,
                           total_commercial_cost,
                           total_manufacturing_cost,
                           total_community_cost,
                           total_hard_cost,
                           total_soft_cost):

    totaldev_cost = [existing_building_purchase,
                     total_lot_purchase_cost,
                     total_landscape_cost,
                     total_residential_cost,
                     total_commercial_cost,
                     total_manufacturing_cost,
                     total_community_cost,
                     total_hard_cost,
                     total_soft_cost]

    sum_dev_cost = sum(totaldev_cost)
    print("---")
    print("Total Development Costs: ${:,}".format(sum_dev_cost))
    return sum_dev_cost