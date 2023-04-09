#Write a Python program to count the number of items in a
#dictionary that has a value greater than a certain number.

    #example
my_dict={"a":2,"b":3,"c":4,"d":5,"e":10,'f':1}
value = 5
count = len([x for x in my_dict.values()if x<=value])
print(count)
   
dicts= {"mango":7,"apple":2,"banana":10,"orange":3}
value =8
counts = len([d for d in dicts.values() if d <value])
print(counts)
    
    #PYTHON SETS
    # Write a Python program to create a set. 
fruits= {"mangoes","banana","guava","melon","pineapple"}
print(fruits)
 #iterate
for f in fruits:print(f)
fruits.add("kiwi")
print(fruits)
fruits.pop()
fruits.discard("guava")
print(fruits)
fruits2={"kiwi","watermelon","passion","banana"}
x =fruits.intersection(fruits2)
print(x)
y= fruits.union(fruits2)
print(y)
t = fruits.difference(fruits2)
print(t)
a = fruits.copy()
print(a)
a.clear()
print(a)
a= {1,56,98,2,987,4325,876,4,345}
for index,i in enumerate(a):print(index,i)
print(max(a))
print(min(a))
print(len(a))
v = fruits.difference_update(fruits2)
print(v)