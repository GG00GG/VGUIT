# 1
def g(a, b, c):
  print(a + b + c)

# 2
def g(a, b):
  print(0.5 * a*b)

# 3
def g(n):
  minutes = n // 60
  hours = minutes // 60

  if not n > 1*60*60*24:
    print(f'{hours:02}:{minutes:02}')

# 4
def l(a, b, c):
  part = a + b + a
  print(c // part)

# 5
def d(a, b, c):
  print(min([a, b, c]))

# 6
def s(a, b, c, d):
  if not (1 <= (a or b or c or d) <= 8):
    return

  print('НЕТ' if a == c or b == d else 'ДА')

# 7
def year(y):
  print('ДА' if y % 4 == 0 and y % 100 != 0 and y % 400 == 0 else 'НЕТ')

# 8
def taro(a, b, c):
  if a == b == c: print(3)
  elif a == b or a == c or b == c: print(2)
  else: print(0)

# 9
def choco(n, m, k):
  print('ДА' if n // m == k or m // n == k else 'НЕТ')
    
