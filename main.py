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
##       main.py is handling the video feed and using the model to determine the alphabets
##
##  Steps:
##      0. Train a model with data and save it (not in this code)
##      1. Image Processing
##      2. Getting the video feed
##      3. Creating landmark coordinates for the hand in the feed with mediaPipe
##              model.pickle has been trained from a opensourse database on kaggle
##                                    ||
##                                   \  /
##                                    \/
##      4. Using previously trained model to determine hand gesture
##      5. Displaying the determined gesture on the feed
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
    with mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.35,
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

            curr_landmark_coord = []
            xList = []
            yList = []
            # Draw landmarks on the image
            img.flags.writeable = True
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            if results.multi_hand_landmarks:
                for landmarks in results.multi_hand_landmarks:
                    mp_drawing.draw_landmarks(img,
                                              landmarks,
                                              mp_hands.HAND_CONNECTIONS)
                for hand_landmarks in results.multi_hand_landmarks:
                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        xList.append(x)
                        yList.append(y)

                    for i in range(len(hand_landmarks.landmark)):
                        x = hand_landmarks.landmark[i].x
                        y = hand_landmarks.landmark[i].y
                        curr_landmark_coord.append(x - min(xList))
                        curr_landmark_coord.append(y - min(yList))

                prediction = model.predict([np.asarray(curr_landmark_coord)])
                predicted_character = prediction[0]
                accuracy = model.predict_proba([np.asarray(curr_landmark_coord)])
                print(predicted_character, accuracy)

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
