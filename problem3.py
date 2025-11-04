a=int(input('enter a number:'))
if a==1 or a==2:
    print("1")
else:
    if a%2==0:
        count=a-1
    else:
        count=a
    result=[]
    for i in range(count):
        odd=2*i+1
        result.append(odd)
    print(",".join(map(str,result)))    

