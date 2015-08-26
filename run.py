import KinoNetwork as kn
import numpy as np
import DataLoader as dl
import heapq

import time
start_time = time.time()

def list_gen(inp_data):
	input_data = []
	for i in range(0,80):
		input_data.append([0])
	for key in inp_data:
		input_data[key] = [1]
	return input_data
		

n = kn.KinoNetwork([80,100,200,400,200,100,80])

dataloader = dl.DataLoader()

data = dataloader.returnData('2015-01-02 10:00','2015-01-05 21:30')

counter = [0,0,0,0,0,0]

for i in range(0,len(data)-1):
	input_data = list_gen(data[i])
	
	output = n.feedforward(input_data).tolist()
	output2 = heapq.nlargest(20,output)
	output3 = []
	
	for key in output2:
		output3.append(output.index(key)+1)
	chance = 0
	next_input = list_gen(data[i+1])
	for y in range(4):
		if (output3[y] in data[i+1]):
			chance += 1

	print("Prediction: " + str(output3[0]) + "," + str(output3[1]) + "," + str(output3[2]) + "," + str(output3[3]))
	print("Outcomes: " + str(data[i+1]))
	
	if (chance == 0):
		counter[0] += 1
		counter[5] += 1
	if (chance == 1):
		counter[1] += 1
		counter[5] += 1
	if (chance == 2):
		counter[2] += 1
		counter[5] += 1
	if (chance == 3):
		counter[3] += 1
		counter[5] += 1
	if (chance == 4):
		counter[4] += 1
		counter[5] += 1

	n.update_network(input_data,next_input,1.0)

print("Out of "+str(counter[5])+" there were:")
print(str(counter[0]) + " 0%")
print(str(counter[1]) + " 25%")
print(str(counter[2]) + " 50%")
print(str(counter[3]) + " 75%")	
print(str(counter[4]) + " 100%")	

print("\n--- %s seconds ---" % (time.time() - start_time))
