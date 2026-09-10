"""Welcome in The Project"""
"""< Password Generator >"""
#----------------------------------------------------#
# in This Project # 
 # I Use Some Module # 
   #-random =>[shuffle()] 
   #-string =>[ascii_uppercase(),ascii_lowercase(),digits(),punctuation(),join()]
 # I Use Basics of Python # 
  #-Function input()
  #-while loop 
  #-for loop 
  #-Function range()
  #-if else break Condition 
  #-list =>[append(),join()] 
 #Function print() 
 # try and except  
#----------------------------------------------------#
import string
import random

ListUpper = list(string.ascii_uppercase)
Listlower = list(string.ascii_lowercase)
Listdigits = list(string.digits)
ListPunctuation = list(string.punctuation)

print("====================================")
print("=== Welcome in Generate Password ===")
print("====================================")

Number_Password = input("How Many Length Of Password Do You Want? : ")

while True:
    try:
        Number_Password = int(Number_Password)

        if Number_Password < 6:
            print("Please Password At Least 6 Characters..!")
            Number_Password = input("Please Enter The Number Again: ")
        else:
            break

    except ValueError:
        print("Please Enter Numbers Only!")
        Number_Password = input("Please Enter The Number Again: ")


random.shuffle(ListUpper)
random.shuffle(Listlower)
random.shuffle(Listdigits)
random.shuffle(ListPunctuation)


Password = []

partOne = round(Number_Password * (30 / 100))
partTwo = round(Number_Password * (30 / 100))
partThree = round(Number_Password * (25 / 100))
partFour = round(Number_Password * (15 / 100))


for i in range(partOne):
    Password.append(ListUpper[i])

for j in range(partTwo):
    Password.append(Listlower[j])

for k in range(partThree):
    Password.append(Listdigits[k])

for l in range(partFour):
    Password.append(ListPunctuation[l])


random.shuffle(Password)

Password = "".join(Password)

print("Generated Password:", Password)

