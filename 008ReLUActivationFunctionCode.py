import numpy as np

def ReLUBasic(inputs):
	output = []
	for i in inputs:
		if i > 0:
			output.append(i)
		else:
			output.append(0)

	return output

def ReLUAlt(inputs):
	output = []
	for i in inputs:
		output.append(max(0,i))

	return output


inputs = [0, 2, -1, 3.3, -2.7, 1.1, 2.2, -100]

output = []

#output = ReLUBasic(inputs)
#output = ReLUAlt(inputs)
output = np.maximum(0, inputs)

print(output)