import numpy as np
import scipy.stats as ss
import matplotlib.pyplot as plt
import csv
import sys


if __name__ == "__main__":
    #sys.stdout = open('a4_OUTPUT_choi_dongjun', 'w')
    countiesAbove50 = []
    countiesBelow50 = []
    #https://www.analyticsvidhya.com/blog/2021/07/t-test-performing-hypothesis-testing-with-python/
    with open('mask-use-by-county.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            # T test where you see a low average for mask use over 50%
            # T test where you see a high average for mask use below 50%
            if(row[5] == 'ALWAYS'):
                continue
            elif(float(row[5]) < 0.5):
                countiesBelow50.append('USA-'+row[0])
            elif(float(row[5]) >= 0.5):
                countiesAbove50.append('USA-'+row[0])
    countiesAbove50AvgCases = []
    countiesBelow50AvgCases = []
    nullcounties = []
    with open('us-counties-recent.csv') as file:
        reader = csv.reader(file)
        for row in reader:
            if(row[1] == 'county'):
                continue
            elif(row[1] in countiesAbove50):
                countiesAbove50AvgCases.append(float(row[6]))
            elif(row[1] in countiesBelow50):
                countiesBelow50AvgCases.append(float(row[6]))
            else:
                nullcounties.append(row[1])
    
    
            
