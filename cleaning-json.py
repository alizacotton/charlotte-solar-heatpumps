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
    filepath= #insert filepath
    data.to_csv(filepath, index=False)


if __name__ == "__main__": 
    """file1 = #insert filepath
    file2 = #insert filepath
    file3 ..."""
    files = [file1, file2, file3, ...]
    data = combine(files)
    write(data)
    




