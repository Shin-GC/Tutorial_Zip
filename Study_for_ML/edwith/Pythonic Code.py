from functools import reduce
from collections import deque #stack과 queue를 지원하는 모듈
from collections import OrderedDict #기본 dict와 달리, 데이터를 입력한 순서대로 dict를 반환시켜준다.
from collections import defaultdict #Dict type 의 값에 기본 값을 지정, 신규 값 생성시 사용하는 방법
from collections import Counter
#split()과 join()
e='love,you,forever'
a,b,c=e.split(',')

list_e=[a,b,c]
print(list_e)

j=' '.join(list_e)

print(j)


#List Comprehension
#result=[i for i in range(1,10)]
result=[i for i in range(1,10+1) if  i %2==0]
print(result)


#Nested For loop
result=[i*j for i in range(1,10) for j in range(1,10)]

print(result)

a='abc'
b='123abc'

result=[i+j for i in a for j in b if not i==j]
#List Comprehension Nested For loop + if 
print(result)


words = 'The quick brown fox jumps over the lazy dog'.split()

result=[[w.upper(),w.lower(),len(w)]for w in words]
#split + list Comprehension
for i in result:
    print(i)


#Enumerate
for i,v in enumerate (['tic','tac','toc']): #list의 index와 값을 unpacking한다.
    print(i,v)

mylist=["a","b","c","d"]
print(list(enumerate(mylist)))
#list의 index와 값을 unpacking하여 list로 저장한다.

dic={i:j for i,j in enumerate('I love you'.split())}
#문장을 list로 만들고 list의 index와 값을 unpacking하여 dict로 저장한다.
print(dic)


a,b,c=zip((1,2,3),(4,5,6),(7,8,9))
print(f'\n{a}\n{b}\n{c}')

add=[sum(x) for x in zip((1,2,3),(4,5,6),(7,8,9))] #각 Tuple의 같은 index를 묶어 합을 list로 변환
print(add)

add=[sum(x) for x in zip([1,2,3],[4,5,6],[7,8,9])]#각 list의 같은 index를 묶어 합을 list 반환
print(add)

alist = ['a1', 'a2', 'a3']
blist = ['b1', 'b2', 'b3']
for a, b in zip(alist, blist): #병렬적으로 값을 추출한다 ex)a1과 b1이 추출되어 a와 b에 처음으로 들어감.
    print(a, b)

for i,(a,b) in enumerate(zip(alist,blist)):
    print(i,a,b)

#Lambda,map Python3부터는 권장되지 않으나 Pandas에서 사용되는 일이 많으므로 참고

two=lambda x: x*2
print(two(5))
mul=lambda x,y:x*y
#map: Sequence 자료형 각 element에 동일한 function을 적용 [python3부터는 list와 함께 쓸 것]
ex=[1,2,3,4,5]
ex2=[5,4,3,2,1]
print(list(map(two,ex)))

print(list(map(mul,ex,ex2)))

#filter 적용
print(list(map(lambda x: x**2 if x%2==0 else 0,ex)))

#map을 사용안하고 List Comprehension을 사용한 코드
print([a **2 for a in ex if a%2==0])

#Reduce Function
#map과 달리 list에 똑같은 function을 적용한 후 통합
print(reduce(lambda x,y:x+y,[1,2,3,4,5]))

def factorial(n):
    return reduce(lambda x,y:x*y,range(1,n+1))

print(factorial(5))

#Asterisk (*을 말함)
#단순 곱셈, 제곱연산, 가변인자 활용 등에 사용된다.

def asterisk_test(a,*args):
    print(a,args)
    print(type(args))

asterisk_test(1,2,3,4,5)

def asterist_test2(a,**kargs):
    print(a,kargs)
    print(type(kargs))

asterist_test2(1,one=2,two=3,three=4)

#Asterisk - unpacking a container
#tutle,dict등 자료형에 들어가 있는 값을 unpacking, 함수의 입력값, zip등에 유용하게 사용이 가능하다.
def unpacking_asterisk_test(a,*args):
    print(a,*args)
    print(type(args))

unpacking_asterisk_test(1,(2,3,4,5,))

#아래와 같은 방식
a,b,c=([1,2],[3,4],[5,6])
print(a,b,c)
data=([1,2],[3,4],[5,6])
print(*data)

#asterisk를 두개 쓰면 dict를 unpacking 한개는 list나 튜플 unpacking
def asterisk_test_dic(a,b,c,d):
    print(a,b,c,d)

data={'b':1,'c':2,'d':3}

asterisk_test_dic(10,**data)

for data in zip(*([1,2],[3,4],[5,6])):
    print(data)
    print(sum(data))
print([data for data in zip(*([1,2],[3,4],[5,6]))])
print([sum(data) for data in zip(*([1,2],[3,4],[5,6]))])

#Deque
#기존 list보다 효울적인 자료구조 제공
#효율적 메모리 구조로 처리속도 향상
deque_list=deque()

[deque_list.append(i) for i in range(5)]

print(deque_list)

deque_list.appendleft(10) #왼쪽에 값 삽입
print(deque_list)

deque_list.rotate(1) #rotate queue 구현 
print(deque_list)
deque_list.extend([5,6,7]) #삽입
print(deque_list)
deque_list.extendleft([8,9,10]) #왼쪽 삽입
print(deque_list)

deque_list.reverse() #뒤집기
print(deque_list)

d=OrderedDict()
d['x']=100
d['y']=200
d['z']=300
d['l']=400

for k,v in d.items():
    print(k,v)

d=defaultdict(object)#Default dctionary 생성
d=defaultdict(lambda:0) #Default 값을 0로 설정

print(d['fist'])

text="""What if we didn't have no pop
If the popsong writers just gave up
Popsong supplyment would stop
That would be something""".lower().split()
#defaultdict 없이 word counting 했을때
word_count={}
for word in text:
    if word in word_count.keys():
        word_count[word]+=1
    else:
        word_count[word]=1
print(word_count)

#Defaultdict 사용시

word_count=defaultdict(object) #Default dictionary 생성

word_count=defaultdict(lambda:0) #Default 값을 0으로 설정

for word in text:
    word_count[word]+=1

print(word_count)

#Counter :Sequence type의 data element들의 갯수를 dict로 반환

c=Counter()
c=Counter(text)
print(c)