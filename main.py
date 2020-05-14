def partition(low,high,a):
    pivot=a[high]
    i=low-1
    for j in range(low,high):
      if a[j]<pivot :
        i+=1
        t=a[i]
        a[i]=a[j]
        a[j]=t
    t=a[i+1]
    a[i+1]=a[high]
    a[high]=t
    return i+1
    
    
def quickSort(low,high,arr):
    if(low<high):
        p = partition(low,high,arr)
        quickSort(low,p-1,arr)
        quickSort(p+1,high,arr)
        
n=int(input("Enter the number of elements:"))
t=0
arr=[]
print("\nEnter the elements:")
while t<n:
    t+=1
    arr.append(int(input()))    
quickSort(0,n-1,arr)
print("\nSorted array: ")
for i in arr:
    print(i,end=" ")
