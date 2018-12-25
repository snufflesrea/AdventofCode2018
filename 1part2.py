file = open('input.txt','r')
frequency = 0
result=set()
data = file.read().strip().split('\n')

while True:
    for line in data:
        frequency = frequency +int(line)
        if frequency in result:
            print frequency
            exit()
        else:
            result.add(frequency)
            continue
