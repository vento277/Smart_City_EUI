# weekly max temp
# min temp
# rain mm
# ...more available if needed.
import pandas as pd

def check():
  df = pd.read_csv(r'Components/Data/WeatherData_Van/Van_Weather_Total.csv')
  print(df)

def Max_temp():
  data = pd.read_csv(r'Components/Data/WeatherData_Van/Van_Weather_Total.csv')
  df = pd.DataFrame(data, columns = ['Max Temp (°C)'])
  s = df["Max Temp (°C)"] # Set s to only be temp column.

  # Initialize variables.
  sum = 0
  count = 0

  for j in range(52):
    avg = 0
    sum = 0
    for i in range(count, count+7):
      a = s[i] # 
      sum += float(a)


    avg = sum / 7
    count += 7
    print("Week %d average: %lf" %(j+1, avg))
    
def rain():
  data = pd.read_csv(r'Components/Data/WeatherData_Van/Van_Weather_Total.csv')
  df = pd.DataFrame(data, columns = ['Total Rain (mm)'])
  s = df["Total Rain (mm)"] # Set s to only be temp column.

  # Initialize variables.
  sum = 0
  count = 0

  for j in range(52):
    avg = 0
    sum = 0
    for i in range(count, count+7):
      a = s[i] # 
      sum += float(a)


    avg = sum / 7
    count += 7
    print("Week %d average: %lf" %(j+1, avg))