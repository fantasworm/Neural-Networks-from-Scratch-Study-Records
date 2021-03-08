#inputs = [1,2,3]
#weights = [0.2, 0.8, -0.5]
#bias = 2

#output = (inputs[0]*weights[0] + inputs[1]*weights[1] + inputs[2]*weights[2] + bias)

#print(output)

import random

#A single neuron with...
#n inputs, use y = n+1 for now
#n weights, use random.random() for now
#1 bias = 0 since a neuron will only has one(at least form what I learned for now)

n = 3
inputs = []
weights = []
bias = 0
output = 0.0

for i in range(n):
	inputs.append(i+1)
	weights.append(random.random())

for j in range(n):
	output += inputs[j]*weights[j]

output += bias

print(output)