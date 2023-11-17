import random


random.seed()

def bubble_sort(list):
    n = len(list)

    while n>0:
        for j in range (0,n-1):
            if list[j]>list[j+1]:
                pom = list[j]
                list[j]=list[j+1]
                list[j+1]=pom
        n-=1

    return list

def counting_sort(list):

    max_value = max(list)
    min_value = min(list)

    histogram = {}
    sorted_list = []

    for i in range(min_value, max_value + 1):
        histogram[i] = 0

    for i in list:
        histogram[i] += 1

    for k, v in histogram.items():
        for i in range(v):
            sorted_list += [k]

    return sorted_list

list=[]

for x in range (0,10) :
    list.append(random.randint(1,1000))
print(list)


list2 = [1, 4, 2, 4, 2, 2]
print(bubble_sort(list))
print(counting_sort(list))