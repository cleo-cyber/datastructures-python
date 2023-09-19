def validPar(s):
    stack=[]
    for i in s:
        if i in ['(','{','[']:
            stack.append(i)

        else:
            if not stack:
                return False
            if i==')':
                if stack.pop()!='(':
                    return False
            if i=='}':
                if stack.pop()!='{':
                    return False
            if i==']':
                if stack.pop()!='[':
                    return False
                    
                
    if stack:
        return False
    
    return stack

# s ="()[]{}"
print(validPar("()[]{}"))