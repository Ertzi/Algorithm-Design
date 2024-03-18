import random
import time
import matplotlib.pyplot as plt
import timeit

def bubbleSort(arr):
    n = len(arr)
    # optimize code, so if the array is already sorted, it doesn't need
    # to go through the entire process
    swapped = False
    # Traverse through all array elements
    for i in range(n-1):
        # range(n) also work but outer loop will
        # repeat one time more than needed.
        # Last i elements are already in place
        for j in range(0, n-i-1):
 
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                swapped = True
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
         
        if not swapped:
            # if we haven't needed to make a single swap, we 
            # can just exit the main loop.
            return
        
lista = [2,4,6,3]
bubbleSort(lista)
print(lista)

def insertionSort(arr):
    n = len(arr)  # Get the length of the array
      
    if n <= 1:
        return  # If the array has 0 or 1 element, it is already sorted, so return
 
    for i in range(1, n):  # Iterate over the array starting from the second element
        key = arr[i]  # Store the current element as the key to be inserted in the right position
        j = i-1
        while j >= 0 and key < arr[j]:  # Move elements greater than key one position ahead
            arr[j+1] = arr[j]  # Shift elements to the right
            j -= 1
        arr[j+1] = key  # Insert the key in the correct position

lista = [2,4,6,3]
insertionSort(lista)
print(lista)

def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
 
    # create temp arrays
    L = [0] * (n1)
    R = [0] * (n2)
 
    # Copy data to temp arrays L[] and R[]
    for i in range(0, n1):
        L[i] = arr[l + i]
 
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
 
    # Merge the temp arrays back into arr[l..r]
    i = 0     # Initial index of first subarray
    j = 0     # Initial index of second subarray
    k = l     # Initial index of merged subarray
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
 
    # Copy the remaining elements of L[], if there
    # are any
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
 
    # Copy the remaining elements of R[], if there
    # are any
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
 
# l is for left index and r is right index of the
# sub-array of arr to be sorted
 
 
def mergeSort(arr, l, r):
    if l < r:
 
        # Same as (l+r)//2, but avoids overflow for
        # large l and h
        m = l+(r-l)//2
 
        # Sort first and second halves
        mergeSort(arr, l, m)
        mergeSort(arr, m+1, r)
        merge(arr, l, m, r)

lista = [2,4,6,3]
mergeSort(lista,0,len(lista)-1)
print(lista)


def heapify(arr, n, i):
    largest = i  # Initialize largest as root
    l = 2 * i + 1  # left = 2*i + 1
    r = 2 * i + 2  # right = 2*i + 2
 
 # See if left child of root exists and is
 # greater than root
 
    if l < n and arr[i] < arr[l]:
        largest = l
 
 # See if right child of root exists and is
 # greater than root
 
    if r < n and arr[largest] < arr[r]:
        largest = r
 
 # Change root, if needed
 
    if largest != i:
        (arr[i], arr[largest]) = (arr[largest], arr[i])  # swap
 
  # Heapify the root.
 
        heapify(arr, n, largest)
 
 
# The main function to sort an array of given size
 
def heapSort(arr):
    n = len(arr)
 
 # Build a maxheap.
 # Since last parent will be at (n//2) we can start at that location.
 
    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)
 
 # One by one extract elements
 
    for i in range(n - 1, 0, -1):
        (arr[i], arr[0]) = (arr[0], arr[i])  # swap
        heapify(arr, i, 0)

lista = [2,4,6,3]
heapSort(lista)
print(lista)


# Function to find the partition position
def partition(array, low, high):
    # choose the rightmost element as pivot
    pivot = array[high]

    # pointer for greater element
    i = low - 1

    # traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if array[j] <= pivot:

            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (array[i], array[j]) = (array[j], array[i])

    # Swap the pivot element with the greater element specified by i
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    # Return the position from where partition is done
    return i + 1


# function to perform quicksort with random pivot
def quickSortRandomPivot(array, low, high):
    if low < high:
        # Randomly choose pivot index
        pivot_index = random.randint(low, high)
        # Swap pivot element with the last element
        array[pivot_index], array[high] = array[high], array[pivot_index]
        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quickSortRandomPivot(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSortRandomPivot(array, pi + 1, high)


# function to perform quicksort with median pivot
def quickSortMedianPivot(array, low, high):
    if low < high:
        # Find median of first, middle and last element as pivot
        mid = (low + high) // 2
        if (array[low] <= array[mid] <= array[high]) or (array[high] <= array[mid] <= array[low]):
            pivot_index = mid
        elif (array[mid] <= array[low] <= array[high]) or (array[high] <= array[low] <= array[mid]):
            pivot_index = low
        else:
            pivot_index = high
        # Swap pivot element with the last element
        array[pivot_index], array[high] = array[high], array[pivot_index]
        # Find pivot element such that
        # elements smaller than pivot are on the left
        # elements greater than pivot are on the right
        pi = partition(array, low, high)
        # Recursive call on the left of pivot
        quickSortMedianPivot(array, low, pi - 1)
        # Recursive call on the right of pivot
        quickSortMedianPivot(array, pi + 1, high)


# function to perform quicksort
def quickSortEnd(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSortEnd(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSortEnd(array, pi + 1, high)


# function to perform quicksort
def quickSortStart(array, low, high):
    if low < high:
 
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(array, low, high)
 
        # Recursive call on the left of pivot
        quickSortStart(array, low, pi - 1)
 
        # Recursive call on the right of pivot
        quickSortStart(array, pi + 1, high)


lista = [2,4,6,3]
quickSortEnd(lista,0,len(lista)-1)
print(lista)



































num_max = 1000
times_1 = []
times_2 = []
times_3 = []
times_4 = []
times_5 = []
for num in range(1,num_max + 1, 100):
   lista = list(range(num, 1, -1))
   ex_time_1 = []
   for i in range(0,15):
        ex_time_1.append(timeit.timeit('bubbleSort(lista.copy())'
                                    ,globals=globals(),number = 10))
   times_1.append(min(ex_time_1))
   ex_time_2 = []
   for i in range(0,15):
        ex_time_2.append(timeit.timeit('insertionSort(lista.copy())'
                             ,globals=globals(),number = 10))
   times_2.append(min(ex_time_2))
   ex_time_3 = []
   for i in range(0,15):
        ex_time_3.append(timeit.timeit('mergeSort(lista.copy(), 0, len(lista)-1)'
                             ,globals=globals(),number = 10))
   times_3.append(min(ex_time_3))
   ex_time_4 = []
   for i in range(0,15):
        ex_time_4.append(timeit.timeit('heapSort(lista.copy())',
                             globals=globals(),number = 10))
   times_4.append(min(ex_time_4))
   ex_time_5 = []
   for i in range(0,15):
        ex_time_5.append(timeit.timeit('quickSortEnd(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 10))
   times_5.append(min(ex_time_5))
plt.plot(range(1,num_max+1, 100),times_1)
plt.plot(range(1,num_max+1, 100),times_2)
plt.plot(range(1,num_max+1, 100),times_3)
plt.plot(range(1,num_max+1, 100),times_4)
plt.plot(range(1,num_max+1, 100),times_5)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.legend(['bubbleSort','insertionSort','mergeSort','heapSort','quickSortEnd'])
plt.title("Comparación de algoritmos para listas inversamente ordenadas")
plt.show()