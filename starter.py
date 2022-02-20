import cv2
import mediapipe as mp
import numpy as np
import streamlit as st 
import logic
<<<<<<< HEAD
from PIL import Image
=======
>>>>>>> 22d7182368d104c9f47d23e6a129b19fc9554230

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

website_icon = Image.open('mascot.jpg')
st.set_page_config(page_title='MyGymBuddy',page_icon=website_icon)
st.title("MyGymBuddy")
st.write("Select an exercise:")

bicep_curl = st.checkbox('Bicep Curl')
extensions = st.checkbox('Extensions')
squats = st.checkbox('Squats')

exercise_list = [bicep_curl, extensions, squats]
exercises = ['Bicep Curl', 'Extensions', 'Squats']
exercise_to_do = {}

for count, item in enumerate(exercise_list):
    if item:
        user_input_rep = st.text_input("Please enter rep amount: " + exercises[count], key=count)
        user_input_sets = st.text_input("Please enter set amount: " + exercises[count],key=count)
        exercise_to_do[exercises[count]] = {"reps":user_input_rep,"sets":user_input_sets}

options = st.button("Click me to begin.")
if options:
    st.write(exercise_to_do)
    logic.start(exercise_to_do)
