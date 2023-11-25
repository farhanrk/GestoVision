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
import os
import pickle
import mediapipe as mp
import cv2
from tkinter import filedialog
############################################||NOTES||############################################
##
##              CoordGenerator.py is a file we use to generate the landmark coordinates
##                                 and save it as data.pickle
##
##  Steps:
##      1. Setting up neccesary objects and variables
##      2. For each folder(represents one letter) itterate through each photo(each file)
##      3. Creates the handlandmark coordinates and saves them along with their label(folder names)
##      4. Dumps them all together and saves as data.pickle
##
#################################################################################################


def main():
    # put the location of the kaggle dataset (or your own) here

    # Comment out line 36, uncomment line 35 and make sure it matches the directory for your data if tkinter is not working
    #DATA_DIRECTORY = "./data"
    DATA_DIRECTORY = filedialog.askdirectory(title="Select a Folder!")

    mp_hands = mp.solutions.hands
    hands = mp_hands.Hands(static_image_mode=True, min_detection_confidence=0.3, max_num_hands=1)  # because we're using photos to train

    data = []
    labels = []
    # this will automatically itterate throught all the folders in the alphabet_train folder, each folder will be one label or one alphanbet
    for letter_label in os.listdir(DATA_DIRECTORY):
        counter = 0
        # iterating through all the photos inside the folder A or B or...
        for img_path in os.listdir(os.path.join(DATA_DIRECTORY, letter_label)):
            print("Working with " + str(letter_label) + " picture no: " + str(img_path))
            curr_landmark_coord = []
            xList = []
            yList = []

            img = cv2.imread(os.path.join(DATA_DIRECTORY, letter_label, img_path))
            # apparently openCV uses BGR and mediapipe needs RGB, I don't really get it
            img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            results = hands.process(img_rgb)
            if results.multi_hand_landmarks:
                # this shouldn't really matter now because we only have a single hand in the training images but eh
                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y

                        xList.append(x)
                        yList.append(y)
                    print("Working with " + str(letter_label) + " picture no: " + str(img_path) + " x and y found.")
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        # because we only need the relative positions of the landmarks, doesn't matter where in the picture they're in
                        curr_landmark_coord.append(x - min(xList))
                        curr_landmark_coord.append(y - min(yList))
                    print("Working with " + str(letter_label) + " picture no: " + str(img_path) + " data created.")

                data.append(curr_landmark_coord)
                labels.append(letter_label)
                counter += 1
            if counter == 2000:
                break


    # saving it all in a pickle file
    f = open('./data.pickle', 'wb')
    pickle.dump({'data': data, 'labels': labels}, f)
    f.close()


# For running the program from terminal
if __name__ == "__main__":
    main()
