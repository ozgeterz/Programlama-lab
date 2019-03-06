# recursive fonksiyon ile üst alma ,faktoriyel hesaplama ve fibonacci sayısı

def fibonacci_loop(n):
  a,b=0,1
  if(n==0):
    return 0
  for i in range(n-1):
    a,b=b,a+b
  return b

print(fibonacci_loop(8))

def fib_recursive(n):
  if(n<2):
    return n
  else:
    return fib_recursive(n-1)+fib_recursive(n-2)

print(fib_recursive(8))

for i in range(10):
  r1,r2=fibonacci_loop(i),fib_recursive(i)
  print("Fibonacci loop : ",r1,end= " ")
  print("Fibonacci recursive : ",r2,end="\n")


def fact_loop(n):
  s=1
  for i in range(1,n+1):
    s=s*i
  return s

def fact_recursive(n):
  if(n==1):
    return 1
  else:
    return n*fact_recursive(n-1)

for i in range(1,10):
  r1,r2=fact_loop(i),fact_recursive(i)
  print("Faktoriyel loop : ",r1,end= " ")
  print("Faktoriyel recursive : ",r2,end="\n")



def power_loop(m,n):
  s=m
  for i in range(1,n+1):
    s=s*m
  return s

def power_recursive(m,n):
  if(n==0):
    return 1
  elif(n==1):
    return m
  elif(n%2==0):
    return power_recursive(m*m,n//2)
  elif(n%2!=0):
    return power_recursive(m*m,n//2)*m

print(power_recursive(5,2))
