import pandas as pd

def EUI_lab():
  # Read the file
  data = pd.read_csv('Components/Data/UBC/Campus/EUIbySpace2021.csv', encoding = 'unicode_escape')
  df = pd.DataFrame(data, columns = ['labTotalEUI'])
  s = df["labTotalEUI"]

  sum = 0
  avg = 0
  count = 0
  per_week = 7

  for j in range(52):   
    for i in range(count, per_week): 
        a = s[i].translate({ord(i):None for i in 'kWh/m²ï¿½Â'})
        sum += float(a) # convert data into int and get sum.

    avg = sum / 7
    sum = 0
    count += 7
    per_week += 7

    print("The week %d average is: %lf" %(j+1, avg)) 

def EUI_classroom():
  data = pd.read_csv(r'Components/Data/UBC/Campus/EUIbySpace2021.csv')
  df = pd.DataFrame(data, columns = ['classroomTotalEUI'])
  s = df["classroomTotalEUI"]

  sum = 0
  avg = 0
  count = 0
  per_week = 7

  # Up untill 2021-06-04
  for j in range(52):   
    for i in range(count, per_week): 
        a = s[i].translate({ord(i):None for i in 'kWh/m²ï¿½Â�'})
        sum += float(a) # convert data into int and get sum.


    avg = sum / 7
    sum = 0
    count += 7
    per_week += 7

    print("The week %d average is: %lf" %(j+1, avg)) 

def EUI_office():
  data = pd.read_csv(r'Components/Data/UBC/Campus/EUIbySpace2021.csv')
  df = pd.DataFrame(data, columns = ['officeTotalEUI'])
  s = df["officeTotalEUI"]

  sum = 0
  avg = 0
  count = 0
  per_week = 7

  # Up untill 2021-06-04
  for j in range(52):   
    for i in range(count, per_week): 
        a = s[i].translate({ord(i):None for i in 'kWh/m²ï¿½Â�'})
        sum += float(a) # convert data into int and get sum.

    avg = sum / 7
    sum = 0
    count += 7
    per_week += 7

    print("The week %d average is: %lf" %(j+1, avg)) 


def EUI_lib():
  data = pd.read_csv(r'Components/Data/UBC/Campus/EUIbySpace2021.csv')
  df = pd.DataFrame(data, columns = ['libraryTotalEUI'])
  s = df["libraryTotalEUI"]

  sum = 0
  avg = 0
  count = 0
  per_week = 7

  # Up untill 2021-06-04
  for j in range(52):   
    for i in range(count, per_week): 
        a = s[i].translate({ord(i):None for i in 'kWh/m²ï¿½Â�'})
        sum += float(a) # convert data into int and get sum.

    avg = sum / 7
    sum = 0
    count += 7
    per_week += 7

    print("The week %d average is: %lf" %(j+1, avg)) 