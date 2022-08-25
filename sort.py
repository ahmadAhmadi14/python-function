def sortingList(unsorted):
    ans=[]
    dic={}
    for i in unsorted:
        if len(i) not in dic:
            dic[len(i)]=[]
        dic[len(i)].append(i)
    for i in list(sorted(dic.keys())):
        ans+=sorted(dic[i])
    return ans


unsorted1 = sortingList(['1', '200', '150', '3'])
print(unsorted1)