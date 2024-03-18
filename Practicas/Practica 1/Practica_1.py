
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


# Python program for implementation of MergeSort
 
# Merges two subarrays of arr[].
# First subarray is arr[l..m]
# Second subarray is arr[m+1..r]
 
 
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




#!/usr/bin/python
# -*- coding: utf-8 -*-
# Python program for implementation of heap Sort
 
# To heapify subtree rooted at index i.
# n is size of heap
 
 
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


# Python program for implementation of Quicksort Sort
 
# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot

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


# Comparamos las funciones para listas ordenadas de tamaños 
# 1, 251, ..., 2501
num_max = 1000
times_1 = []
times_2 = []
times_3 = []
times_4 = []
times_5 = []
for num in range(1,num_max + 1, 100):
   lista = list(range(0, num))
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
plt.title("Comparación de algoritmos para listas ordenadas")
plt.show()


# Comparamos las funciones para listas inversamente ordenadas
# de tamaños 1, 101, 201,..., 1001
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



# Comparamos las funciones para listas aleatorias de 
# tamaños 1, 501, ..., 5001
num_max = 1000
times_1 = []
times_2 = []
times_3 = []
times_4 = []
times_5 = []
for num in range(1,num_max + 1, 500):
   ex_time_1 = []
   ex_time_2 = []
   ex_time_3 = []
   ex_time_4 = []
   ex_time_5 = []
   for i in range(0,30):
        lista = []
        for j in range(0,num):
            lista.append(random.random())
        ex_time_1.append(timeit.timeit('bubbleSort(lista.copy())'
                                    ,globals=globals(),number = 1))
        ex_time_2.append(timeit.timeit('insertionSort(lista.copy())'
                             ,globals=globals(),number = 1))
        ex_time_3.append(timeit.timeit('mergeSort(lista.copy(), 0, len(lista)-1)'
                             ,globals=globals(),number = 1))
        ex_time_4.append(timeit.timeit('heapSort(lista.copy())',
                             globals=globals(),number = 1))
        ex_time_5.append(timeit.timeit('quickSortEnd(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 1))
   times_1.append(min(ex_time_1))
   times_2.append(min(ex_time_2))
   times_3.append(min(ex_time_3))
   times_4.append(min(ex_time_4))
   times_5.append(min(ex_time_5))

plt.plot(range(1,num_max+1, 500),times_1)
plt.plot(range(1,num_max+1, 500),times_2)
plt.plot(range(1,num_max+1, 500),times_3)
plt.plot(range(1,num_max+1, 500),times_4)
plt.plot(range(1,num_max+1, 500),times_5)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.legend(['bubbleSort','insertionSort','mergeSort','heapSort','quickSortEnd'])
plt.title("Comparación de algoritmos para listas aleatorias")
plt.show()

# Comparamos las funciones para listas aleatorias de 
# tamaños 1, 501, ..., 5001, pero en este caso con los tres algoritmos
# más rápidos.
num_max = 1000
times_1 = []
times_2 = []
times_3 = []
times_4 = []
times_5 = []
for num in range(1,num_max + 1, 500):
   ex_time_1 = []
   ex_time_2 = []
   ex_time_3 = []
   ex_time_4 = []
   ex_time_5 = []
   for i in range(0,30):
        lista = []
        for j in range(0,num):
            lista.append(random.random())
        ex_time_3.append(timeit.timeit('mergeSort(lista.copy(), 0, len(lista)-1)'
                             ,globals=globals(),number = 1))
        ex_time_4.append(timeit.timeit('heapSort(lista.copy())',
                             globals=globals(),number = 1))
        ex_time_5.append(timeit.timeit('quickSortEnd(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 1))
   times_3.append(min(ex_time_3))
   times_4.append(min(ex_time_4))
   times_5.append(min(ex_time_5))
plt.plot(range(1,num_max+1, 500),times_3)
plt.plot(range(1,num_max+1, 500),times_4)
plt.plot(range(1,num_max+1, 500),times_5)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.legend(['mergeSort','heapSort','quickSortEnd'])
plt.title("Comparación de los algoritmos más rápidos para listas aleatorias")
plt.show()














# Vamos a comparar el tiempo de ejecución de bubbleSort para listas
# ordenadas, inversamente ordenadas y desordenadas de distintos tamaños.
num_max = 1000
times_21 = []
times_22 = []
times_23 = []

for num in range(1,num_max + 1, 100):
   
   lista_21 = list(range(1, num))
   ex_time_21 = []
   for i in range(0,15):
        ex_time_21.append(timeit.timeit('bubbleSort(lista_21.copy())'
                             ,globals=globals(),number = 10))
   times_21.append(min(ex_time_21))

   lista_22 = list(range(num, 1, -1))
   ex_time_22 = []
   for i in range(0,15):
        ex_time_22.append(timeit.timeit('bubbleSort(lista_22.copy())'
                             ,globals=globals(),number = 10))
   times_22.append(min(ex_time_22))

   lista_23 = []
   for i in range(0,num):
       lista_23.append(random.random())
   ex_time_23 = []
   for i in range(0,15):
        ex_time_23.append(timeit.timeit('bubbleSort(lista_23.copy())'
                             ,globals=globals(),number = 10))
   times_23.append(min(ex_time_23))

plt.plot(range(1,num_max+1, 100),times_21)
plt.plot(range(1,num_max+1, 100),times_22)
plt.plot(range(1,num_max+1, 100),times_23)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.title("Velocidad de ejecución de BubbleSort")
plt.legend(['Lista ordenada','Lista inversamente ordenada',
            'Lista desordenada'])
plt.show()


# Vamos a comparar el tiempo de ejecución de insertionSort para listas
# ordenadas, inversamente ordenadas y desordenadas de distintos tamaños.
num_max = 1000
times_21 = []
times_22 = []
times_23 = []

for num in range(1,num_max + 1, 100):
   
   lista_21 = list(range(1, num))
   ex_time_21 = []
   for i in range(0,15):
        ex_time_21.append(timeit.timeit('insertionSort(lista_21.copy())'
                             ,globals=globals(),number = 10))
   times_21.append(min(ex_time_21))

   lista_22 = list(range(num, 1, -1))
   ex_time_22 = []
   for i in range(0,15):
        ex_time_22.append(timeit.timeit('insertionSort(lista_22.copy())'
                             ,globals=globals(),number = 10))
   times_22.append(min(ex_time_22))

   lista_23 = []
   for i in range(0,num):
       lista_23.append(random.random())
   ex_time_23 = []
   for i in range(0,15):
        ex_time_23.append(timeit.timeit('insertionSort(lista_23.copy())'
                             ,globals=globals(),number = 10))
   times_23.append(min(ex_time_23))

plt.plot(range(1,num_max+1, 100),times_21)
plt.plot(range(1,num_max+1, 100),times_22)
plt.plot(range(1,num_max+1, 100),times_23)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.title("Velocidad de ejecución de InsertionSort")
plt.legend(['Lista ordenada','Lista inversamente ordenada',
            'Lista desordenada'])
plt.show()

# Vamos a comparar el tiempo de ejecución de mergeSort para listas
# ordenadas, inversamente ordenadas y desordenadas de distintos tamaños.
num_max = 1000
times_21 = []
times_22 = []
times_23 = []

for num in range(1,num_max + 1, 100):
   
   lista_21 = list(range(1, num))
   ex_time_21 = []
   for i in range(0,15):
        ex_time_21.append(timeit.timeit('mergeSort(lista_21.copy(), 0, len(lista_21)-1)'
                             ,globals=globals(),number = 10))
   times_21.append(min(ex_time_21))

   lista_22 = list(range(num, 1, -1))
   ex_time_22 = []
   for i in range(0,15):
        ex_time_22.append(timeit.timeit('mergeSort(lista_22.copy(), 0, len(lista_22)-1)'
                             ,globals=globals(),number = 10))
   times_22.append(min(ex_time_22))

   lista_23 = []
   for i in range(0,num):
       lista_23.append(random.random())
   ex_time_23 = []
   for i in range(0,15):
        ex_time_23.append(timeit.timeit('mergeSort(lista_23.copy(), 0, len(lista_23)-1)'
                             ,globals=globals(),number = 10))
   times_23.append(min(ex_time_23))

plt.plot(range(1,num_max+1, 100),times_21)
plt.plot(range(1,num_max+1, 100),times_22)
plt.plot(range(1,num_max+1, 100),times_23)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.title("Velocidad de ejecución de MergeSort")
plt.legend(['Lista ordenada','Lista inversamente ordenada',
            'Lista desordenada'])
plt.show()

# Vamos a comparar el tiempo de ejecución de heapSort para listas
# ordenadas, inversamente ordenadas y desordenadas de distintos tamaños.
num_max = 1000
times_21 = []
times_22 = []
times_23 = []

for num in range(1,num_max + 1, 100):
   
   lista_21 = list(range(1, num))
   ex_time_21 = []
   for i in range(0,15):
        ex_time_21.append(timeit.timeit('heapSort(lista_21.copy())'
                             ,globals=globals(),number = 10))
   times_21.append(min(ex_time_21))

   lista_22 = list(range(num, 1, -1))
   ex_time_22 = []
   for i in range(0,15):
        ex_time_22.append(timeit.timeit('heapSort(lista_22.copy())'
                             ,globals=globals(),number = 10))
   times_22.append(min(ex_time_22))

   lista_23 = []
   for i in range(0,num):
       lista_23.append(random.random())
   ex_time_23 = []
   for i in range(0,15):
        ex_time_23.append(timeit.timeit('heapSort(lista_23.copy())'
                             ,globals=globals(),number = 10))
   times_23.append(min(ex_time_23))

plt.plot(range(1,num_max+1, 100),times_21)
plt.plot(range(1,num_max+1, 100),times_22)
plt.plot(range(1,num_max+1, 100),times_23)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.title("Velocidad de ejecución de HeapSort")
plt.legend(['Lista ordenada','Lista inversamente ordenada',
            'Lista desordenada'])
plt.show()

# Vamos a comparar el tiempo de ejecución de quickSort para listas
# ordenadas, inversamente ordenadas y desordenadas de distintos tamaños.
num_max = 1000
times_21 = []
times_22 = []
times_23 = []

for num in range(1,num_max + 1, 100):
   
   lista_21 = list(range(1, num))
   ex_time_21 = []
   for i in range(0,15):
        ex_time_21.append(timeit.timeit('quickSortEnd(lista_21.copy(), 0, len(lista_21)-1)'
                             ,globals=globals(),number = 10))
   times_21.append(min(ex_time_21))

   lista_22 = list(range(num, 1, -1))
   ex_time_22 = []
   for i in range(0,15):
        ex_time_22.append(timeit.timeit('quickSortEnd(lista_22.copy(), 0, len(lista_22)-1)'
                             ,globals=globals(),number = 10))
   times_22.append(min(ex_time_22))

   lista_23 = []
   for i in range(0,num):
       lista_23.append(random.random())
   ex_time_23 = []
   for i in range(0,15):
        ex_time_23.append(timeit.timeit('quickSortEnd(lista_23.copy(), 0, len(lista_23)-1)'
                             ,globals=globals(),number = 10))
   times_23.append(min(ex_time_23))

plt.plot(range(1,num_max+1, 100),times_21)
plt.plot(range(1,num_max+1, 100),times_22)
plt.plot(range(1,num_max+1, 100),times_23)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.legend(['Lista ordenada','Lista inversamente ordenada',
            'Lista desordenada'])
plt.title("Velocidad de ejecución de QuickSortEnd")
plt.show()

# Vamos a comparar el tiempo de ejecucion de quickSort,
# para una lista aleatoria,
# tomando ahora el pivote en posiciones diferentes.
num_max = 1000
times_1 = []
times_2 = []
times_3 = []
times_4 = []
times_5 = []
for num in range(1,num_max + 1, 100):
   ex_time_1 = []
   ex_time_2 = []
   ex_time_3 = []
   ex_time_4 = []
   ex_time_5 = []
   for i in range(0,30):
        lista = []
        for j in range(0,num):
            lista.append(random.random())
        ex_time_1.append(timeit.timeit('quickSortRandomPivot(lista.copy(), 0, len(lista)-1)'
                                    ,globals=globals(),number = 1))
        ex_time_2.append(timeit.timeit('quickSortMedianPivot(lista.copy(), 0, len(lista)-1)'
                             ,globals=globals(),number = 1))
        ex_time_4.append(timeit.timeit('quickSortEnd(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 1))
        ex_time_5.append(timeit.timeit('quickSortStart(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 1))
   times_1.append(min(ex_time_1))
   times_2.append(min(ex_time_2))
   times_4.append(min(ex_time_4))
   times_5.append(min(ex_time_5))

plt.plot(range(1,num_max+1, 100),times_1)
plt.plot(range(1,num_max+1, 100),times_2)
plt.plot(range(1,num_max+1, 100),times_4)
plt.plot(range(1,num_max+1, 100),times_5)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.legend(['quickSortRandomPivot','quickSortMedianPivot','quickSortEnd','quickSortStart'])
plt.title("Comparación de diferentes pivotes en QuickSort, para listas aleatorias")
plt.show()


# Vamos a comparar el tiempo de ejecucion de quickSort, 
# para una lista ordenada,
# tomando ahora el pivote en posiciones diferentes.
num_max = 1000
times_1 = []
times_2 = []
times_3 = []
times_4 = []
times_5 = []
for num in range(1,num_max + 1, 100):
   ex_time_1 = []
   ex_time_2 = []
   ex_time_3 = []
   ex_time_4 = []
   ex_time_5 = []
   for i in range(0,30):
        lista = list(range(1, num))
        ex_time_1.append(timeit.timeit('quickSortRandomPivot(lista.copy(), 0, len(lista)-1)'
                                    ,globals=globals(),number = 1))
        ex_time_2.append(timeit.timeit('quickSortMedianPivot(lista.copy(), 0, len(lista)-1)'
                             ,globals=globals(),number = 1))
        ex_time_4.append(timeit.timeit('quickSortEnd(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 1))
        ex_time_5.append(timeit.timeit('quickSortStart(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 1))
   times_1.append(min(ex_time_1))
   times_2.append(min(ex_time_2))
   times_4.append(min(ex_time_4))
   times_5.append(min(ex_time_5))

plt.plot(range(1,num_max+1, 100),times_1)
plt.plot(range(1,num_max+1, 100),times_2)
plt.plot(range(1,num_max+1, 100),times_4)
plt.plot(range(1,num_max+1, 100),times_5)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.legend(['quickSortRandomPivot','quickSortMedianPivot','quickSortEnd','quickSortStart'])
plt.title("Comparación de diferentes pivotes en QuickSort, para listas ordenadas")
plt.show()

# Vamos a comparar el tiempo de ejecucion de quickSort, 
# para una lista inversamente ordenada,
# tomando ahora el pivote en posiciones diferentes.
num_max = 1000
times_1 = []
times_2 = []
times_3 = []
times_4 = []
times_5 = []
for num in range(1,num_max + 1, 100):
   ex_time_1 = []
   ex_time_2 = []
   ex_time_3 = []
   ex_time_4 = []
   ex_time_5 = []
   for i in range(0,30):
        lista = list(range(num, 1, -1))
        ex_time_1.append(timeit.timeit('quickSortRandomPivot(lista.copy(), 0, len(lista)-1)'
                                    ,globals=globals(),number = 1))
        ex_time_2.append(timeit.timeit('quickSortMedianPivot(lista.copy(), 0, len(lista)-1)'
                             ,globals=globals(),number = 1))
        ex_time_4.append(timeit.timeit('quickSortEnd(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 1))
        ex_time_5.append(timeit.timeit('quickSortStart(lista.copy(), 0, len(lista)-1)',
                             globals=globals(),number = 1))
   times_1.append(min(ex_time_1))
   times_2.append(min(ex_time_2))
   times_4.append(min(ex_time_4))
   times_5.append(min(ex_time_5))

plt.plot(range(1,num_max+1, 100),times_1)
plt.plot(range(1,num_max+1, 100),times_2)
plt.plot(range(1,num_max+1, 100),times_4)
plt.plot(range(1,num_max+1, 100),times_5)
plt.xlabel("Tamaño de la lista")
plt.ylabel("Tiempo (segundos)")
plt.legend(['quickSortRandomPivot','quickSortMedianPivot','quickSortEnd','quickSortStart'])
plt.title("Comparación de diferentes pivotes en QuickSort, para listas inversamente ordenadas")
plt.show()