a=[[1,2,3],[4,5,6],[7,8,9]]

b='V'
c="V"
if b==c:
    print("some letters")
else:
    print("different")
e=8
d=20 if e>5 else 12
print(d)

if e>15:
    print(15)
elif e>7:
    print(7)

i=0
while i<10:
    print(i)
    i+=1
f=["hello",2,True,"Terra"]

print(f[2])

for i in f:
    print(i)

#print(range(1,100,2))
for i in range(1,100,2):
    print(i,end=" ")

print()
print(len(f))
for i in range(0,len(f)):
    f[i]="Foo"
print(f)

def some_thing(a,b):
    return a+b

foo=some_thing
del(foo)
c=foo(3,4)
print(c)