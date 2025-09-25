# 1
def a(n):
  for i in range(n+1):
    print(i**2)

# 2
def b(n):
    a = [i for i in range(1, n+1)]
    a.remove(1)
    print(min(a))
            
b(10)

# 3
def c(n):
    a = [i for i in range(0, n+1) if (2 ** i) <= n]
    print(max(a))
    
c(10)

# 4
def d(x, y):
    a, c = x, 0
    while a <= y:
        a *= 1.1
        c += 1
        
    print(c)
        
d(10, 17)
    
# 5
def f(l):
    l.remove(0)
    print(len(l))
    
f([0,1,2,3,4,5,6,0])

# 6
def average(l):
    print(sum(l) / len(l))
    
average([1,2,3,4,5,6,7,0])

# 7
def g(l):
    i, c = 0, 0
    length = len(l)
    while i < length:
        if i+1 < length and l[i] < l[i+1]:
            c += 1
        else: continue
        i += 1
      
    print(c)
    
g([1, 4, 2, 3, 1, 6, 7, 8])

# 8
def h(l):
    i, c = 0, 1
    length = len(l)
    maxs = []
    while i < length:
        if i+1 < length and l[i] == l[i+1]:
            c += 1
        else: 
            maxs.append(c)
            c = 1
        i += 1
      
    print(max(maxs))
    
h([1, 1, 2, 3, 1, 1, 1, 8])
