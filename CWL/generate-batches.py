import os
import sys

#idx = int(sys.argv[1])
batch_len = int(sys.argv[1])

all_couples = os.listdir("../build/structures_0_16/")

for el in all_couples:
	if "." in el or "_" not in el:
		all_couples.remove(el)

all_couples.sort()
num_batches = round(len(all_couples)/batch_len)

def make_batches(l):
	batches = []
	for i in range(len(all_couples)//batch_len):
		index = i*100
		batches.append(all_couples[index:index+100])
	batches.append(all_couples[index+100:])
	return batches

batches = make_batches(all_couples)

res = ""
original_stdout = sys.stdout

for i in range(len(batches)):
	res = ""
	for el in batches[i]:
		res += " " + el
	filename = "batch_"+str(i+1)
	with open(filename, "w") as f:
		sys.stdout = f
		print(res)



sys.stdout = original_stdout
#print(res)
