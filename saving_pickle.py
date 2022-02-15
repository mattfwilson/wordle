import pickle
import os
os.system('clr')

names = ['Angus Young', 'Malcolm Young', 'Bon Scott']
print('Original List')
print(names)

pickle.dump(names, open('names.dat', 'wb'))

names.remove('Bon Scott')
print('Edited List')
print(names)

# Load saved data
names = pickle.load(open('names.dat', 'rb'))
print('Loading Original List')
print(names)

test = {"test1": 0, "test2": 0}
print(test)

test['test2'] += 1
print(test)