def insertionSort(A):
    N=len(A)
     for i in range(1,N):
        value=A[i]
        j=i
        while j>0 and A[j-1]>value:
            A[j]=A[j-1]
            j-=1
        A[j]=value
