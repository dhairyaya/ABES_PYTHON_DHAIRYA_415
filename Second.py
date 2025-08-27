x,y,z=5,6,7
print(id(x))
print(id(y))
print(id(z))

#unpack a collection(in list,tuple)
f=["a","b","c"]
x,y,z=f
print(x)
print(y)
print(z)

#global variables
x="awesome"

def anyfunc():
    print("Python is " + x)

anyfunc()