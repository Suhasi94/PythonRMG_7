# to print the number of characters in a  sample.txt file

# to count the number of words in a file

# to print lines starting with vowels

# to print line_no and number of words in a line


import os
os.chdir(r"C:\Users\User\OneDrive\Desktop\filehandling\files")
 # with using len function
"""
with open("sample.txt") as file:
    count_char = 0
    for line in file:
        count_char += len(line)
    print(count_char)

# without using len

with open("sample.txt") as file:
    count_char = 0
    for line in file:
        for char in line:
            count_char += 1
    print(count_char)

# with using len
with open("sample.txt") as file:
    count_words = 0
    for line in file:
        words = line.split()
        count_words += len(words)
    print(count_words)

with open("sample.txt") as file:
    count_words = 0
    for line in file:
        words = line.split()
        for word in words:
            count_words += 1
    print(count_words)



# print lines starting with vowels

with open("sample.txt") as file:
    for line in file:
        if line.strip():
            if line[0] in "aeiouAEIOU":
                print(line)


# to print line_no and number of words in a line

with open("sample.txt") as file:
    count = 0
    for line_no, line in enumerate(file,start=1):
        if line.strip():
            for word in line.split():
                count += 1
            print(line_no,count)

with open("sample.txt") as file:
    
    for line_no, line in enumerate(file,start=1):
        words = line.split()
    print(line_no, len(words))
                
with open("sample.txt") as file:
    line_no = 0
    for line in file:
        line_no += 1
        word = line.split()
        print(line_no,len(word))
"""

#1. to read a file from the last line
#2. to count the number of spaces in the file
#3. to create a dictionary with each
  #""" word and its count pair in the file """
#4. most occurring word in the file
#5. to print nth line from a file
#6. to print 4th to 7th lines
#7. to print last 'n' lines from a file
#8. ip addresses and their count from access-log file

#9. most occurring brand names from data.txt
#10. names of the countries from football.txt file
  
##########################################
  
#1. to read a file from the last line
"""
with open("sample.txt") as file:
    for line in (list(file))[::-1]:
        print(line)

with open("sample.txt") as file:
    for line in reversed(list(file)):
        print(line)

#2. to count the number of spaces in the file
# without using inbuilt method
with open("sample.txt") as file:
    count = 0
    for line in file:
        for char in line:
            if char == " ":
                count += 1
print(count)

#with using inbuilt method

with open("sample.txt") as file:
    count = 0
    for line in file:
        count += line.count(" ")
    print(count)

#3. to create a dictionary with each
  # word and its count pair in the file
#4. most occurring word in the file

with open("sample.txt") as file:
    d = {}
    for line in file:
        if line.strip():
            words = line.split()
            for word in words:
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1
print(d)

res=sorted(d.items(),key=lambda item:item[-1])
print(res[-1])
print(res[-2])


#print nth line from the file
n = 5
with open("sample.txt") as file:
    for line_no,line in enumerate(file,start=1):
        if line_no == n:
            print(line)
            
with open("sample.txt") as file:
    count = 0
    for line in file:
        count +=1
        if 4 <= count < 8:
            print(line)
"""
"""
from itertools import islice
n=4
with open("sample.txt") as file:
    lines = islice(file,5)
    for line in lines:
        print(line)
        
from collections import deque

with open("sample.txt") as file:
    lines = deque(file,5)
    for line in lines:
        print(line)
from itertools import islice
n=5
with open("sample.txt") as file:
    count = 0
    for line in file:
        count += 1
    file.seek(0)
    lines = islice(file,count-n,count)
    for i in lines:
        print(i)

#8. ip addresses and their count from access-log file
d = {}
with open("access-log.txt") as file:
    for line in file:
        if line.strip():
            word = line.split()
            if word[0] not in d:
                d[word[0]] = 1
            else:
                d[word[0]] += 1
print(d)

l= []
with open("access-log.txt") as file:
    for line in file:
        if line.strip():
            word = line.split()
            l.append(word[0])

#print(l)
from collections import Counter
c = Counter(l)
print(c)
print(c.most_common(3))

#9. most occurring brand names from data.txt
from collections import defaultdict
dd = defaultdict(int)
with open("data.txt") as file:
    for line in file:
        brand = line.split()
        dd[brand[0]] += 1
print(dd)

    
#10. names of the countries from football.txt file
from collections import Counter
with open("football.txt",encoding = "UTF-8") as file:
    l = []
    for line in file:
        country = line.split()
        l.append(country[1])
print(Counter(l))


"""



    

        











































            

















    
