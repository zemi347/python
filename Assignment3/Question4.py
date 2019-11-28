# Question 4: Write a Python program to sum all the numeric items in a dictionarydef sumFunctiom(dic): 
def sumFunctiom(dic): 
    sum = 0
    for i in dic:
        if(type(dic[i])==int):
            sum = sum + dic[i] 
    return sum
dictionary = {'a': 10, 'b':15, 'c':22,'d':"maaz"} 
print("Sum :", sumFunctiom(dictionary))