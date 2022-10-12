def insertion_sort(elements):
    for i in range(1, len(elements)):
        tmp=elements[i]
        j=i-1 #start from a previous element of i

        while j>=0 and elements[j]>tmp:
            elements[j+1] = elements[j] # swap elements 
            j=j-1;
        elements[j+1]=tmp



# Test cases

elements=[11,9,29,7,2,15,28]
insertion_sort(elements)
print(elements)
arr2=[12,14,13,11,10,18,16,17]
insertion_sort(arr2)
print(arr2)