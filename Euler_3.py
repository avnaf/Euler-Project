Python 2.7.14 (v2.7.14:84471935ed, Sep 16 2017, 20:19:30) [MSC v.1500 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> def f():
	print "1"

	
>>> s = "f"
>>> import os
>>> os.execl
<function execl at 0x025F9DF0>
>>> os.execl(s)

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    os.execl(s)
  File "C:\Python27\lib\os.py", line 314, in execl
    execv(file, args)
ValueError: execv() arg 2 must not be empty
>>> sum([i for i in range(1000) if not i % 3 or not i % 5])
233168
>>> fib = [1,2]
>>> while fib[-1] + f[-2] < 4*10**6:
	fib.append(fib[-1] + f[-2])

	

Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    while fib[-1] + f[-2] < 4*10**6:
TypeError: 'function' object has no attribute '__getitem__'
>>> fib
[1, 2]
>>> fib[-1]
2
>>> fib[-2]
1
>>> fib[-3]

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    fib[-3]
IndexError: list index out of range
>>> while fib[-1] + f[-2] < 4000000:
	fib.append(fib[-1] + f[-2])

	

Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    while fib[-1] + f[-2] < 4000000:
TypeError: 'function' object has no attribute '__getitem__'
>>> while (fib[-1] + f[-2]) < 4000000:
	fib.append(fib[-1] + f[-2])

	

Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    while (fib[-1] + f[-2]) < 4000000:
TypeError: 'function' object has no attribute '__getitem__'
>>> while fib
KeyboardInterrupt
>>> 
KeyboardInterrupt
>>> while fib[-1] + fib[-2] < 4*10**6:
	fib.append(fib[-1] + fib[-2])

	
>>> fib
[1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578]
>>> sum fib
SyntaxError: invalid syntax
>>> sum(fib[::2])
3524577
>>> sum(fib)
9227463
>>> sum(::2)
SyntaxError: invalid syntax
>>> sum(fib[::2])
3524577
>>> sum(fib)-_
5702886
>>> fib[::2]
[1, 3, 8, 21, 55, 144, 377, 987, 2584, 6765, 17711, 46368, 121393, 317811, 832040, 2178309]
>>> sum([i in fib if i % 2 == 1])
SyntaxError: invalid syntax
>>> sum([i for i in fib if i % 2 == 1])
4613731
>>> 
=================== RESTART: C:/Python27/Euler/Euler_2.py ===================
>>> 
>>> 


>>> 


>>> 

>>> prime_factors = []
>>> def prime_factors(n):
	primes = [2,3,5,7,11,13,17]
	for p in primes:
		if n // p == n/p:
			n /= p

>>> def prime_factors(n):
	primes = [2,3,5,7,11,13,17]
	
	for p in primes:
		if n // p == n/p:
			n /= p
			
