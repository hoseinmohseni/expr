import mod
import os
os.system('cls' or 'clear')

class color : 
    GREEN = '\033[92m'
    RED = '\033[91m'
    WHITE = '\033[0m'


print (color.GREEN + '======= WELCOME TO CALCULATOR ======')
print (color.GREEN + '==========                 =========')
print (color.GREEN + '=====                          =====')
print (color.WHITE + '=           Version : 1.01         =')
print (color.WHITE + '=  Coded by : S Hossein S Mohseni  =')
print (color.RED + '=====                          =====')
print (color.RED + '==========                 =========')
print (color.RED + '====================================')
print("")
print("")

start = input("Do You need help ? Y/N : ")

if start == "n" :

    result = input(color.WHITE + "Enter Expr : ")
    print(color.GREEN + "Answer : ")
    print(mod.Calculation(result))

elif start == "y" :
    print("You can write your phrase to calculate ")
    print("Example : 4+(2/2)")
    print("Run The Program again to use")



else : 
    print("Please enter y or n")