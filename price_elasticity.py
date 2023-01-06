import pandas as pd

data = pd.DataFrame({"Demand" : [20, 30, 31, 33, 30, 33, 35],
                     "price" : [2000, 1800, 1850, 1700, 1800, 1700, 1600]})
#print(data)

data["% change in Demand"] = data["Demand"].pct_change()
data["% change in price" ] = data["price"].pct_change()

#print(data)

data["Price Elasticity"] = data["% change in Demand"]/data["% change in price" ]
print(data)
                    
                    
