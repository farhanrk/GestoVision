<h1 align="center">COMP 3301 Project</h1>
<h1 align="center">GestoVision</h1>
<h3 align="center">Trishir Kumar Singh & Farhan Rahman Khan</h3><br>


<br>
<p align="center">A real-time Python application for American Sign Language gesture recognition, using scikit-learn for model training, MediaPipe for hand detection, and OpenCV for image manipulation.</p>
<br>
To run the program with the already trained model just run main.py and make sure you have all the required libraries from requirements.txt or from the list below.
<br>
<br>
Required:<br>
<blockquote>
mediapipe==0.10.8<br>
opencv-python==4.8.1.78<br>
scikit-learn==1.3.2<br>
numpy==1.26.2<br>
tkinter==8.6<br>         
</blockquote>

<br>
<br>
If you want to train your own model with your own photos, go through the files in sequence <code>coord_gen.py</code> &rarr; <code>model_trainer.py</code> &rarr; <code>main.py</code> <br>
Otherwise just run <code>main.py</code> <br>
<h3>main.py</h3> 
<p>This is our main program.</p>
<blockquote>
Run the file from terminal like so:<br>
<code>python main.py</code> or <code>python3 main.py</code><br>
Or you can also run the file using an IDE like VSCode<br>
</blockquote>
<em>NOTE: Comment out line 36, uncomment line 35 and make sure it matches the directory for your data if tkinter is not working.</em>
<br>

<h3>coord_gen.py</h3>

<p>This is the program to generate data (from pictures) on which we're going to train the model.</p>
<br>
<blockquote>
Run the file from terminal like so:<br>
<code> python coord_gen.py </code>
 or 
<code> python3 coord_gen.py</code><br>
Or you can also run the file using an IDE like VSCode<br>
</blockquote>
<br>

<h3>model_trainer.py</h3>
<p>This is where we train our model form the data created.</p>
<blockquote>
<br>
Run the file from terminal like so:<br>
<code>python model_trainer.py</code> or <code>python3 model_trainer.py</code><br>
Or you can also run the file using an IDE like VSCode<br>
</blockquote>
<br>

<h2> Acknowledgement </h2>
<blockquote>
@misc{https://www.kaggle.com/grassknoted/aslalphabet_akash nagaraj_2018 <br>
title={ASL Alphabet} <br>
url={https://www.kaggle.com/dsv/29550} <br>
DOI={10.34740/KAGGLE/DSV/29550} <br>
</blockquote>
