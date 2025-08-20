import requests
import pandas as pd
import numpy as np

class BidDataExtract:
    def init (self, csv_path):
        self.csv=csv_path
        self.data=""
def queries(self):
    self.data=pd.read_csv(self.csv)

def response(self):
    return self.data.head(5)