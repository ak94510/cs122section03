# ----------------------------------------------------------------------
# Name:        hw10
# Purpose:     Pandas data frame query practices

# Date:       5/1/2019
# ----------------------------------------------------------------------
"""
Pandas Data Frame Query Practices

Using Pandas to answer the following questions about
Fuel Economy Data from the EPA website.
1. How many cars are made by the manufacturer Honda?
2. How many 'Guzzlers' are there (as indicated by the column 'Guzzler?')
3. What is the value of the highest combined Fuel Efficiency as given
    by "Comb FE (Guide) - Conventional Fuel"?
4. Which division and car line has the lowest combined FE -
    Conventional Fuel?
5. What is the highest combined FE - Conventional Fuel among
    all wheel drives?
6. Which car line has the largest difference between Highway and City
    Fuel efficiency - Conventional Fuel?
7. What is the average annual fuel cost (Annual Fuel1 Cost -
    Conventional Fuel) of supercharged cars?
8. What SUV has the lowest annual fuel cost?
9. Which manufacturer has the most cars with manual transmission?
10. What is the average annual fuel cost by car division?
11. What criteria would you use to buy a car?
"""
import pandas as pd
import numpy as np
import re

def q1(df):
    """
    How many cars are made by the manufacturer Honda?
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (integer) number of cars made by Honda
    """
    return len(df[df['Mfr Name'] == 'Honda'])

def q2(df):
    """
    How many 'Guzzlers' are there (as indicated by the column Guzzler?)
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (integer) nbumber of Guzzlers
    """
    return len(df[df['Guzzler?'] == 'G'])

def q3(df):
    """
    What is the value of the highest combined Fuel Efficiency as given
    by "Comb FE (Guide) - Conventional Fuel"?
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (float) - value of the highest combined Fuel Efficiency
    """
    return df.loc[df['Comb FE (Guide) - Conventional Fuel'].idxmax(),
                  'Comb FE (Guide) - Conventional Fuel']

def q4(df):
    """
    Which division and car line has the lowest combined FE -
    Conventional Fuel?
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (tuble of strings) division and car line
    """
    min_idx = df['Comb FE (Guide) - Conventional Fuel'].idxmin()
    return df.loc[min_idx, 'Division'], df.loc[min_idx, 'Carline']

def q5(df):
    """
    What is the highest combined FE - Conventional Fuel among
    all wheel drives? Use 'Drive Desc'.
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (float) the highest combined FE
    """
    wheel_drivers = df[df['Drive Desc'] == 'All Wheel Drive']
    highest = wheel_drivers['Comb FE (Guide) - Conventional Fuel'].idxmax()
    return wheel_drivers.loc[highest
                            , 'Comb FE (Guide) - Conventional Fuel']

def q6(df):
    """
    Which car line has the largest difference between Highway and City
    Fuel efficiency - Conventional Fuel?
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (string) car line with largest difference
    """
    carline = df.groupby('Carline').sum()
    diff = carline['City FE (Guide) - Conventional Fuel'] - \
           carline['Hwy FE (Guide) - Conventional Fuel']
    return diff.abs().idxmax()

def q7(df):
    """
    What is the average annual fuel cost (Annual Fuel1 Cost -
    Conventional Fuel) of supercharged cars?
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (float) the average annual fuel cost
    """
    supercharged = df[df['Air Aspiration Method Desc'] == 'Supercharged']
    return supercharged['Annual Fuel1 Cost - Conventional Fuel'].mean()

def q8(df):
    """
    What SUV has the lowest annual fuel cost?
    (Use "Carline Class Desc" to identify SUVs.)
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (string) SUV with the lowest annual fuel cost
    """
    suvs = df[df['Carline Class Desc'].str.contains('SUV', na=False)]
    return suvs.loc[suvs['Annual Fuel1 Cost - Conventional Fuel']
                    .idxmin(), 'Carline']

def q9(df):
    """
    Which manufacturer has the most cars with manual transmission?
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (string) manufacturer with the most cars with manual
             transmission.
    """
    manual_cars = df.loc[df["Trans"] == 'M']
    return manual_cars.groupby('Mfr Name').count()['Model Year'].idxmax()

def q10(df):
    """
    What is the average annual fuel cost by car division?
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (Pandas series) average annual fuel cost by car division
    """
    divisions = df.groupby('Division').mean()
    return divisions['Annual Fuel1 Cost - Conventional Fuel']


def q11(df):
    """
    What criteria would you use to buy a car?
    (returns your perfect car based on your criteria)
    :param df: Pandas DataFrame representing data in '2019 FE Guid.csv'
    :return: (string) the perfect carline for you
    """
    return df.loc[(df['Mfr Name'] == 'Mercedes-Benz') &
                  (df['Carline Class Desc'] == 'Standard SUV 4WD') &
                  (df['Trans'].str.contains('A')) &
                  (df['Eng Displ'] == 4.7), 'Carline'].unique()


def main():
    # Read the csv file and use colum 0 (Park Name) as our index
    df_cars = pd.read_csv('hw10/2019 FE Guide.csv')
    #print(df_cars)

    # Question 1
    print(f'Q1: {q1(df_cars)}.')

    # Question 2
    print(f'Q2: {q2(df_cars)}.')

    # Question 3
    print(f'Q3: {q3(df_cars)}.')

    # Question 4
    print(f'Q4: {q4(df_cars)}.')

    # Question 5
    print(f'Q5: {q5(df_cars)}.')

    # Question 6
    print(f'Q6: {q6(df_cars)}.')

    # Question 7
    print(f'Q7: {q7(df_cars)}.')

    # Question 8
    print(f'Q8: {q8(df_cars)}.')

    # Question 9
    print(f'Q9: {q9(df_cars)}.')

    # Question 10
    print(f'Q10:\n{q10(df_cars)}.')

    # Question 11
    print(f'Q11: {q11(df_cars)}.')

if __name__ == "__main__":
    main()
