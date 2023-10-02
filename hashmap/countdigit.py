# You are given a 0-indexed string num of length n consisting of digits.

# Return true if for every index i in the range 0 <= i < n, the digit i occurs num[i] times in num, otherwise return false.

# Soltuoion 1:
def solve( num):
    for i in range(len(num)):
        if num.count(str(i))!=int(num[i]):

            return False
        
    return True

# Solution 2:
# Challenge not working, returns false for 1210 
# def solve( num):
#     # Write your code here

    hashmap={}
    for i in num:
        if i not in hashmap:
            hashmap[i]=1
        else:
            hashmap[i]+=1
    for i in range(len(num)):
        if hashmap[num[i]]!=int(num[i]):
            return False
    return True

# # Sample test cases
# n='1210'
# print(solve(n))


 