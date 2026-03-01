#insertion sort

def insertion_sort(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr [j]
            j = j-1
            print("i=",i,"j=",j,"arr[j]=",arr[j],"arr[j+1]=",arr[j+1],"key=",key,"arr=",arr)
        arr[j+1] = key
    return arr

numbers = [12, 9, 1, 5, 6]
print("Original array:", numbers)
print("Sorted array:", insertion_sort(numbers))
