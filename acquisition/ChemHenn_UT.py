import pandas as pd

# Daily Value Extraction

def Henn_elec_power_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemHennings_Build_UT.csv')
  df = pd.DataFrame(data, columns = ['Electrical Power'])
  s = df["Electrical Power"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'kW'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

def Henn_hw_power_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemHennings_Build_UT.csv')
  df = pd.DataFrame(data, columns = ['Hot Water Power'])
  s = df["Hot Water Power"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'kW'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)

def Henn_water_vol_day():
  data = pd.read_csv(r'Components/Data/UBC/ChemBuilds/ChemHennings_Build_UT.csv')
  df = pd.DataFrame(data, columns = ['Water Consumption Volume'])
  s = df["Water Consumption Volume"] # Set s to only be temp column.

  for i in range(365):
    a = s[i].translate({ord(i):None for i in 'm��m³'}) # 
    a= float(a)
    
    #print("The day %d value for elec power is: %lf" %(i+1, a))
    print(a)