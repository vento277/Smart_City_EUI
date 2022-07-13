import pandas as pd

# Daily Value Extraction

def cent_water_vol_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
  df = pd.DataFrame(data, columns = ['Chem Centre'])
  s = df["Chem Centre"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'm³'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

def east_water_vol_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
  df = pd.DataFrame(data, columns = ['Chem East'])
  s = df["Chem East"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'm³'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

def north_water_vol_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
  df = pd.DataFrame(data, columns = ['Chem North'])
  s = df["Chem North"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'm³'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

def south_water_vol_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
  df = pd.DataFrame(data, columns = ['Chem South'])
  s = df["Chem South"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'm³'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

def phys_water_vol_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
  df = pd.DataFrame(data, columns = ['Chem Phys'])
  s = df["Chem Phys"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'm³'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

############################

#  Weekly Average Caculations

# def cent_water_vol():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
#   df = pd.DataFrame(data, columns = ['Chem Centre'])
#   s = df["Chem Centre"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#       a = s[i].translate({ord(i):None for i in 'm³'}) # 
#       sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for Chem Centre is: %lf" %(j+1, avg))

# def phys_water_vol():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
#   df = pd.DataFrame(data, columns = ['Chem Phys'])
#   s = df["Chem Phys"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#       a = s[i].translate({ord(i):None for i in 'm³'}) # 
#       sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for Chem Phys is: %lf" %(j+1, avg))

# def east_water_vol():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
#   df = pd.DataFrame(data, columns = ['Chem East'])
#   s = df["Chem East"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#       a = s[i].translate({ord(i):None for i in 'm³'}) # 
#       sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for Chem East is: %lf" %(j+1, avg))

# def north_water_vol():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
#   df = pd.DataFrame(data, columns = ['Chem North'])
#   s = df["Chem North"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#       if s[i] == '':
#         i = i + 1
#       else:
#         a = s[i].translate({ord(i):None for i in 'm³'}) #
#         sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for Chem North is: %lf" %(j+1, avg))

# def south_water_vol():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/Water_Volume_2021.csv')
#   df = pd.DataFrame(data, columns = ['Chem South'])
#   s = df["Chem South"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#       a = s[i].translate({ord(i):None for i in 'm³'}) # 
#       sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for Chem South is: %lf" %(j+1, avg))