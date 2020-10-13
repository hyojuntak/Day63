# N명의학생정보가있다. 
# 학생정보는학생의이름과학생의성적으로구분된다. 
# 각학생의이름과성적정보가주어졌을때
# 성적이낮은순서대로학생의이름을출력하는프로그램을
# 작성하시오.
# •첫째줄에학생의수N이입력된다. 
# •둘째줄부터N+1번째줄에는학생의이름을나타내는
# 문자열A와학생의성적을나타내는정수B가공백으로구분되어입력된다.  
# 모든학생의이름을성적이낮은순서대로출력한다. 
# 성적이동일한학생들의순서는자유롭게출력해도괜찮다. 
# 입력예시
# 2
# 홍길동95
# 이순신77
# 출력예시
# 이순신 홍길동

N = int(input())
N_list = []
name = ''
name_list = []

for i in range(N):
    r = input().split()
    N_list.append(r)

min = N_list[0][1]

for j in range(N):
    if min>N_list[j][1]:
        min = N_list[j][1]
        name = N_list[j][0]   
        name_list.append(name)
    else:
      name_list.append(N_list[j-1][0])
print(name_list)




########################


N = int(input())
N_list = []

for i in range(N):
    r = input().split()
    N_list.append(r)

G_list = list(zip(N_list,range(N)))
print(sorted(G_list))

for j in range(len(G_list)):
    print(G_list[j][0][0], end = " ", reversed=False)



#####오후#####
import numpy as np 
names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])
data = np.random.rand(7,4)
names
data

names =='Bob'
data[names =='Bob']


arr = np.arange(15).reshape((3,5))
arr


arr.T

arr = np.random.randn(6,3)
arr

np.dot(arr.T, arr)

arr = np.arange(16).reshape((2,2,4))
arr

arr.transpose((1,0,2))


arr
arr.swapaxes(1,2)


arr = np.arange(10)

arr

np.sqrt(arr)

np.exp(arr)

x = np.random.randn(8)

y = np.random.randn(8)

np.maximum(x,y)

arr = np.random.randn(7)*5
arr

remainder, whole_part = np.modf(arr)
remainder
whole_part


arr

np.sqrt(arr,arr)


import numpy as np 
points = np.arange(-5,5,0.01)


xs,ys = np.meshgrid(points, points)

z = np.sqrt(xs**2 + ys**2)


import matplotlib.pyplot as plt 

plt.imshow(z, cmap=plt.cm.gray); plt.colorbar()

plt.show()

xarr = np.array([1.1,1.2,1.3,1.4,1.5])
yarr = np.array([2.1,2.2,2.3,2.4,2.5])

cond = np.array([True,False,True,True,False])

result = [(x if c else y) for x,y,c in zip(xarr, yarr, cond)]

result

result = np.where(cond,xarr,yarr)

result

arr = np.random.randn(4,4)

arr

arr > 0

np.where(arr > 0,2,-2)

np.where(arr > 0, 2, arr)


arr = np.random.randn(5,4)

arr

arr.mean()

np.mean(arr)

arr.sum()

arr.mean(axis=1)

arr.sum(axis=0)

arr = np.array([0,1,2,3,4,5,6,7])

arr.cumsum()

arr = np.random.randn(6)

arr

arr.sort()

arr

arr = np.random.randn(5,3)

arr

arr.sort(1)[::-1]

arr


names = np.array(['Bob','Joe','Will','Bob','Will','Joe','Joe'])

np.unique(names)

ints = np.array([3,3,3,2,2,1,1,4,4])

np.unique(ints)

sorted(set(names))

values = np.array([6,0,0,3,2,5,6])

values


np.in1d(values,[2,3,6])

arr = np.arange(10)

arr

x = np.array([[1,2,3],[4,5,6]])

samples = np.random.normal(size=(4,4))

samples

from random import normalvariate
import timeit


N = 1000000

%timeit samples = [normalvariate(0,1) for _ in range(N)]
samples



import matplotlib.pyplot as plt 
import numpy as np

import random 
position = 0 
walk = [position]
steps = 1000
for i in range(steps):
    step = 1 if random.randint(0,1) else -1 
    position+=step
    walk.append(position)





plt.plot(walk[:100])
plt.show()

nstemps = 1000
draws = np.random.randint(0,2,size=nstemps)
steps = np.where(draws > 0,1,-1)
walk = steps.cumsum()
walk.min()
walk.max()
(np.abs(walk)>=10).argmax()

nwalks = 5000
nstemps = 1000
draws = np.random.randint()
