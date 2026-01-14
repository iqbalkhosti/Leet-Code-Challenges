
def print_pyramid(n):

	for i in range(1, n+1):

		spaces = " " * (n-i)
		asters = "*" * (2*i -1)

		print(spaces+asters)
		
print_pyramid(4)

