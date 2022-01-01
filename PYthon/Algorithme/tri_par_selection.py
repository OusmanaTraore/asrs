import random

def generate_random_list(n,min,max):
    l=[]
    for i in range(n):
        e=random.randint(min,max)
        l.append(e)
    return l

def selection_sort(l):
    for unsorted_index in range(0,len(l)-1):
        min = l[unsorted_index]
        min_index = unsorted_index
        for i in range(unsorted_index+1, len(l)):
            if l[i] < min:
                min=l[i]
                min_index= i         
        l[min_index]=l[unsorted_index]
        l[unsorted_index]=min


l= generate_random_list(50,-1000,1000)
print("UNSORTED: ", l)

selection_sort(l)

print("SORTED: ", l)
