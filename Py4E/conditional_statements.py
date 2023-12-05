print(5 == 5)
print(5 == 6)
type(True != False)
print(type(5 != 5))

#x != y               # x is not equal to y
#x > y                # x is greater than y
#x < y                # x is less than y
#x >= y               # x is greater than or equal to y
#x <= y               # x is less than or equal to y
#x is y               # x is the same as y
#x is not y           # x is not the same as y
x = 5
if x < 10 :
    print('smaller')
if x < 20:
    print('Bigger')
print('finis')

if x > 2 :
    print('Biger than 2')
    print('Still bigger')
print('Done with 2')

for i in range(5) :
    print(i)
    #nested if
    if i > 2 :
        print('Bigger than 2')
    print('Done with i', i)
print('All Done')

#2 way if, if else

x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')

print('All done')