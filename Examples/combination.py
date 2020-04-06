def comb(n,k):
  if k==0 or k==n:
    return 1
  return (comb(n-1,k) + comb(n-1,k-1))
#----------------------------------

print(comb(100,4))
