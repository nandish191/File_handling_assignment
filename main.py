
f=open("document.txt", mode="r")
print(f)
s=f.read()
print(s)
f.close()

f=open("document.txt", mode="r")
s=f.read(4)
print(s)
f.close()

f=open("document.txt", mode="r")
s=f.readlines()
print(s)

s=f.readlines(1)
print(s)

s=f.readline(3)
print(s)

f=open("data.txt", mode="w")
f.write("bangalore located in karnataka\n")
f.write("it is the capital city of karnataka also\n")
f.write("silicon valley of india ")
f.close()

a=open("data.txt", mode="r")
s=a.read(10)
# read=a.readlines()
# print(read)
print(s)

f=open("data.txt", mode="r+")
x=f.readlines()
# for lines in x:
#     print(lines)
f.write("\nnew line added")
print(x)


print(x)
f=open("data.txt", mode="a")
f.write("\nbesant techologies training center located in rajajinagar Bangalore ")
f.close()
f=open("data.txt", mode='r')
a=f.readlines()
for lines in a:
    print(lines)
# print(a)
f.close()

f=open("image.jpg", mode="rb")
a=f.read()
f.close()

new_copy=open("image_copy.jpg", mode="wb" )
new_copy.write(a)
f.close()

f=open("excel_data.xlsx", mode='r')
a=f.readlines()
print(a)
f.close() // error

import pandas as pd

data_frame=pd.read_excel("excel_data.xlsx")
print(data_frame.head(data_frame['Id']))

x=data_frame['City']=data_frame.City.astype('category')
print(x)

# ##O/P
# 0          New York
# 1          New York
# 2          New York
# 3          New York
# 4          New York
#              ...
# 1048570         NaN
# 1048571         NaN
# 1048572         NaN
# 1048573         NaN
# 1048574         NaN
# Name: City, Length: 1048575, dtype: category
# Categories (4, object): ['Boston', 'Los Angeles', 'New York', 'San Diego']

print(data_frame.memory_usage())

# ##O/P
# Index             132
# Id            8388600
# Date          8388600
# Region        8388600
# City          8388600
# Category      8388600
# Product       8388600
# Column4       8388600
# Qty           8388600
# Unit Price    8388600
# print(dir(data_frame))


print(data_frame.head())

# ###O/P
#    Id       Date Region      City Category         Product  Column4    Qty  Unit Price
# 0  ID07354 2022-01-10  North  New York  Cookies  Chocolate Chip      NaN   82.0        1.87
# 1  ID07359        NaT  North  New York     Bars          Carrot      NaN  100.0        1.77
# 2  ID07360 2024-10-25  North  New York   Snacks    Potato Chips      NaN   28.0        1.35
# 3  ID07366 2022-02-15  North  New York   Snacks    Potato Chips      NaN   27.0        1.35
# 4  ID07371 2022-03-02  North  New York  Cookies  Chocolate Chip      NaN   85.0        1.87

print(data_frame.head(8))

# ###O/P 
#      Id       Date Region      City Category         Product  Column4    Qty  Unit Price
# 0  ID07354 2022-01-10  North  New York  Cookies  Chocolate Chip      NaN   82.0        1.87
# 1  ID07359        NaT  North  New York     Bars          Carrot      NaN  100.0        1.77
# 2  ID07360 2024-10-25  North  New York   Snacks    Potato Chips      NaN   28.0        1.35
# 3  ID07366 2022-02-15  North  New York   Snacks    Potato Chips      NaN   27.0        1.35
# 4  ID07371 2022-03-02  North  New York  Cookies  Chocolate Chip      NaN   85.0        1.87
# 5  ID07376 2022-03-17  North  New York     Bars          Carrot      NaN   38.0        1.77
# 6  ID07377 2022-03-20  North  New York   Snacks    Potato Chips      NaN   68.0        1.68
# 7  ID07383 2022-04-07  North  New York     Bars          Carrot      NaN   91.0        1.77

print(data_frame.describe())

# ##O/P
#                       Date  Column4           Qty  Unit Price
# count                  243      0.0    245.000000  244.000000
# mean   2023-01-09 18:40:00      NaN    126.628571    2.200820
# min    2022-01-01 00:00:00      NaN     20.000000    1.350000
# 25%    2022-07-10 12:00:00      NaN     32.000000    1.770000
# 50%    2023-01-08 00:00:00      NaN     47.000000    1.870000
# 75%    2023-07-07 12:00:00      NaN     81.000000    2.840000
# max    2024-10-25 00:00:00      NaN  15512.000000    3.490000
# std                    NaN      NaN    988.083414    0.600169


print(data_frame.tail())
# ##O/P
#         Id Date Region City Category Product  Column4      Qty  Unit Price
# 1048570  NaN  NaT    NaN  NaN      NaN     NaN      NaN      NaN         NaN
# 1048571  NaN  NaT    NaN  NaN      NaN     NaN      NaN      NaN         NaN
# 1048572  NaN  NaT    NaN  NaN      NaN     NaN      NaN      NaN         NaN
# 1048573  NaN  NaT    NaN  NaN      NaN     NaN      NaN      NaN         NaN
# 1048574  NaN  NaT    NaN  NaN      NaN     NaN      NaN  15512.0         NaN


for ele in data_frame:
    print(ele)

##O/P
# Id
# Date
# Region
# City
# Category
# Product
# Column4
# Qty
# Unit Price