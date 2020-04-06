import sys
def pf(n,k):
  if n==k:
    print(n)
    return 
  if n%k == 0:
    print(k)
    return pf(n//k, k)
  else:
    return pf(n, k+1)
#------------------

pf(int(sys.argv[1]),2)
