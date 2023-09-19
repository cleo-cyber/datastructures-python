sample="abcdefghijk"
stack=[]

def zz(s):
    for i in sample:
     stack.append(i)
    for i in stack:
        if i=='a':
            stack.pop() !="k"
            return False
    return stack
print(zz(sample))
    