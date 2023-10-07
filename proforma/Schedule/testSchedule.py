from proforma.Schedule import ScheduleDataFrame as Schedule

myScheduleGrid = Schedule.ScheduleGrid(yrs=10,
                                       start_year=2022,
                                       total_gross_income= 1021228000.00,
                                       total_vacancy= - 102061400.00,
                                       operating_expenses=  1147500.00,
                                       real_estate_taxes=  425000.00,
                                       replacement_reserve=  225000.00,
                                       debt_calc=  175837188.00 ,
                                       equity = 94681562.50,
                                       debt_calc_service=  12098478.00 ,
                                       debt_calc_service_rate= 0.068805,
                                       begin_year_balance= 175837188.00,
                                       interest_rate= 0.05,
                                       annual_public_subsidy_increase = 0.02,
                                       depreciation= -3917249.42,
                                       odinary_tax_income= 0.35
                                       )

print(myScheduleGrid.table.to_string())

