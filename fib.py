def fib(max):
	n,a,b = 0,0,1
	
	while n < max:
		yield b
		a,b = b, a+b
		n = n+1
	return 'done'

f = fib(4)
print(next(f)) # print 1
print(next(f)) # print 1
print(next(f)) # print 2
print(next(f)) # print 3
print(next(f)) # error