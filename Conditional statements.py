## 1. If Statements ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
free_apps_ratings=[]
for i in apps_data[1:]:
    price=float(i[4])
    if(price==0.0):
         free_apps_ratings.append(float(i[7]))
avg_rating_free=sum(free_apps_ratings)/len(free_apps_ratings)
                                 

## 2. Booleans ##

a_price = 0
if(a_price==0):
     print('This is free')
if(a_price==1):
    print('This is not free')

## 3. The Average Rating of Non-free Apps ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
non_free_apps_ratings=[]
for i in apps_data[1:]:
    price=float(i[4])
    if(price!=0):
        non_free_apps_ratings.append(float(i[7]))
avg_rating_non_free=sum(non_free_apps_ratings)/len(non_free_apps_ratings)                                    
                                    

## 4. The Average Rating of Gaming Apps ##

from csv import *
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
non_games_ratings=[]
for i in apps_data[1:]:
    rating=float(i[7])
    genre=i[11]
    if(genre!='Games'):
         non_games_ratings.append(rating)
avg_rating_non_games=sum(non_games_ratings)/len(non_games_ratings)                  

## 5. Multiple Conditions ##

from csv import *
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
free_games_ratings=[]
for i in apps_data[1:]:
    if(float(i[4])==0.0 and i[11]=='Games'):
         free_games_ratings.append(float(i[7]))
avg_rating_free_games=sum(free_games_ratings)/len(free_games_ratings)            
        

## 6. The or Operator ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
games_social_ratings=[]
for i in apps_data[1:]:
    if(i[11]=='Social Networking' or i[11]=='Games'):
         games_social_ratings.append(float(i[7]))
avg_games_social=sum(games_social_ratings)/len(games_social_ratings)            

## 7. Combining Logical Operators ##

from csv import reader
opened_file=open("AppleStore.csv")
read_file=reader(opened_file)
apps_data=list(read_file)
nonfree_games_social_ratings=[]
for i in apps_data[1:]:
    if(float(i[4])!=0.0): 
        if(i[11]=='Social Networking' or i[11]=="Games"):
              nonfree_games_social_ratings.append(float(i[7]))
avg_non_free=sum(nonfree_games_social_ratings)/len(nonfree_games_social_ratings)       

## 8. Comparison Operators ##

opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)
rating=[]
n_apps_more_9=0
n_apps_less_9=0
for i in apps_data[1:]:
    if(float(i[4])>9):
           rating.append(float(i[7]))
           n_apps_more_9=n_apps_more_9+1
    if(float(i[4])<9):
          n_apps_less_9=n_apps_less_9+1
avg_rating=sum(rating)/len(rating)           

## 9. The else Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    if(price==0.0):
        app.append("free")
    else:
        app.append("non-free")
apps_data[0].append("free_or_not")
for i in apps_data[0:6]:
     print(i)

## 10. The elif Clause ##

# INITIAL CODE
opened_file = open('AppleStore.csv')
from csv import reader
read_file = reader(opened_file)
apps_data = list(read_file)

for app in apps_data[1:]:
    price = float(app[4])
    if(price==0):
        app.append("free")
    elif(price>0 and price<20):
        app.append("affordable")
    elif(price>=20 and price<50):
        app.append("expensive")
    elif(price>=50):
        app.append("very expensive")
apps_data[0].append("price_label")
print(apps_data[0:6])