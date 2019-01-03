import re
from collections import defaultdict

#This block of code is to register the input from file to dictionary wit set
#Input: file.txt. Output: {x1,y1:idn,idm, x2,y2:ido,idp, ..}
coordinat_list = defaultdict(set)
with open("input3.txt","r") as file:
    for string in file.read().strip().split("\n"):
        id,x,y,width,height = map(int,re.findall('\d+',string))
        for i in range(x,x+width):
            for j in range(y,y+height):
                coordinat_list[i,j].add(id)

#Part1
#Calculate the summary of the overlapping coordinat
#The overlapping coordinat will have two id, thus the len >1
sum = 0
for coordinat in coordinat_list:
    if len(coordinat_list[coordinat])>1:
        sum = sum+1
print (sum)

#Part2
#This block of code try to register the id which there is overlap
overlap_coordinat={0}
for coordinat in coordinat_list:
    if len(coordinat_list[coordinat])>1:
        for id in coordinat_list.get(coordinat):
            overlap_coordinat.add(id)

#This block of code will count the size where for each id no overlapping area
total = 0
for key,value in coordinat_list.items():
    if list(value)[0] not in overlap_coordinat:
        total = total+1
        print ("coordinat:{} id:{}".format(key,value))
