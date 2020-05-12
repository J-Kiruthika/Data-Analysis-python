## 1. Functions ##

a_list = [4444, 8897, 6340, 9896, 4835, 4324, 10, 6445,
          661, 1246, 1000, 7429, 1376, 8121, 647, 1280,
          3993, 4881, 9500, 6701, 1199, 6251, 4432, 37]
sum_manual=0
for i in a_list:
    sum_manual=sum_manual+i
print(sum_manual)    

## 2. Built-in Functions ##

ratings = ['4+', '4+', '4+', '9+', '12+', '12+', '17+', '17+']
content_ratings={}
for i in ratings:
    if(i in content_ratings):
        content_ratings[i]+=1
    else:
        content_ratings[i]=1


## 3. Creating Our Own Functions ##

def square(data):
    return data*data
squared_10=square(10)
squared_16=square(16)

## 4. The Structure of a Function ##

def add_10(num):
    return num+10
add_30=add_10(30)
add_90=add_10(90)
    

## 5. Parameters and Arguments ##

def square(num):
    return num*num
squared_6=square(6)
squared_11=square(11)

## 6. Extract Values From Any Column ##

from csv import *
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
def extract(num):
    list=[]
    for i in apps_data[1:]:
        value=(i[num])
        list.append(value)
    return list
genres=extract(11)

## 7. Creating Frequency Tables ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
def freq_table(list):
    dictionary={}
    for i in list:
        if(i in dictionary):
            dictionary[i]+=1
        else:
            dictionary[i]=1
    return dictionary
genres=[]
for i in apps_data[1:]:
        genres.append(i[11])
genres_ft=freq_table(genres)


## 8. Writing a Single Function ##

from csv import *
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)

def freq_table(num):
    dictionary={}
    for i in apps_data[1:]:
        if(i[num] in dictionary):
            dictionary[i[num]]+=1
        else:
            dictionary[i[num]]=1
    return dictionary
ratings_ft=freq_table(7)
    
    

## 9. Reusability and Multiple Parameters ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)


def freq_table(data,index):
    frequency_table = {}
    
    for row in data[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
            
    return frequency_table
ratings_ft=freq_table(apps_data,7)

## 10. Keyword and Positional Arguments ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def freq_table(data_set, index):
    frequency_table = {}
    
    for row in data_set[1:]:
        value = row[index]
        if value in frequency_table:
            frequency_table[value] += 1
        else:
            frequency_table[value] = 1
        
    return frequency_table
content_ratings_ft=freq_table(apps_data,10)
ratings_ft=freq_table(apps_data,7)
genres_ft=freq_table(apps_data,11)

## 11. Combining Functions ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

def extract(data_set, index):
    column = []    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length
def mean(a_list):
    return find_sum(a_list)/find_length(a_list)
price=[]
for i in apps_data[1:]:
    price.append(i[4])
avg_price=mean(price)    

## 12. Debugging Functions ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
def extract(data_set, index):
    column = []
    
    for row in data_set[1:]:
        value = row[index]
        column.append(value)
    
    return column

def find_sum(a_list):
    a_sum = 0
    for element in a_list:
        a_sum += float(element)
    return a_sum

def find_length(a_list):
    length = 0
    for element in a_list:
        length += 1
    return length

def mean(data_set, index):
    column = extract(data_set, index)
    return find_sum(column) / find_length(column)

avg_price = mean(apps_data, 4)
avg_rating = mean(apps_data, 7)