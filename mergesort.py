def merge_sort(given):
    if len(given) <=1:
        return given
    else:
        mid = len(given) // 2
        left = merge_sort(given[:mid])
        right = merge_sort(given[mid:])
        new_list = merge(left,right)
        return new_list

def merge(listA,listB):
    a=0
    b=0
    new_list= list()

    while a<len(listA) and b < len(listB):
        if listA[a] < listB[b]:
            new_list.append(listA[a])
            a=a+1
        else:
            new_list.append(listB[b])
            b=b+1

    while a<len(listA):
        new_list.append(listA[a])
        a=a+1
    while b<len(listB):
        new_list.append(listB[b])
        b=b+1
    return new_list

a = [56, 89, 45, 34, 90, 32, 20, 67, 43]
print(merge_sort(a)) 
    
