import pandas as pd
from app import App

df = pd.read_csv("../african_crises.csv", sep=",")

application = App(df)
application.reduce_dimensionality(['case', 'year'])
application.perform_algorithm("inflation_annual_cpi","exch_usd")

