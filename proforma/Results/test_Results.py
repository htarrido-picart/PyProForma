from proforma.Results import Results as myResults

debt_cash_flow_list = [-8662500,1048617,1122546,1197566,1273699,1350967,1429393,1509001,1589812,1671853, 25076715]
noDebt_cash_flow_list = [1048617,
                         1122546,
                         1197566,
                         1273699,
                         1350967,
                         1429393,
                         1509001,
                         1589812,
                         1671853,
                         25076715]


testResults = myResults.Results(equity = 8662500,
                                net_operating_income= 1995000,
                                debt_cash_flow_list= debt_cash_flow_list,
                                cash_flow_after_taxes= 1048617,
                                total_net_operating_income= 2431894,
                                total_development_cost= 24750000,
                                total_replacement_reserve= 1084022 ,
                                accumulated_depreciation= -8310023,
                                mortgage_payoff= -10571720)
