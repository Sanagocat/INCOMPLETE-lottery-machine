#powerball : lottery number making machine
#Lotto : 1 ~ 45 : select 6 number 

# import random
from random import random
from random import randint

#1 45 -> integer random number!!!
 #return 1~10 (include 1, 10) integer number

count = 0
while(True):
  count = count+1
  print("Your " + str(count) + " lucky number is:")
  result = randint(1,45)
  print(result)
  
  if count==6:
    break


#input (from, to) 
def LNMM (a,b):
  print("The Prize numbers are " + str(randint(a,b)) +","+ str(randint(a,b)) + ","+str(randint(a,b)) +","+ str(randint(a,b)) + ","+str(randint(a,b)) +","+ str(randint(a,b)))
  
a=1  
b=65
LNMM(a,b)

