import numpy as np 
import random

#inputs = [[1.0, 2.0, 3.0, 2.5], [2.0, 5.0, -1.0, 2.0], [-1.5, 2.7, 3.3, -0.8]] 
#weights = [[0.2, 0.8, -0.5, 1.0], [0.5, -0.91, 0.26, -0.5], [-0.26, -0.27, 0.17, 0.87]] 
#biases = [2.0, 3.0, 0.5] 

#layer_outputs = np.dot(inputs, np.array(weights).T) + biases
#print(layer_outputs)

def inputset(base, x):
	inputs = []
	for i in range(x):
		inputs.append(i+1+base)
	return inputs

def weightset(x):
	weights = []
	for i in range(x):
		weights.append(random.random()) 
	return weights

n = 4
base = 0
m = 3
inputarray = []
weightarray = []
biasarray = []
outputarray = []

for i in range(m):
	inputarray.append(inputset(base, n))
	base +=1
	weightarray.append(weightset(n))
	biasarray.append(random.randrange(10) * random.random())

print("inputarray")
print(inputarray)
print("weightarray")
print(weightarray)
print("biasarray")
print(biasarray)

outputarray = np.dot(inputarray, np.array(weightarray).T) + biasarray
print("outputarray")
print(outputarray)