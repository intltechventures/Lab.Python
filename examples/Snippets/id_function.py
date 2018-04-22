'''
Example of the id() function

https://docs.python.org/3/library/functions.html#id
	Return the “identity” of an object. This is an integer which is guaranteed to be unique and constant for this object during its lifetime. Two objects with non-overlapping lifetimes may have the same id() value.

	CPython implementation detail: This is the address of the object in memory.
'''

x = 7
y = 7
print("Identity value of x: ", id(x))
print("Identity value of y: ", id(y))
x = "Changed value to String"
y = 14
print("Identity value of x: ", id(x))
print("Identity value of y: ", id(y))

