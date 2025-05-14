void bubbleSort(int *A, int n){
    for (int i = 0; i < n; i++) {
        for (int i = n-1; i > 0; i--) {
            if(A[j]<A[j-1]){
                int temp=A[j];
                A[j]=A[j-1];
                A[j-1]=temp;
            }
        }
    }
}