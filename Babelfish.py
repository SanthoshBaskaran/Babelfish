list1=[]
list2=[]
count=0
result=[]
for i in range(10):
    try:
        inputs1=list(map(str,input().split()))
        list1.append(inputs1[0])
        list2.append(inputs1[1])
        count=count+1
    except IndexError:
        break
for j in range(count):
    try:
        inputs2=input()
        if inputs2 in list2:
            index1=list2.index(inputs2)
            string=list1[index1]
            result.append(string)
        else:
            result.append('eh')
    except IndexError:
        break
result.remove('eh')
for k in result:
    print(k)
