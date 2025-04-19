# initialize
a = ()
b = (1)
c = (1,)
d = (1,2,3,4)
e = (1,2,'apple','banana','melon')
f = (1,2,('apple','banana','melon'))
print(type(a), type(b), type(c), type(d), type(e), type(f))

# indexing
print(d[1])
print(d[0]+d[1]+d[2])
print(e[2]+e[3]+e[4])
print(e[-1])
print(f[-1])
print(f[-1][0])
print(f[:-1])

# type change
print(list(f[-1][1]))

# operation
print(d+e)
print(d+f[-1])
print(d*3)
print(e*3)

# tuple function

a = (1,2,3,4)
print(a.index(1))
print(a.count(1))
print(type(a[0]), type(a[1]))