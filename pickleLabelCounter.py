###################################________GestoVision________###################################
##
##  Project || CS 3301 - Visual Computing
##  Group Name          : The Trainers
##  Group Members(s)    : [Trishir Kumar Singh, Farhan Rahman Khan] 
##  Name                : Trishir Kumar Singh
##  Student ID          : 202023149
##  Name                : Farhan Rahman Khan
##  Student ID          : 202124798
##
#####################################||IMPORTING LIBRARIES||#####################################
import pickle
############################################||NOTES||############################################
##
##               pickleLabelCounter.py is just a helper file for debugging purposes
##                      it tells us how many data we have for some alphabets
##
#################################################################################################

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

print("A: "+str(countA))
print("B: "+str(countB))
print("C: "+str(countC))