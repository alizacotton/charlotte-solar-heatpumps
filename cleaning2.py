import pandas as pd

data = pd.read_csv("C:/Users/aliza/OneDrive/charlotte-project/full-data.csv")

data = data.rename(columns={"address.streetAddress": "streetAddress" , "address.city": "City", 
                     "address.zipcode": "Zipcode", "resoFacts.yearBuilt": "yearBuilt", "resoFacts.livingArea": "squareFootage", 
                     "resoFacts.cooling": "coolingMethod", "resoFacts.heating": "heatingMethod"})

data["homeAge"] = 2025 - data["yearBuilt"] 

data["coolingMethod"] = data["coolingMethod"].str.replace('[', '')
data["coolingMethod"] = data["coolingMethod"].str.replace(']', '')

data["heatingMethod"] = data["heatingMethod"].str.replace('[', '')
data["heatingMethod"] = data["heatingMethod"].str.replace(']', '')

data["squareFootage"] = data["squareFootage"].str.replace(" sqft", '')

print(data.head)

filepath= 'C:/Users/aliza/OneDrive/charlotte-project/final.csv'
data.to_csv(filepath, index=False)
