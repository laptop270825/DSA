s='a*b#c'
result=[]
lt=list(s)
print(lt)
for i in lt:
    if i.islower():
        if result== None:
            result=[]
            result.append(i)
        else:
            result.append(i)
    elif i=='*':
        if result==[]:
            continue
        else:
            result.pop()
    elif i=='#':
        result=result.append(result)

     
