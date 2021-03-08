import math

#Values from the previous output when we described
#what a neural network is
layer_outputs = [4.8, 1.21, 2.385]

#e - mathematical constant, we use E here to match a common coding
#style where constants are uppercased
E = math.e #2.71828182846

#For each value in a vector, calculate the exponential value
exp_values = []
for output in layer_outputs:
	exp_values.append(E ** output)
#print('exponentiated values:')
#print(exp_values)

#Now normalize values
norm_base = sum(exp_values)
norm_values = []
for value in exp_values:
	norm_values.append(value / norm_base)
print('Normalized exponentiated values:')
print(norm_values)

print('Sum of normalized values:', sum(norm_values))