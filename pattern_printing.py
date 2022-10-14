# left justified triangle
"""
*
* *
* * *
* * * *
* * * * *
"""
"""
#row and coloum
for row in range(6):
    for col in range(row+1):
        print("*",end=" ")
    print()
print()
#only row
for row in range(1,6):
    print("* "*row)
"""

# right justified triangle
"""
        *
      * *
    * * *
  * * * *
* * * * *

"""
"""
for row in range(1,6):
    print(f"{'* '*row:>10}")

for row in range(1,6):
    print(f"{'* '*row:<10}")
"""

# centre justified triangle
"""
    *
   * *
  * * *
 * * * *
* * * * *
"""
"""
for row in range(1,6):
    print(f"{'* '*row:^10}")

"""

# inverted triangle pattern

"""
* * * * *
* * * *
* * *
* *
*
"""
"""
for row in range(5,0,-1):
    print("* "*row)

"""
"""
* * * * *
  * * * *
    * * *
      * *
        *
"""
"""

for row in range(5,0,-1):
    print(f"{'* '*row:>10}")

"""
"""
* * * * *
 * * * *
  * * *
   * *
    *
"""
"""
for row in range(5,0,-1):
    print(f"{'* '*row:^10}")

"""

"""
    *
   * *
  * * *
 * * * *
* * * * *
 * * * *
  * * *
   * *
    *
"""
"""
for row in range(1,6):
    print(f"{'* '*row:^10}")
for row in range(4,0,-1):
    print(f"{'* '*row:^10}")

"""
"""
*
*
*
* *
*
* * *
*
* * * *
"""
"""
for row in range(1, 5):
    print("*")
    print("* "*row)
"""
# alphabet pattern printing

"""
a
a b
a b c
a b c d
"""
"""
1    
12   
123  
1234 
12345
"""
"""
pat = ""
for row in range(1,6):
    pat = pat + str(row)
    print(pat)

for row in range(1,5):
    for col in range(1,row+1):
        print(col, end = " ")
    print()
"""
"""
    1
   12
  123
 1234
12345
"""
"""
pat = ""
for row in range(1,6):
    pat = pat + str(row)
    print(f"{pat:>5}")
"""
"""
     1    
    1 2   
   1 2 3  
  1 2 3 4 
 1 2 3 4 5

"""
"""
pat = ""
for row in range(1,6):
    pat = pat + ' '+ str(row)
    print(f"{pat:^10}")
"""
pat = ""
start = "a"
end = "d"
"""
for row in range(ord(start),ord(end)+1):
    pat = pat +' '+ chr(row)
    print(pat)
print()
"""
"""
for row in range(ord(start),ord(end)+1):
    pat = pat +" "+ chr(row)
    print(f"{pat:^10}")

"""

"""

l = [1,2,3,4]
def sq_(item):
    if item % 2 == 0:
        return item**2
    else:
        return 0
 
    
print(list(map(sq_,l)))
print(list(filter(sq_,l)))

"""
print(list(filter((lambda item:item**2 if item%2==0 else 0),[1,2,3,4])))


































    


    

   































    













