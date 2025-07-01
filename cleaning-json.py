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


def write(data):
    filepath= 'C:/Users/aliza/OneDrive/charlotte-project/full-data.csv'
    data.to_csv(filepath, index=False)


if __name__ == "__main__": 
    file1 = 'C:/Users/aliza/OneDrive/charlotte-project/batch1.json'
    file2 = 'C:/Users/aliza/OneDrive/charlotte-project/batch2.json'
    file3 = 'C:/Users/aliza/OneDrive/charlotte-project/batch3.json'
    file4 = 'C:/Users/aliza/OneDrive/charlotte-project/batch4.json'
    file5 = 'C:/Users/aliza/OneDrive/charlotte-project/batch5.json'
    files = [file1, file2, file3, file4, file5]
    data = combine(files)
    write(data)
    




