# This file returns the average of temp and humid for the given UBC data. 
# Read carefully the comment and understand them so we can use them as needed.
# The data consists of 97 timestamps per day. 
# The function averages thoes 97 data to get the per-day data. 
# Now you 7 of thoes data to get per-week data.
#
# The function is set to print out the data. This will be done for Temperature and Humidity.import
# ex. Week 1 7.10
#     Week 2 8.98...
#
# Condition will be a separate parameter. 
# Thus, this file will consist of 3 paparmeters: Temp, Humid and Cond. 
#------------------------------
import pandas as pd
import numpy as np

# Check if the data is correctly read as a whole. 
def check():
  df = pd.read_csv(r'Components/Data/WeatherData_UBC/2021UBC_RH_TEMP_Q1.csv')
  print(df)

# The average per day, per week can be checked by printing the values at the right place.
# There is only data up to April which is about 14 weeks, thus, the 14 in the k range.
def UBC_temp_total_day():

  # Read the file
  data = pd.read_csv(r'Components/Data/WeatherData_UBC/2021UBC_RH_TEMP.csv')
  df = pd.DataFrame(data, columns = ['UBC Temp']) # Set to be only Temp column
  df.fillna('', inplace=True) # Replace empty string as NULL.
  s = df["UBC Temp"] # Set s to only be temp column.

  # Initialize variables.
  sum = 0
  avg_sum = 0
  avg = 0
  week_avg = 0
  time_per_day = 97
  count = 1

  # day(j) loop
  for j in range (365):   
    avg = 0
    sum = 0

    # timestamp(i) loop
    for i in range(count, time_per_day):  
      if s[i] == "":  
        i = i + 1
      else:
        a = s[i].translate({ord(i):None for i in '°C�'}) #  Replace °C with NULL.
        sum += float(a) # Convert the string to float and sum the data.

    # Calculation
    avg = sum / (97-2) # two datime cells
    count = count + 97
    time_per_day = count + 97 

  
    #print("The day %d average is: %lf" %(j+1, avg)) 
    print(avg)

def UBC_temp_total_week():

  # Read the file
  data = pd.read_csv(r'Components/Data/WeatherData_UBC/2021UBC_RH_TEMP.csv')
  df = pd.DataFrame(data, columns = ['UBC Temp']) # Set to be only Temp column
  df.fillna('', inplace=True) # Replace empty string as NULL.
  s = df["UBC Temp"] # Set s to only be temp column.

  # Initialize variables.
  sum = 0
  avg_sum = 0
  avg = 0
  week_avg = 0
  time_per_day = 97
  count = 1

  # week(k) loop
  for k in range (52):
    avg_sum = 0 

    # day(j) loop
    for j in range (7):   
      avg = 0
      sum = 0

      # timestamp(i) loop
      for i in range(count, time_per_day):  
        if s[i] == "":  
          i = i + 1
        else:
          a = s[i].translate({ord(i):None for i in '°C�'}) #  Replace °C with NULL.
          sum += float(a) # Convert the string to float and sum the data.

      # Calculation
      avg = sum / (97-2) # two datime cells
      avg_sum += avg
      count = count + 97
      time_per_day = count + 97 

    week_avg = avg_sum / 7
    
    print("The week %d average is: %lf" %(k+1, week_avg)) 

def UBC_humid_total_day():

  # Read the file
  data = pd.read_csv(r'Components/Data/WeatherData_UBC/2021UBC_RH_TEMP.csv')
  df = pd.DataFrame(data, columns = ['UBC Humidity']) # Set to be only Temp column
  df.fillna('', inplace=True) # Replace empty string as NULL.
  s = df["UBC Humidity"] # Set s to only be temp column.

  # Initialize variables.
  sum = 0
  avg_sum = 0
  avg = 0
  week_avg = 0
  time_per_day = 97
  count = 1

  # day(j) loop
  for j in range (365):   
    avg = 0
    sum = 0

    # timestamp(i) loop
    for i in range(count, time_per_day):  
      if s[i] == "":  
        i = i + 1
      else:
        a = s[i].translate({ord(i):None for i in '°%RHg'}) #  Replace °C with NULL.
        sum += float(a) # Convert the string to float and sum the data.

    # Calculation
    avg = sum / (97-2) # two datime cells
    count = count + 97
    time_per_day = count + 97 

  
    #print("The day %d average is: %lf" %(j+1, avg)) 
    print(avg)

def HDD_day():
  data = pd.read_csv(r'Components/Data/WeatherData_UBC/UBC_HDD_CDD_Days.csv')
  df = pd.DataFrame(data, columns = ['UBC Heating Degree Days'])
  s = df["UBC Heating Degree Days"] # Set s to only be temp column.

  # Initialize variables.
  count = 0

  for i in range(count, 365):
    a = s[i].translate({ord(i):None for i in '°daysC'}) # 
    a = float(a)
    
    #print("The week %d average for HDD is: %lf" %(i+1, a))
    print(a)

def HDD_week():
  data = pd.read_csv(r'Components/Data/WeatherData_UBC/UBC_HDD_CDD_Days.csv')
  df = pd.DataFrame(data, columns = ['UBC Heating Degree Days'])
  s = df["UBC Heating Degree Days"] # Set s to only be temp column.

  # Initialize variables.
  sum = 0
  count = 0

  for j in range(52):
    avg = 0
    sum = 0
    for i in range(count, count+7):
      a = s[i].translate({ord(i):None for i in '°daysC'}) # 
      sum += float(a)

    avg = sum / 7
    count += 7
    print("The week %d average for HDD is: %lf" %(j+1, avg))

def CDD_day():
  data = pd.read_csv(r'Components/Data/WeatherData_UBC/UBC_HDD_CDD_Days.csv')
  df = pd.DataFrame(data, columns = ['UBC Cooling Degree Days'])
  s = df["UBC Cooling Degree Days"] # Set s to only be temp column.

  # Initialize variables.
  count = 0

  for i in range(count, 365):
    a = s[i].translate({ord(i):None for i in '°daysC'}) # 
    a = float(a)
    
    #print("The week %d average for HDD is: %lf" %(i+1, a))
    print(a)

def CDD_week():
  data = pd.read_csv(r'Components/Data/WeatherData_UBC/UBC_HDD_CDD_Days.csv')
  df = pd.DataFrame(data, columns = ['UBC Cooling Degree Days'])
  s = df["UBC Cooling Degree Days"] # Set s to only be temp column.

  # Initialize variables.
  sum = 0
  count = 0

  for j in range(52):
    avg = 0
    sum = 0
    for i in range(count, count+7):
      a = s[i].translate({ord(i):None for i in '°daysC'}) # 
      sum += float(a)

    avg = sum / 7
    count += 7
    print("The week %d average for CDD is: %lf" %(j+1, avg))

def CDD_ln():
  data = pd.read_csv(r'Components/Data/WeatherData_UBC/UBC_HDD_CDD_Days.csv')
  df = pd.DataFrame(data, columns = ['UBC Cooling Degree Days'])
  s = df["UBC Cooling Degree Days"] # Set s to only be temp column.

  # Initialize variables.
  sum = 0
  count = 0
  ln = 0

  for j in range(52):
    avg = 0
    sum = 0
    for i in range(count, count+7):
      a = s[i].translate({ord(i):None for i in '°daysC'}) # 
      sum += float(a)

    avg = sum / 7
    ln = np.log(avg)
    count += 7

    # Note that natural log of 0 is -inf. 
    print("The week %d average for CDD_ln is: %lf" %(j+1, ln))


    

    
 
    
 
