# Create a python list and access the indices of elements 
# while iterating over a sequence with a for loop
fruits=["Mango","Pineapple","Banana","Apple","Watermelon"]
for index,fruit in enumerate(fruits):print(index,fruit)

#Write a function that takes two numbers as input and returns their sum.
def numbers(num1,num2):
    
    return num1+num2
result = numbers(2,56)
print(result)

#Write a function that takes a string as input and returns the length of the string.
def names (Str1):
    return len(Str1)
a = names("Mercy")
print(a)
#Write a function that takes a list of numbers as input and returns the average of the numbers.
def average(numb):
    total= sum(numb)
    count =len(numb)
    avg = total/count
    return(avg)
numb =[3,89,45,90,3,5,7,]
b = average(numb)
print(b)
    
    #Write a function that takes a string as input and returns 
    # True if the string is a palindrome, and False otherwise.
def palindrome(Str2):
    Str2 = Str2.lower().replace(""," ")
    if Str2==Str2[::-1]:
        return True
    else:
        return False
    
Str2=("Civic")
result =palindrome(Str2)
print(result)

#Write a function that takes a list of numbers as input and returns the maximum number in the list
def returns(numss):
    maximum = max(numss)
    return(maximum)
numss= [34,567,21,678,4,59,98]
d=returns(numss)
print(d)

#Write a function that takes a list of numbers as input and returns the minimum number in the list.
def returning(num1):
    maximum = min(num1)
    return(maximum)
num1= [34,567,21,678,40,59,98]
e=returning(num1)
print(e)   

#Write a function that takes a list of strings as input and returns the longest string in the list
def long(longest):
    maxstr =""
    for x in longest:
        if len(x)> len(maxstr):
            maxstr=x
    return maxstr
longest = ["melon","watermelon","apple","mango","guava"]
longer = long(longest)
print(longer)

#Write a function that takes a list of strings as input and returns the shortest string in the list.
def short(shortest):
    minstr =""
    for f in shortest:
        if len(f)< len(minstr):
            f=minstr
    return f
shortest = ["melon","watermelon","apple","mango","guava","kiwi"]
shorter = short(shortest)
print(shorter)

#Write a function that takes a string as input and returns a new string with all vowels removed.
def vowels (str5):
    strr ="aeiouAEIOU"
    stt=""
    for c in str5:
        if c not in strr:
            stt +=c
    return stt
str5=("Loice is a student")
n=vowels(str5)
print(n)

#Write a function that takes a list of numbers as input and returns a new list with all even numbers removed.

def numbers(numss):
    list=[]
    for num in numss:
        if num %2 != 0:
            list.append(num)
            
    return list

numss=[1,2,3,4,5,6,7,8,10]
n= numbers(numss)
print(n)


    