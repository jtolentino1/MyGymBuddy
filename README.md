# MyGymBuddy

 MyGymBuddy is an application that seeks to promote your physical well-being by providing tools to aide you with exercises.
 
## About
MyGymBuddy is python web application (hosted using streamlit) that uses computer vision (through openCV and mediapipe) in order to visualize the exercises of the user. In the application, Users can select from a library of exercises and build their routine at home. From there, using their webcams, they are able to see how well their form is with feedback from the application.
  
 ## Showcase
 
  #### Front page of the website
 ![alt text](https://github.com/jtolentino1/MyGymBuddy/blob/main/showcase1.png)
 
  #### Selection of exercise with tab view
 ![alt text](https://github.com/jtolentino1/MyGymBuddy/blob/main/showcase2.png)
 
   #### Webcam view of the squat exercise
  ![alt text](https://github.com/jtolentino1/MyGymBuddy/blob/main/showcase3.png)
 
 ## What we Learned
 
 This was a great learning experience for all memebers of the team, as we learned that how to use the OpenCV library, as well as how to use streamlit library that Python offerend. This was also a great experience where we all worked together and collaborated and how to split up tasks to ensure that no one was left out and to make sure that our project was completed in the right amount of time. 


 ## What can be Improved?

Some of the biggest issues that we faced were having one camera connected at a time, which prevented us from being able to have as many exercises as we wanted to. One reason why this is important, and an improvement is that we can have more exercises and can have the user decide how they want to do their work out with having the need to move the camera. 

We can also add more exercises as well, and this would be a simple addition, and it will benefit heavily from the improvements that can be made to our camera capturing abilities. 

One large improvement that we could make would be to have users be able to put in their own workout so that they are not limited to the workouts that we have made for them.

## Requirements

For this project, run these commands to fufill all dependecies in order to run the project.
```
pip install opencv-python
pip install mediapipe
pip install streamlit
pip install streamlit_lottie
pip install requests
pip install PIL
pip install st-annotated-text
```
## Running the Project

To run the project, first cd into the repo then run:

```
python -m streamlit run starter.py
```
