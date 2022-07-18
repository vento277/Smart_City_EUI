# Sort the EUI value according to the categorized variables.
# i.e:
# built year = 1 -> corrosponding EUI | built year = 0 -> coorosponding EUI
# building height > 20 -> corrosponding EUI | building height < 20 -> corrospoding EUI
# and so on...

# In total there are... 
# Building Age:      1 or 0
# Orientation:       1 or 2 or 3 or 4

# Name                             Mean               | Median
# Building Height:   over or under 17.747142857142155 | 16.4
# V/FA Ratio:        over or under 37.487618285714866 | 41.633328
# V/SA Ratio:        over or under 72.66836562999836  | 74.68855941
# FA/SA Ratio:       over or under 2.0034229748571764 | 1.793960824

# Header
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
 
class sort():
    def __init__(self, file, dep, indep, atype):
        self.file = file
        self.dep = dep
        self.indep = indep
        self.atype = atype

    def config(self):
        # Read file
        data = pd.read_csv(self.file, encoding = 'unicode_escape')

        # Dependant Var
        depp = pd.DataFrame(data, columns = [self.dep])[self.dep]

        # Independant Var
        indep = pd.DataFrame(data, columns = [self.indep])[self.indep]

        # Cutoff, use mean & median as benchmark
        if (self.atype == 'cutoff'):
                
                # Mean
                # mean computation
                total = 0
                length = len(indep)
                for i in range (length):
                    total += depp[i]
                mean = total/length

                # Median
                # median computation
                median = int(length / 2)
           
                # sorting, if lower than the cutoff val, store in 'l', else store in 'h'
                c_val = mean
                c_val2 = depp[median]

                # check value
                print(c_val2)

                l = []
                h = []
                for i in range (length):
                    if (depp[i]) < c_val2: # c_val <-> c_val2
                        l.append(indep[i])
                    else:
                        h.append(indep[i])


                # store as csv
                # df = pd.DataFrame(l)
                # df.to_csv('Building_Height_m_median_lower.csv')
                # df = pd.DataFrame(h)
                # df.to_csv('Building_Height_m_median_higher.csv')

        # Or, categorize the output via input
        # 
        if (self.atype == 'or'):

            arr = []
            dat = []
            length = len(indep)
            no_of_or = int(input("Please enter the number of categories: "))

            for i in range(no_of_or):
                user = int(input("Please enter the number: "))
                arr.append(user)

            for j in range(len(arr)):
                for k in range(length):
                    if (depp[k] == j):
                        dat.append(indep[k])
                    
                    dat.append("------")    
            
            # # store as csv
            # df = pd.DataFrame(dat)
            # df.to_csv('Building_Age_.csv')

    def or_s():

        data = pd.read_csv("test.csv", encoding = 'unicode_escape')
        dep = pd.DataFrame(data, columns = ['Orientation'])['Orientation']
        indep = pd.DataFrame(data, columns = ['EUI'])['EUI']

        length = len(indep)
        dat0 = []
        dat1 = []
        dat2 = []
        dat3 = []
        for i in range (length):
            if dep[i] == 4:
                dat3.append(indep[i])
            if dep[i] == 3:
                dat2.append(indep[i])
            if dep[i] == 2:
                dat1.append(indep[i])
            if dep[i] == 1:
                dat0.append(indep[i])

        df = pd.DataFrame(dat0)
        df2= pd.DataFrame(dat1)
        df3= pd.DataFrame(dat2)
        df4= pd.DataFrame(dat3)
        df.to_csv('Ori_1.csv')
        df2.to_csv('Ori_2.csv')
        df3.to_csv('Ori_3.csv')
        df4.to_csv('Ori_4.csv')



# Call
# a = sort('test.csv', 'Building_Height_m', 'EUI', 'cutoff').config()
# a = sort('test.csv', 'Built_Year', 'EUI', 'or').config()
# or_s()
