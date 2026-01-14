letters = "MyName"

chars_split = letters.split()

#print(chars_split)

for i in letters:
	num = ord(i)
	#print(chr(num))

#print(letters.encode())

import numpy as np
import random 

data = np.random.rand(3,5)
print(f"data: {data}")

sliced = data[:,0]
print(sliced)
