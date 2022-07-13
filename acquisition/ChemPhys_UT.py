import pandas as pd

# Daily Value Extraction

def Phys_elec_power_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemPhys_Build_UT.csv')
  df = pd.DataFrame(data, columns = ['Chem Phys Elec Main Meter Power'])
  s = df["Chem Phys Elec Main Meter Power"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'kW'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

def Phys_hw_power_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemPhys_Build_UT.csv')
  df = pd.DataFrame(data, columns = ['Chem Phys HW Main Meter Power'])
  s = df["Chem Phys HW Main Meter Power"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'kW'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

############################

# Weekly Average Caculations

# def phys_elec_power():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemPhys_Build_UT.csv')
#   df = pd.DataFrame(data, columns = ['Chem Phys Elec Main Meter Power'])
#   s = df["Chem Phys Elec Main Meter Power"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#       a = s[i].translate({ord(i):None for i in 'kW'}) # 
#       sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for elec power is: %lf" %(j+1, avg))

# def phys_elec_energy():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemPhys_Build_UT.csv')
#   df = pd.DataFrame(data, columns = ['Chem Phys Elec Main Meter Energy'])
#   s = df["Chem Phys Elec Main Meter Energy"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#       a = s[i].translate({ord(i):None for i in 'kWh'}) # 
#       sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for elec energy is: %lf" %(j+1, avg))
    
# def phys_HW_power():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemPhys_Build_UT.csv')
#   df = pd.DataFrame(data, columns = ['Chem Phys HW Main Meter Power'])
#   s = df["Chem Phys HW Main Meter Power"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#         a = s[i].translate({ord(i):None for i in 'kW'}) # 
#         sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for HW power is: %lf" %(j+1, avg))
    
# def phys_HW_energy():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemPhys_Build_UT.csv')
#   df = pd.DataFrame(data, columns = ['Chem Phys HW Main Meter Energy'])
#   s = df["Chem Phys HW Main Meter Energy"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#         a = s[i].translate({ord(i):None for i in 'kWh'}) # 
#         sum += float(a)


#     avg = sum / 7
#     count += 7

#     print("The week %d average for HW energy is: %lf" %(j+1, avg))

# def phys_water():
#   data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemPhys_Build_UT.csv')
#   df = pd.DataFrame(data, columns = ['Chem Phys Water Main Meter Consumption'])
#   s = df["Chem Phys Water Main Meter Consumption"] # Set s to only be temp column.

#   # Initialize variables.
#   sum = 0
#   count = 0

#   for j in range(52):
#     avg = 0
#     sum = 0
#     for i in range(count, count+7):
#       a = s[i].translate({ord(i):None for i in '³m'}) # 
#       sum += float(a)

#     avg = sum / 7
#     count += 7

#     print("The week %d average for water is: %lf" %(j+1, avg))