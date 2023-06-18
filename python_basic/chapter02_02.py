n = 700

print(n)
print(type(n))

x = y = z = 700

print(x, y, z)

m = 777

n = m
print(m, n)
m = 400
print(m, n)

print()
# id

m = 800
n = 600

print(id(m))
print(id(n))
print(id(m) == id(n))
print()
m = 800
n = 800

print(id(m))
print(id(n))
print(id(m) == id(n))
print()
