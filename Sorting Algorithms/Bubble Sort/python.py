#A is the list we want to sort

def bubbleSort(A):
  N=len(A)
  for i in range(N):
    for j in range(N-1,i,-1):
      if A[j]<A[j-1]:
        A[j],A[j-1]=A[j-1],A[j]

L=[1,6,3,2]
bubbleSort(L)
print(L)
