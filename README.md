# Data Structures And Algorithms
This is a library for all the data structures and algorthims I have learned so far, as well as code for everything.
<br>
<br>
For example, 
<br>
## Bubble Sort

```python
#A is the list we want to sort

def bubbleSort(A):
  N=len(A)
  for i in range(N):
    for j in range(N-1,i,-1):
      if A[j]<A[j-1]:
        A[j],A[j-1]=A[j-1],A[j]

```
