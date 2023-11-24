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
import cv2
import numpy as np
import math
from matplotlib import pyplot as plt
import mediapipe as mp

############################################||NOTES||############################################
##
##  So far, the mapping becomes slower because of image processing
##
##  Steps:
##      1. Image Processing
##      2. Crop it out to only hand for efficiency (not cropping the video feed, but working with the cropped part)
##      3. Generate Landmarks
##      4. Train, classify, detect
##
#################################################################################################

def main():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    #mp_drawing_styles = mp.solutions.drawing_styles
    # Initialize MediaPipe Hands
    hands = mp_hands.Hands(min_detection_confidence=0.35)
    # Initialize media capture
    cap = cv2.VideoCapture(0)
    while True:
        # Get frame
        success, img = cap.read()
        if not success:
            break

        ############################||Apply sharpening with kernal for rgb
        # kernel = np.array([[-1, -1, -1],
        #                 [-1,  9, -1],
        #                 [-1, -1, -1]])
        # sharpImg = cv2.filter2D(img, -1, kernel)

        # Process the image and get hand landmarks
        results = hands.process(img)

        # Draw landmarks on the image
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, landmarks, mp_hands.HAND_CONNECTIONS)

        # Displaying the video by frame
        cv2.imshow("Image", img)
        key_press = cv2.waitKey(1)
        if key_press == 27: # Exit on ESC
            break
    cap.release()
    cv2.destroyAllWindows()


# For running the program from terminal
if __name__ == "__main__":
    main()
