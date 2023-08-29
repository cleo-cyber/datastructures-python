# array=[5,6,9,10,11,12,0,2,3,4]
# array=[1,2,3,4,5,6,7,8]
array=[0]
def get_rotations(array):
    index=0
    l,r=0,len(array)-1

    if len(array)<=0:
        return -1
    
    for i,ele in enumerate(array):

        if array[l]<array[r]:
         return -1
        if len(array)==1:
            return i+1
        if array[i]>array[i+1] and i<len(array)-1:
            index=i+1
            # print(index)
            return index
        else:
            i=+1


    return index
    
cd=get_rotations(array)
print(cd)