#()tuples are immutable
from logging import exception, raiseExceptions

a=(1,2,3,34)
b=(1,23,42)
#print(a[1])
#print(a[-1])
#print(a[:4])
#print(a[0:])
#print(a)
#print(a+b)
#print(a.count(1))
i=0
while i < 4:
    print(a[i])
    i=i+1






#set is a data structure
a={2,5,60,2,12,3,4,22,45}
print(a)


#a.add(34)
#a.remove(2)
print(a)
b={22,45,8,}
#a.update(b)
print(a)
print("total element in the a:", str(len(a)))

#differnce 
a.difference(b)
diff=a.difference(b)
print(diff)

b.difference(a)
diifer=b.difference(a)
print(diifer)
print(a.intersection(b)) #union
print(b.union(a))

#converting data structures
list0=[1,2,4,5,6,6]
list_to_tuple=tuple(list0)
print(list_to_tuple)
list0_to_set=set(list0)
print(list0_to_set)

#dictionaries in data structure
dic={"name":"varinder", "age":26, "liveing":"berlin"}
print(dic["age"])
print(dic)
c=dic["liveing"]
print(c)
print(len(dic))
key_know=(dic.keys())
print(key_know)
value_know=(dic.values())
print(value_know)
dic["age"]=45
print(dic)
dic.update({"name":"Harry"})
print(dic)
dic["phne_number"]=93239024
print(dic)
dic.pop("name")
print(dic)

#control flow
age=21
if not age>10:
    print("child")


def list_calliing():
    a=[1,3,4,5,6,7,8]
    for i in a:
        if i==5:
            continue 
        print(i)


for j  in range(1,100,5):
    pass
        
#pass, continue, break

def addition(a,b):
    try:
        res=a+b
        return res

    except Exception as error:
        raise("programm crashing")
sum = addition(34, 6)
print(sum)



sum=addition(34,98)
print(sum)



cost=lambda a,b,c,d:(((a*b)**2)-c)+d
print(cost(2,5,2,3))

import mymodule
print(mymodule.name(3,33))
print(mymodule.sub(55,30))

#exception handling to handle the error and to make our code rebust
a=12
b=1
try:
   div = a / b
except Exception as error:
    raise Exception(error)

#tuple=(1,2,3,4,5)


x={1,2,3,4}
x.remove(3)
print(x)

k=[12,23,3,4,]
k.reverse()
del k[2]
print(k)

g={133,4,34,65}#set
f={3,4,5,6}
diff=g.difference(f)
print(diff, len(g))

























