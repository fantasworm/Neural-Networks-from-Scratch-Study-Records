import numpy as np 
import random

#inputs = [1.0, 2.0, 3.0, 2.5] 
#weights = [[0.2, 0.8, -0.5, 1], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]]
#biases = [2.0, 3.0, 0.5]

#layer_outputs = np.dot(weights, inputs) + biases
#print(layer_outputs)

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
outputarray = []

for i in range(m):
	weightarray.append(weightset(n))
	print('weights{} : {}'.format(i, weightarray[i]))
	biasarray.append(random.randrange(10) * random.random())
	print('bias{} : {}'.format(i, biasarray[i]))

outputarray = np.dot(weightarray, inputs) + biasarray
print(outputarray)