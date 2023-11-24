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
# import tkinter as tk
# from tkinter import filedialog
# from tkinter import simpledialog
# from tkinter import messagebox
import numpy as np
import math
from matplotlib import pyplot as plt
import mediapipe as mp

############################################||NOTES||############################################
##
##  So far, the mapping becomes slower because of image processing
##
##
##
#################################################################################################

def main():
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    # Initialize MediaPipe Hands
    hands = mp_hands.Hands()
    # Initialize media capture
    cap = cv2.VideoCapture(0)
    while True:
        # Get frame
        success, img = cap.read()
        if not success:
            break
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # # Image processing
        # imgHeight = img.shape[0]
        # imgWidth = img.shape[1]
        # #Padding the image 
        # #creating a new image with an additional border of 1
        # paddedImg = np.zeros((imgHeight+2, imgWidth+2), dtype=np.uint8)
        # #Copying the original image to the center of the new image
        # for x in range(imgWidth):
        #     for y in range(imgHeight):
        #         paddedImg[y + 1][x + 1] = img[y][x]

        # #creating a canvas for the blurred image
        # blurred = np.zeros((imgHeight+2, imgWidth+2), dtype=np.uint8)
        # #Using a 3x3 averaging mask to blur the image
        # blurrer = np.ones((3, 3), np.float32) / 9
        # for x in range(1, paddedImg.shape[1] - 1):
        #     for y in range(1, paddedImg.shape[0] - 1):
        #         sum = 0
        #         for i in [-1,0,1]:
        #             for j in [-1,0,1]:
        #                 sum += blurrer[j + 1][i + 1] * paddedImg[y + j][x + i]
        #         blurred[y][x] = sum

        # #Removing the padding
        # blurr = np.zeros((imgHeight, imgWidth), dtype=np.uint8)
        # for x in range(imgWidth):
        #     for y in range(imgHeight):
        #         blurr[y][x] = blurred[y+1][x+1]

        # #Calculating the mask
        # mask = np.subtract(img,blurr,dtype=np.longlong)
        # #Ensuring the pixel values are in the [0, 255] range
        # for y in range(imgHeight):
        #     for x in range(imgWidth):
        #         if mask[y][x] < 0:
        #             mask[y][x] = 0
        #         elif mask[y][x] > 255:
        #             mask[y][x] = 255

        # #Sharpening the image by adding the mask
        # sharpImg = np.add(img,mask,dtype=np.longlong)
        # #Ensuring the pixel values are in the [0, 255] range
        # for y in range(imgHeight):
        #     for x in range(imgWidth):
        #         if sharpImg[y][x] < 0:
        #             sharpImg[y][x] = 0
        #         elif sharpImg[y][x] > 255:
        #             sharpImg[y][x] = 255

        # sharpImg = sharpImg.astype(np.uint8)

        # Apply sharpening with kernal for rgb
        kernel = np.array([[-1, -1, -1],
                        [-1,  9, -1],
                        [-1, -1, -1]])
        sharpImg = cv2.filter2D(img, -1, kernel)

        # Process the image and get hand landmarks
        results = hands.process(sharpImg)

        # Draw landmarks on the image
        if results.multi_hand_landmarks:
            for landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(img, landmarks, mp_hands.HAND_CONNECTIONS)

        # Displaying the video by frame
        cv2.imshow("Image", img)
        key_press = cv2.waitKey(100)
        if not key_press == -1:
            break
    cap.release()
    cv2.destroyAllWindows()


# For running the program from terminal
if __name__ == "__main__":
    main()
