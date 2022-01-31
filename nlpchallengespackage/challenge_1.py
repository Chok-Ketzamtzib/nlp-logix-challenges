# -*- coding: utf-8 -*-
"""
@author: William J. Wakefield

Data Decription: https://catalog.data.gov/dataset/radnet-map-interface-for-near-real-time-radiation-monitoring-data
Data Source: https://www.epa.gov/radnet/radnet-csv-file-downloads#FL

"""
import pandas as pd

def main():

    radiationdf = pd.read_csv('FL_JACKSONVILLE_2020.csv')

    #print(radiationdf)

    print("Sorted Column Names in Alphabetical Order:\n\n", list(sorted(radiationdf.columns))) #sorted alphabetically

    print("Number of Rows: ", len(radiationdf.index))

    print(radiationdf.info())

    radiationdf['SUM OF COUNT RATE R02 AND R03 (CPM)'] = radiationdf["GAMMA COUNT RATE R02 (CPM)"] + radiationdf["GAMMA COUNT RATE R03 (CPM)"]


    print("Sum of Gamma Counte Rate R02 and R03:\n ", radiationdf['SUM OF COUNT RATE R02 AND R03 (CPM)'] )

    radiationdf.to_csv('NEW_FL_JACKSONVILLE_2020.csv', index=False)

if __name__ == "challenge-1":
    main()