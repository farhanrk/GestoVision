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
import mediapipe as mp
import pickle

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
    # Load the model first
    model = pickle.load(open("model.pickle", "rb"))

    # Setup media pipe
    mp_hands = mp.solutions.hands
    mp_drawing = mp.solutions.drawing_utils
    #mp_drawing_styles = mp.solutions.drawing_styles

    # Initialize media capture
    cap = cv2.VideoCapture(0)
    with mp_hands.Hands(min_detection_confidence=0.35,
                        min_tracking_confidence=0.35) as hands:
        while cap.isOpened():
            # Get frame
            success, img = cap.read()
            if not success:
                print("Ignoring empty camera frame")
                continue

            # Abiding by OpenCV's whims
            img.flags.writeable = False
            img= cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            # Process the image and get hand landmarks
            results = hands.process(img)

            # Draw landmarks on the image
            img.flags.writeable = True
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(img,
                                              landmarks,
                                              mp_hands.HAND_CONNECTIONS)

            # Displaying the video by frame
            # Flip the image horizontally for a selfie-view display.
            cv2.imshow("Press ESC to exit", cv2.flip(img, 1))

            # Exit on ESC
            key_press = cv2.waitKey(1)
            if key_press == 27:
                break
    cap.release()
    cv2.destroyAllWindows()


# For running the program from terminal
if __name__ == "__main__":
    main()
