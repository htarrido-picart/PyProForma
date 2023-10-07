from proforma.Inputs import InputsAssumptions
from statistics import mean

myUnits = mean([900,1000,500])

myProformita = InputsAssumptions.MyInputsAssumptions(lot_area=11000,
                                                     existingBuildingFloorArea=0,
                                                     existingBuildingPurchase=0,
                                                     residential_FAR= 9,
                                                     commercial_FAR= 0,
                                                     manufacturing_FAR=0,
                                                     communityFAR=0,
                                                     avgUnitSize_residential=myUnits,
                                                     avgUnitSize_commercial = 0,
                                                     avgUnitSize_manufacturing = 0,
                                                     avgUnitSize_community = 0,
                                                     residential_cost= 0,
                                                     commercial_cost= 0,
                                                     manufacturing_cost= 0,
                                                     community_cost= 0,
                                                     hard_cost= 0,
                                                     soft_cost= 200,
                                                     land_cost= 0
                                                     )