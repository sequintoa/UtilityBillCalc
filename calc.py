'''
Created on jan 27, 2012

@author: mbk
'''

# Mahesh Bharath Keerthivasan
# University of Arizona

# UtilityBillCalc v1.0
# Date : 27 January 2012 

# UtilityBillCalc v1.1 
# Added creation of a log file 
# Last Modified : 24 May 2012 

#----------------------------------------------------------------------------

import sys
import datetime

#-----------------------------------------------------------------------------

print("Welcome to UtilityBillCalc v1.1 !!!", end="\n")
print(end="\n")
print("This is a Python 3.2 program that will help sharing electricity bills easier amongst roommates sharing an apartment.")
print(end="\n")
print(end="\n")

amount = float(input("Please enter the Bill Amount in Dollars: "))
print(end="\n")

days = int(input("Please enter the number of days for the bill: "))
print(end="\n")

amountPerDay = amount / days

numPersons = int(input("Please enter the number of persons sharing the bill :"))
print(end="\n")

isEvenShare = input("Is the share even ? Please enter Y / N : ")
print(end="\n")

if isEvenShare == 'Y' or isEvenShare == 'y':
    flag = 1

if isEvenShare == 'N' or isEvenShare == 'n' :
    print("Okay. This means that some of the occupants stay in the house for only a few days compared to the other.", end="\n")
    print(end="\n")
    daysList = []
    print("Do the days the occupants live overlap ? ie. if one person stays only for 12 days do all of the others also stay during that period ?")
    print(end="\n")
    isOverlapDays = input("Please enter Y / N : ")
    print(end="\n")

    if isOverlapDays == 'Y' or isOverlapDays == 'y' :

        flag = 2

        for i in range(numPersons) :
            print("Please enter number of days person {0} stayed: ".format(i + 1))
            tmp = int(input(""))
            print(end="\n")
            if tmp > days or tmp < 0 :
                print("Error !!! Please check the value you have entered.", end="\n")
                print("The number of days specified is invalid.")
                print(end="\n")
                sys.exit("The number of days specified is invalid.")
            daysList.append(tmp)
            
        sortedDaysList = daysList
        sortedDaysList.sort()
        #print(sortedDaysList)

    if isOverlapDays == 'N' or isOverlapDays == 'n' :

        flag = 3
        print("Currently UtilityBillCalc v1.0 does not support the No option for this question.")
        print(end="\n")

        # Think of an algorithm to fit this condition :)   


if flag == 1:
    amountPerPerson = (amountPerDay * days) / numPersons
    print("Each person pays {0} $ for the Bill".format(amountPerPerson))
    print(end="\n")
#    print(end="\n")
#    print("Thank you for using TEPCalc !!")
#    print(end="\n")

if flag == 2:
    
    amountList = []
    amountPerPersonList = []
    
    tmp1 = numPersons
    for i in range(numPersons):
        if i == 0 :
            daysTemp1 = sortedDaysList[i]
        else :
            daysTemp1 = sortedDaysList[i] - sortedDaysList[i - 1]

        #print("daysTemp1 is ",daysTemp1)
        tmp2 = (amountPerDay * daysTemp1) / tmp1
        #print(tmp2, tmp1)
        amountList.append(tmp2)
        tmp1 = tmp1 - 1
    #print(amountList)

    tmp3 = 0
    for i in range(numPersons):
        amountTemp1 = amountList[i] + tmp3
        tmp3 = amountTemp1
        amountPerPersonList.append(amountTemp1)
    #print(amountPerPersonList)

    # Sanity Check :
    amountTotal = 0
    for i in range(numPersons):
        amountTotal = amountPerPersonList[i] + amountTotal
    print("Sanity Check !!! The total based on the different shares is $ {0}".format(amountTotal))
    if amountTotal == amount :
        print(":-)")
    if amountTotal != amount :
        print(":-(")
    print(end="\n")
    

    for i in range(numPersons):
        print("The person who stayed for {0} days pays $ {1} for the Bill".format(sortedDaysList[i], amountPerPersonList[i]))
        print(end="\n")



# Create a log file for reference 

now = datetime.datetime.now()
f = open("../log/UtilityBillCalc.log","a")
f.write("---------------------------------------------\n")
f.write("UtilityBillCalc log : {0} \n\n".format(str(now)))
f.write("Bill Amount in $: {0} \n".format(amount))
f.write("Bill Duration in days : {0} \n\n".format(days))
for i in range(numPersons):
    f.write("The person who stayed for {0} days pays $ {1}\n".format(sortedDaysList[i], amountPerPersonList[i]))
f.write("---------------------------------------------\n")

print("Log file written successfully \n")
print("Thank you for using UtilityBillCalc !!")
print(end="\n")

