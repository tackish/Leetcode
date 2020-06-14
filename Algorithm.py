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


#BFS (Breadth-first search) #수직으로 먼저 검색
#Dictionary 이용



Graph = {

    1 : [2,3,4],
    2 : [1,5,6],
    3 : [1],
    4 : [1,7,8],
    5 : [2,9,10],
    6 : [2],
    7 : [4,11,12],
    8 : [4],
    9 : [5],
    10: [5],
    11: [7],
    12: [7]

}



def bfs(Graph,Start_number):
    Visited =list()
    Queue = list()
    Queue.append(Start_number)

    while Queue:
        
        Temp=Queue.pop(0)
        if Temp not in Visited:
            Visited.append(Temp)
            Queue.extend(Graph[Temp])
    return Visited



print(bfs(Graph,1))


#DFS (Depth-first search) #수직으로 먼저 검색
#Dictionary 이용

def dfs(Graph,Start_number):
    Visited =list()
    Queue = list()
    Queue.append(Start_number)

    while Queue:
        
        Temp=Queue.pop()
        if Temp not in Visited:
            Visited.append(Temp)
            Queue.extend(Graph[Temp])
    return Visited



print(dfs(Graph,1))


#Recursive call : 팩토리얼 구현

def factorial(n):
    if n >1:
       return n * factorial(n-1)
    else:
        return n


print(factorial(4))


#Recursive examples
# 1부터 N까지의 곱

def multiple_Recursive(n):
    if n > 1:
        return n * multiple_Recursive(n-1)
    else:
        return n



print(multiple_Recursive(4))


# 리스트의 수를 모두 합

import random

data=random.sample(range(100),10)



def list_sum(data):
    if len(data) >1:
        return data[0]+list_sum(data[1:])
    else:
        return data[0]


print(data)
print(list_sum(data))


## 회문 연습
## level 처럼 뒤집어도 똑같은것 판별하는 함수

#리커시브 아닌 방식 부터
def reverse_same(word):
    reverse=''
    for x in word:
        reverse = x + reverse
    
    List_reverse=list(reverse)
    List_word=list(word)

    for y in range(len(List_reverse)):
        if List_reverse[y] == List_word[y]:
            return True
        else :
            return False


print(reverse_same("level"))


#리커시브 방식

def recursive_reverse_same(word):
    if len(word)<=1:
        return True
    
    if word[0] == word[-1]:
        return recursive_reverse_same(word[1:-1])
    else:
        return False



print(recursive_reverse_same("level"))

    


#binary_search 구현

def binary_search(data,search):
    if search == data[0] and len(data) ==1 : 
        return True
    if search != data[0] and len(data) ==1 :
        return False

    data.sort()

    medium=len(data)//2

    if search == data[medium]:
        return True

    else: 
        if search > data[medium]:
            return binary_search(data[medium:],search)

        if search < data[medium]:
            return binary_search(data[:medium],search)




import random

data_list=random.sample(range(100),50)
# 100 내에서 50개 값 랜덤 생성

print(data_list, " 랜덤 생성값")
print(binary_search(data_list,30)," 찾는값(binary) : 30")



#sequencial_search 순차탐색

def seq_search(data,search):
    count = len(data)
    for x in range(count):
        if data[x]==search:
            return True
    return False

print(seq_search(data_list,30)," 찾는값(seq) : 30")


## 클래스 연습

class test:
    #셀프는 인스턴스 자체를 인자로 받는다는 뜻. 꼭 self 아니어도 됨
    def __init__(self):
        self.result=0

    def add(self,a,b):
        #a,b를 인자로 받는다는 뜻. self는 인스턴스를 지칭
        self.a=a
        self.b=b

        return a+b


a=test()

a.add(1,2)

print(a.a+a.b)

##젠킨스 연동 완료, 푸시 웹훅 테스트

## 코드파이프라인 테스트, 푸시 웹훅 테스트