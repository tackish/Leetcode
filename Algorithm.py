#Bubble_Sort
def Bubble(List):
    count=len(List)
    for x in range(count):
     for y in range(count-x-1):
        if List[y] > List[y+1]:
         List[y],List[y+1] = List[y+1],List[y]
    return List
print(Bubble([5,3,2,4,1]))

#Quick_sort
def Quick_sort(List):
    if len(List) <1:
     return List
    Center_value=List[len(List)//2]
    left,right,mid= [],[],[]
    for x in List:
     if x > Center_value:
         left.append(x)
     elif x < Center_value:
         right.append(x)
     else:
        mid.append(x)
    return Quick_sort(left) + mid + Quick_sort(right)

print(Quick_sort([5,3,2,4,1]))

