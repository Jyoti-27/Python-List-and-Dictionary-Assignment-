#!/usr/bin/env python
# coding: utf-8

# - Q.1 City = [‘Gurgaon’, ’Mumbai’, ’Bangalore’] 
#    
#     i) Print the second item from the list. 
#     
#     ii) Change the value from "Gurgaon" to "Kerala" 
#     
#     iii) Remove the last element of the list. 

# In[3]:


# i) Print the second item from the list.
City = ['Gurgaon', 'Mumbai', 'Bangalore']
print(City[1])


# In[4]:


# ii) Change the value from "Gurgaon" to "Kerala"
City = ['Gurgaon', 'Mumbai', 'Bangalore']
City[0]='Kerala'
print(City)


# In[3]:


# iii) Remove the last element of the list.
City = ['Gurgaon', 'Mumbai', 'Bangalore']
City.remove('Bangalore')
print(City)


# - Q.2 Use negative indexing to print the last item in the list. Make a list by yourself. 

# In[2]:


# Example 1
negative_list = ['D', 'A', 'T', 'A', 'S', 'C', 'I', 'E', 'N', 'T', 'I', 'S', 'T']
print(negative_list[-1])
print("Last Element is:",negative_list[-1])


# In[14]:


# Example 2
City = ['Gurgaon', 'Mumbai', 'Bangalore']
print(City[-1])


# - Q.3 Use a range of indexes to print the third, fourth, and fifth item in the list. Make a list by yourself. 

# In[3]:


# First Method
Students = ['Prajakta', 'Rujuta', 'Poonam', 'Shabdashree','Latika', 'Namita', 'Vandana']
print("Third, fourth and fifth items in the list are :", Students[2:5])


# In[5]:


# Second Method
indexes = ['Prajakta', 'Rujuta', 'Poonam', 'Shabdashree','Latika', 'Namita', 'Vandana']
print ("List index-value are : ") 
for index, value in zip(range(len(indexes)), indexes): 
    print (index, value)
    print("Third, fourth and fifth items in the list are :", indexes[2:5])
    print("Third items in the list is :", indexes[2])
print("Fourth items in the list is :", indexes[3])
print("Fifth items in the list is :", indexes[5])


# - Q.4 Remove the last element from the city list 

# In[8]:


# First Method
cities = ['Gurgaon', 'Mumbai', 'Bangalore']
print ("City popped is : ", cities.pop(-1))
print("Remaning elements in the list is:",cities)


# In[6]:


# Second Method
City = ['Gurgaon', 'Mumbai', 'Bangalore']
print(City[-1])
print(City[0:2])


# In[10]:


# Third Method 
myList = ['Gurgaon', 'Mumbai', 'Bangalore']
myList.remove(myList[len(myList)-1])
print("Remaning elements in the list is:",myList)


# - Q.5 fruits=[‘apple’,’lichi’,’guava’,’cherry’,’mango’,’watermelon’,’banana’] 
#    
#        i) Add "orange" at the end of the above list. 
# 
#       ii) Add "lemon" as the second item in the fruits list 

# In[27]:


#  i) Add "orange" at the end of the above list. 
fruits=['apple','lichi','guava','cherry','mango','watermelon','banana']
fruits.append('orange')
print("Added orange at the end of the list :",fruits)


# In[30]:


# ii) Add "lemon" as the second item in the fruits list.
fruits.insert(2,'lemon')
print("Inserted lemon as the second item to the list :", fruits)


# - Q.6 Remove ‘cherry’ from the fruit list given above. 

# In[29]:


fruits=['apple','lichi','guava','cherry','mango','watermelon','banana']
fruits.remove('cherry')
print("Removed cherry from the list :", fruits)


# - Q.7 Write the python program to let the user input a list of numbers and print the list in descending order. 

# In[35]:


# First Method
input_string = input("Enter numbers separated by comma ")
num_list  = input_string.split(",")
print(num_list)
newList = sorted(num_list, reverse=True)
print("Descending order list :" ,newList)


# In[11]:


# Second Method
print("Enter a list element separated by space:")
nums = list(map(int, input().split()))
nums.sort()
nums.reverse()
print("After sorting the list in descending order:",*nums)


# - Q.8 Write the python program to let the user input two lists and combine both the lists. 

# In[38]:


# First Method
list1=input("Enter list1 by comma seperated values :")
list2=input("Enter list2 by comma seperated values :")
list3=list1+','+list2
print("Combined lists are :" , list3)


# In[12]:


# Second Method
lis1=input("Enter list1 by space seperated values :")
lis2=input("Enter list2 by space seperated values :")
lis3=lis1+' '+lis2
print("Combined lists are :" , lis3)


# - Q.9 List = [10, 45, 78, 11, 9, 23]. Shuffle this list.

# In[40]:


import random
List = [10, 45, 78, 11, 9, 23]

print("Original list:", List)

random.shuffle(List)
print("List after first shuffle:", List)

random.shuffle(List)
print("List after second shuffle:", List)


# - Q.10 x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo'] 
# 
#        i) What is the expression that returns the 'z' in 'baz'?  
#        
#        ii) What expression returns the list ['baz', 2.718]? 
#        

# In[13]:


# i) What is the expression that returns the 'z' in 'baz'?  
# First Method
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
x[1][2][1][-1]
print("Expression that returns z in baz: ", x[1][2][1][-1])


# In[61]:


# i) What is the expression that returns the 'z' in 'baz'?  
# Second Method
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1])
print(x[1][2][1][2])
# print(x[1][2][1:3])


# In[68]:


# i) What is the expression that returns the 'z' in 'baz'?  
# Third Method 
print(x[-2])
print(x[1][2])
print(x[1][-1])
print(x[1][2][1])
print(x[1][2][-2])
print(x[1][2][1][-1])


# In[14]:


# ii) What expression returns the list ['baz', 2.718]?  
# First Method
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print(x[1][2][1:3])


# In[16]:


# ii) What expression returns the list ['baz', 2.718]?  
# Second Method
x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print("Expression that returns list: ", x[1][2][-2:])


# - Q.11 Extract element 20 from the above list. 

# In[17]:


x = [10, [3.141, 20, [30, 'baz', 2.718]], 'foo']
print("Extracted element 20 from the list :", x[1][1])


# - Q.12 You have a list a = [1, 2, 7, 8] 
#        
#  Write a Python statement using slice assignment that will fill in the missing values so that a equals [1, 2, 3, 4, 5, 6, 7, 8]
# 

# In[87]:


a = [1, 2, 7, 8]
a[2:2]=[3,4,5,6]
print("Missing values added to list a :", a)


# In[ ]:




