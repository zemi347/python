# Question 5: Write a program to identify duplicate values from list
def checkIfDuplicates_1(listOfElems):
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True


listOfElems = ['Pakistan', 'India', 'Pakistan', 'Pakistan', 'Bangladesh', 'Afghanistan', 'Afghanistan',  'Pakistan']
 
result = checkIfDuplicates_1(listOfElems)
 
if result:
    print('Yes, list contains duplicates')
else:
    print('No duplicates found in list')    