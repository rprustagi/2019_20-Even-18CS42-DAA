import sys
cnt = 0
def pow(a,n):
  global cnt
  cnt +=1
  if n==1:
    return a
  if (n%2 ==0):
    x = pow(a, n//2)
    return x * x
  else:
    x = pow(a, (n-1) // 2)
    return a * x * x

n = int(sys.argv[1])
y = pow(n, n)
print(cnt, y)