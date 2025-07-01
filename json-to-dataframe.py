import pandas as pd
import json



def combine(files):
    frames = process(files)
    result = pd.concat(frames)
    return result


def process(files):
    frames = []
    for file in files:
        with open(file) as train_file:
            dict_train = json.load(train_file)

        data = pd.json_normalize(dict_train)
        df = data[['address.streetAddress', 'address.city', 'address.zipcode', 'resoFacts.yearBuilt', 'resoFacts.livingArea', 'resoFacts.cooling', 'resoFacts.heating']]
        frames.append(df)
    return frames

def clean(data):
    data = data.rename(columns={"address.streetAddress": "streetAddress" , "address.city": "City", 
                     "address.zipcode": "Zipcode", "resoFacts.yearBuilt": "yearBuilt", "resoFacts.livingArea": "squareFootage", 
                     "resoFacts.cooling": "coolingMethod", "resoFacts.heating": "heatingMethod"})

    data["homeAge"] = 2025 - data["yearBuilt"] 

    data["coolingMethod"] = data["coolingMethod"].str.replace('[', '')
    data["coolingMethod"] = data["coolingMethod"].str.replace(']', '')

    data["heatingMethod"] = data["heatingMethod"].str.replace('[', '')
    data["heatingMethod"] = data["heatingMethod"].str.replace(']', '')

    data["squareFootage"] = data["squareFootage"].str.replace(" sqft", '')


def write(data):
    filepath= #insert filepath
    data.to_csv(filepath, index=False)


if __name__ == "__main__": 
    """file1 = #insert filepath
    file2 = #insert filepath
    file3 ..."""
    files = [file1, file2, file3, ...]
    data = combine(files)
    write(data)
    




