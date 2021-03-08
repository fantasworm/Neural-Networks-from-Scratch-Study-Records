import random

#A layer of neuron with...
#n inputs, use y = n+1 for now
#n weights, use random.random() for now
#m output, save as a list
#m bias, use random.randrange(10) * random.random() for now

def inputset(x):
	inputs = []
	for i in range(x):
		inputs.append(i+1)
	return inputs

def weightset(x):
	weights = []
	for i in range(x):
		weights.append(random.random()) 
	return weights

n = 4
m = 3
inputs = inputset(n)
print('inputs : {}'.format(inputs))
weightarray = []
biasarray = []
output = 0.0
outputarray = []

for i in range(m):
	weightarray.append(weightset(n))
	print('weights{} : {}'.format(i, weightarray[i]))
	biasarray.append(random.randrange(10) * random.random())
	print('bias{} : {}'.format(i, biasarray[i]))

for j in range(m):
	output = 0.0
	for k in range(n):
		output += inputs[k]*weightarray[j][k]
	output += biasarray[j]
	outputarray.append(output)

print(outputarray)