### The try / except Stucture
#Surrounding fail same for bad data inputs.
#i.e traceback.

astr = 'hello bob'
try:
    istr = int(astr)
except:
    ister = -1

print('First', ister)
aster = '123'
try:
    ister = int(astr)
except:
    ister = -1
    
print('Second', ister)


raw = input('Enter a number ')
try:
    ival = int(raw)
except:
    ival = -1

if ival > 0 :
    print('Nice work! ')
else:
    print('Not a number ')