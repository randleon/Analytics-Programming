#!/usr/bin/env python
# coding: utf-8

# In[6]:


import csv
# be sure to update the path below to reflect your own environment!!
# also be sure that the code is properly indented after you paste it!


## made empty lists for rows
price_list = []
main_cost_list = []
num_doors_list = []
num_passenger_list = []
lugg_cap_list = []
safety_rating_list = []
class_of_vehicle = []
with open('/Users/RandyLeon/Desktop/cars-sample35.txt') as csvfile:
    readCSV = csv.reader(csvfile)
    for row in readCSV:
    # print each row as read by the csv.reader function
        price_list.append(row[0])
        main_cost_list.append(row[1])
        num_doors_list.append(row[2])
        num_passenger_list.append(row[3])
        lugg_cap_list.append(row[4])
        safety_rating_list.append(row[5])
        class_of_vehicle.append(row[6])


# In[8]:


##find the list index values of each automobile having a price rating of "med"
print(price_list)
price_list_med = []
print(len(price_list))
for i in range(len(price_list)):
	print(i)
	if price_list[i] == 'med':
		price_list_med.append(i)
print(price_list_med)


# In[27]:


##find the "number of passengers" value for each auto having a "price" value of "med"
print(num_passenger_list)
print(len(num_passenger_list))

##using found indices in previous task to find the number of passengers with price of "med"
print(num_passenger_list[6],
      num_passenger_list[16],
      num_passenger_list[20],
      num_passenger_list[23],
      num_passenger_list[26],
      num_passenger_list[29], )


# In[29]:


#making new list
num_pass_med = ["more", 2, 2, 2, 4, 2]


# In[30]:


#testing new list
print(num_pass_med)


# In[31]:


##Your fourth task is to 
##find the index value for each automobile having a price value of "high" 
##and a maintenance value that is not "low". 
##Create a new list to store your findings and be sure to print your results.


# In[68]:


print(price_list)
print(main_cost_list)


####find the index value for each automobile having a price value of "high"
print(price_list)
price_list_high = []
print(len(price_list))
for i in range(len(price_list)):
	print(i)
	if price_list[i] == 'high':
		price_list_high.append(i)
print(price_list_high)

##and a maintenance value that is not "low" trying to use same logic as previous function but this time using a not equals to
print(main_cost_list)
price_main_nlow = []
print(len(main_cost_list))
for i in range(len(main_cost_list)):
    print(i)
    if price_list[i] != 'low':
        price_main_nlow.append(i)
print(price_main_nlow)


# In[70]:


#testing new lists

print(price_list_high)
print(price_main_nlow)


# In[71]:


##let's go that worked


# In[72]:


##Your fifth task is to 
##find the index value for each auto having 2 doors and 
##luggage value of "big". 
##Create a new list to store your findings and be sure to print your results.


# In[73]:


#looking at list for each auto having two doors
print(num_doors_list)


# In[78]:


##finding indices of autos having two doors
two_door_cars = []
print(len(num_doors_list))
for i in range(len(num_doors_list)):
    print(i)
    if num_doors_list[i] == '2':
        two_door_cars.append(i)
print(two_door_cars)


# In[81]:


##looking at luggage list
print(lugg_cap_list)


# In[82]:


##finding and print index values of luggage capacities that are 'big'
big_luggage = []
print(len(lugg_cap_list))
for i in range(len(lugg_cap_list)):
    print(i)
    if lugg_cap_list[i] == 'big':
        big_luggage.append(i)
print(big_luggage)


# In[83]:


## these are the indices of the cars that have two doors AND have big luggage capacities 
    set(two_door_cars).intersection(big_luggage)


# In[84]:


#Finally, create a new list containing the only the integer equivalents of the doors values. 
#Keep in mind that the lists you have created thus far are composed solely of strings. 
#If you find any values of '5more' in your list, convert them to a '5'.
#After converting the '5more' values to '5', convert all of the items in your list 
#to their numeric equivalent and calculate the average number of doors 
#across all 35 autos using whichever of Python's built in functions you require. 
#Print your result.##


# In[85]:


#looking at number of doors list
print(num_doors_list)


# In[89]:


print(num_doors_list)


# In[ ]:




