import pickle

data_dict = pickle.load(open("./data.pickle","rb"))

print(data_dict.keys())
# print(data_dict)


countA = 0
countB = 0
countC = 0
for i in data_dict['labels']:
    if (i=="A"):
        countA +=1
    if (i=="B"):
        countB +=1
    if (i=="C"):
        countC +=1


print(countA)
print(countB)
print(countC)