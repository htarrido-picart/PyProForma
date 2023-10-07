from proforma.Inputs  import CapitalStructureHelper as CSHelper

class CapitalStructure:

    def __init__(self,
                 total_development_cost: int,
                 equity_percent:  float,
                 debt_service_percent: float):

        self.total_development_cost = total_development_cost
        self.equity_percent = equity_percent
        self.debt_service_percent = debt_service_percent

        self.debt_percent = 1.0 - equity_percent

        self.equity = CSHelper.equity(my_totaldev_cost= total_development_cost,
                                                equity_percent= self.equity_percent)

        self.debt = CSHelper.debt_calc(my_totaldev_cost= total_development_cost,
                                            debt_percent= self.debt_percent)

        self.debt_service = CSHelper.debt_calcService(my_total_debt= self.debt,
                                                          debt_service_percent= self.debt_service_percent)
