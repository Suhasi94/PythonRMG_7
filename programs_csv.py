#1. Write a program to read all the names of the employee in employees.csv file
#2. Write a program to print only the salaries that are > 70000
#3. Write a program to group male and female employees in the file
#4. Write a program to group employees based on their team
#5. Write a program to sort the shares in test.csv file based on the share prices 
#6. Write a program to add all the shares in test.csv file
#7. Analysing vaccination data.
#a Total_vaccinations of all the countries.
#b Total_vaccinations by country.
#c Names of countries and WHO region.
#d Country and persons vaccinated, and get top 3 countries with most vaccinated people.
#e Countries with less than 10K vaccinated people.
#f Get the latest updated country with its total vaccinations and number of people vaccinated.

import csv
import os
os.chdir(r"C:\Users\User\OneDrive\Desktop\filehandling\files\csv_files")
"""
#1. Write a program to read all the names of the employee in employees.csv file
with open("employees.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    for data in reader:
        print(data["name"])

#2. Write a program to print only the salaries that are > 70000

with open("employees.csv") as file:
    reader = csv.reader(file)
    header = next(reader)
    print(header)
    for data in reader:
        if int(data[3]) > 70000:
            print(data[-1])
#3. Write a program to group male and female employees in the file
d = {}
with open("employees.csv") as file:
    reader = csv.DictReader(file)
    #header = next(reader)
    for data in reader:
        if data["gender"] not in d:
            d[data["gender"]] = [data["name"]]
        else:
            d[data["gender"]] += [data["name"]]
print(d)

#4. Write a program to group employees based on their team

d = {}
with open("employees.csv") as file:
    reader = csv.DictReader(file)
    header = next(reader)
    for data in reader:
        if data["team"] not in d:
            d[data["team"]] = [data["name"]]
        else:
            d[data["team"]] += [data["name"]]
print(d)

#5. Write a program to sort the shares in test.csv file based on the share prices
d = {}
from collections import Counter
with open("test.csv") as file:
    reader = csv.DictReader(file)
    #header = next(reader)
    for data in reader:
        if data["shares"] and data["price"] != " ":
            d[data["shares"]] = data["price"]
c = Counter(d)
print(c)
res = sorted(d.items(),key=lambda item:item[-1])
print(res)

#6. Write a program to add all the shares in test.csv file
from collections import Counter
with open("test.csv") as file:
    sum_ = 0
    reader = csv.DictReader(file)
    #header = next(reader)
    for data in reader:
        sum_ += int(data["shares"])
    print(sum_)
       
"""
#7. Analysing vaccination data.
#a Total_vaccinations of all the countries.
#c Names of countries and WHO region.
#d Country and persons vaccinated, and get top 3 countries with most vaccinated people.
#e Countries with less than 10K vaccinated people.
#f Get the latest updated country with its total vaccinations and number of people vaccinated.

with open("vaccination_data.csv") as file:
    d={}
    reader = csv.DictReader(file,skipinitialspace=True)
    header = next(reader)
    for data in reader:
        d[data["COUNTRY"]] = data["TOTAL_VACCINATIONS"]
#print(d)
from collections import defaultdict
d = defaultdict(list)
with open("vaccination_data.csv") as file:
    reader = csv.DictReader(file,skipinitialspace=True)
    header = next(reader)
    for data in reader:
        d[data["WHO_REGION"]] += [data["COUNTRY"]]
#print(d)

from collections import defaultdict,Counter
dd = defaultdict(list)
with open("vaccination_data.csv") as file:
    d = {}
    reader = csv.DictReader(file,skipinitialspace=True)
    header = next(reader)
    for data in reader:
        if data["PERSONS_VACCINATED_1PLUS_DOSE"] and data["COUNTRY"] != " ":
            d[data["COUNTRY"]] = data["PERSONS_VACCINATED_1PLUS_DOSE"]
res = sorted(d.items(),key=lambda item:int(item[-1])) #d
res1 = sorted(d.items(),key=lambda item:(int(item[-1])>10000)) #e
#print(res1)
#print(res[-1],res[-2],res[-3])

with open("vaccination_data.csv") as file:
    d={}
    reader = csv.DictReader(file,skipinitialspace=True)
    header = next(reader)
    for data in reader:
        d[data["COUNTRY"]] = [data["TOTAL_VACCINATIONS"],data["PERSONS_VACCINATED_1PLUS_DOSE"]]
    print(d)

"""
    

        














    
    



            
