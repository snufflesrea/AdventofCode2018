file = open('input2.txt','r')
counterlist = []
datas = file.readlines()

"This function will return the number of letter difference"
"from 2 string"
def comparestr (str1, str2):
    counter = 0
    if len(str2) < len(str1):
        min = str2
        max = str1
    else:
        min = str1
        max = str2

    for i in range(len(min)):
        if min[i] != max[i]:
            counter += 1

    return counter

for data in datas:
    str1 = data
    for data in datas:
        str2 = data
        if comparestr(str1,str2) == 1 :
            print ("str1 is {}str2 is {}".format(str1,str2))
