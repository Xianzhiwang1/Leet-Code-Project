import numpy as np
import pandas as pd

class FinalProject:
    def __init__(self):
        pass

    def prepare_data(self, df):
        y = df['Form']
        X = df.drop(['Form'], axis = 1)
        return df, X, y

    def split_data(self, df):
        train, validate, test = np.split(df.sample(frac=1, random_state=42), [int(.6*len(df)), int(.8*len(df))])
        return train, validate, test  


    






































