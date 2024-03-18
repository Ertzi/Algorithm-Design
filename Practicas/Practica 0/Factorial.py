import matplotlib.pyplot as plt
import timeit

def recur_fac(n):
   """Function to return the factorial
   of a number using recursion"""
   if n == 1:
       return 1
   else:
       return n * recur_fac(n-1)

num_max = 500
iterations = 100
times = []
for num in range(1,num_max + 1):
   ex_time = timeit.timeit('recur_fac(num)',globals=globals(),number = iterations) / iterations * 1000 # Pasarlo a milisegundos
   times.append(ex_time)

plt.plot(range(1,num_max+1),times)
plt.xlabel("Números del 1 al 500")
plt.ylabel("Tiempo de ejecución en milisegundos")
plt.show()




