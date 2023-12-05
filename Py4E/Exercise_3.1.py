#write a program to prompt the juser for hours and rate 
# per hour using input to compute gross pay.
# Pay the hourly rate for the hours up to 40 and 1.5 times the
# hourly rate for all hours worked worked > 40. use 45 hours and 
# a rate of 10.50 per hour, to test thge program (the pay should be 498.75). 
# you should use input to read a string and float() to convert the sting to a number
#Dont worry about error checking the user input - assume the user types numbers properly.


hours = input('enter hours worked \n')
hr = float(hours)  
    
while hr < 0 :
    input ('Enter a number greater than 0 \n')
    hr = float(input())
       
overtime = hr - 40
regtime = hr - overtime

rate = input('enter your rate \n')
rt = float(rate)

while rt < 0 :
    input ("Enter a number greater than 0 \n")
    rt = float(input())

otrate = rt * 1.5

if hr > 40 :
    
    print(overtime * otrate + regtime * rt) 
    
elif hr <= 40 :
    print(hr * rt)
