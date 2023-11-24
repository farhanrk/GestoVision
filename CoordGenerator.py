import os
import pickle

import mediapipe as mp
import cv2
import matplotlib.pyplot as plt

#put the location of the kaggle dataset here
DATA_DIRECTORY = "./data\\alphabet_train"

cap = cv2.VideoCapture(0)

mp_hands = mp.solutions.hands

hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, model_complexity=1) #because we're using photos to train

data = []
labels = []
# this will automatically itterate throught all the folders in the alphabet_train folder, each folder will be one label or one alphanbet
for letter_label in os.listdir(DATA_DIRECTORY):
    #iterating through all the photos inside the folder A or B or...
    for img_path in os.listdir(os.path.join(DATA_DIRECTORY, letter_label)):
        
        print("Working with "+str(letter_label)+" picture no: "+str(img_path))
        curr_landmark_coord = []
        xList = []
        yList = []

        
        img = cv2.imread(os.path.join(DATA_DIRECTORY, letter_label, img_path))
        #apparently openCV uses BGR and mediapipe needs RGB, I don't really get it
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

        results = hands.process(img_rgb)
        if results.multi_hand_landmarks:
            #this shouldn't really matter now because we only have a single hand in the training images but eh
            for hand_landmarks in results.multi_hand_landmarks:
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y

                    xList.append(x)
                    yList.append(y)
                print("Working with "+str(letter_label)+" picture no: "+str(img_path)+" x and y found.")
                for i in range(len(hand_landmarks.landmark)):
                    x = hand_landmarks.landmark[i].x
                    y = hand_landmarks.landmark[i].y
                    #because we only need the relative positions of the landmarks, doesn't matter where in the picture they're in
                    curr_landmark_coord.append(x - min(xList))
                    curr_landmark_coord.append(y - min(yList))
                print("Working with "+str(letter_label)+" picture no: "+str(img_path)+" data created.")

            data.append(curr_landmark_coord)
            labels.append(letter_label)

#saving it all in a pickle file
f = open('./data.pickle', 'wb')
pickle.dump({'data': data, 'labels': labels}, f)
f.close()
