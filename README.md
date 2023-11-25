<h2 align="center">COMP 3301 Project</h2>
<h1 align="center">GestoVision</h1>
<h5 align="center">Trishir Kumar Singh & Farhan Rahman Khan</h5><br>


<br>
<p align="center">A real-time Python application for American Sign Language gesture recognition, using scikit-learn for model training, MediaPipe for hand detection, and OpenCV for image manipulation.</p>
<br>
To run the program with the already trained model just run main.py and make sure you have all the required libraries from requirements.txt or from the list below.
<br>
<br>
Reqired:<br>
mediapipe==0.10.8<br>
opencv==4.8.1.78<br>
scikit-learn==1.3.2<br>
numpy==1.26.2<br>
<br>
<br>
If you want to train your own model with your own photos, go through the files in sequence CoordGenerator.py --> model_trainer.py --> main.py
<h3 align="center">main.py</h3> <br>
<p align="center">This is our main program.</p>
<br>
Run the file from terminal like so:<br>
python main.py or python3 main.py<br>
Or you can also run the file using an IDE like VSCode<br>
<br>
Note: Larger path may take a while to find the path, the code uses BFS algorithm to find the shortest path but time complexity is high.<br>
      The console will have outputs as you run the program to keep you updated on what's happening inside the code.<br>
      If you select a big range for start and end coordinates the console will show the traversing nodes/coordinates, the program doesn't crash but takes some time on occasions but works.<br><br>

<h3 align="center">CoordGenerator.py</h3> <br>
<p align="center">This is the program to generate data (from pictures) on which we're going to train the model.</p>
<br>
Run the file from terminal like so:<br>
python CoordGenerator.py or python3 CoordGenerator.py<br>
Or you can also run the file using an IDE like VSCode<br>
<br>
<br>

<h3 align="center">model_trainer.py</h3> <br>
<p align="center">This is where we train our model form the data created.</p>
<br>
Run the file from terminal like so:<br>
python model_trainer.py or python3 model_trainer.py<br>
Or you can also run the file using an IDE like VSCode<br>
<br>
<br>
