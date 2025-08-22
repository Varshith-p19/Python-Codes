#find the largest number in the givrn list 


l = [11,22,33]

for i in l:
    largest = l[0]
    for i in l:
        if i>largest:
            largest = i
print(largest)
