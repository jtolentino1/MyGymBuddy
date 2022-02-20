import mediapipe as mp
import numpy as np
import streamlit as st 
import main
from PIL import Image
import requests
from streamlit_lottie import st_lottie
from annotated_text import annotated_text

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose
website_icon = Image.open('MyGymBuddy.jpg')   

st.set_page_config(
    page_title='MyGymBuddy',
    page_icon=website_icon

    )
hidden_menu = """
    <style>
    #MainMenu {visibility: hidden; }
    footer {visibility: hidden;}
    </style>
    """
st.markdown(hidden_menu, unsafe_allow_html=True)

st.sidebar.markdown("""# <u>Exercises:</u>""",unsafe_allow_html=True)
st.sidebar.markdown(""" #  Bicep Curl 
    ##### For <u>bicep curls</u>, please place your <i>arms</i> and the left side of your body in _full view_ of the camera!
    #  Extensions 
    ##### For <u>extensions</u>, please place your <i>arms</i> and the left side of your body in _full view_ of the camera!
    #  Squats 
    ##### For <u>squats</u>, please place your <i>legs</i> and <i>feet</i> in _full view_ of the camera!
    #  Crunches 
    ##### For <u>crunches</u>, please <i>lay</i> down and keep the <i>left side</i> of your entire body in _full view_ of the camera!
    #  Rows 
    ##### For <u>rows</u>, please <i>lay</i> down and keep the <i>left side</i> of your entire body in _full view_ of the camera!
    #  Bench Press 
    ##### For <u>bench press</u>, please <i>lay</i> down and keep the <i>left side</i> of your body in _full view_ of the camera!
""",unsafe_allow_html=True)

col1, col2 = st.columns([2, 1])
with col1:
    st.title("MyGymBuddy")
    st.write("Select an exercise:")

    bicep_curl = st.checkbox('Bicep Curl')
    extensions = st.checkbox('Extensions')
    squats = st.checkbox('Squats')
    crunches = st.checkbox('Crunches')
    rows = st.checkbox('Rows')
    benchpress = st.checkbox('Benchpress')

    exercise_list = [bicep_curl, extensions, squats, crunches, rows, benchpress]
    exercises = ['Bicep Curl', 'Extensions', 'Squats','Crunches','Rows','Benchpress']
    exercise_to_do = {}

    for count, item in enumerate(exercise_list):
        if item:
            selected = True 
            user_input_rep = st.text_input("Please enter rep amount: " + exercises[count], key=count)
            user_input_sets = st.text_input("Please enter set amount: " + exercises[count],key=count)
            exercise_to_do[exercises[count]] = {"reps":user_input_rep,"sets":user_input_sets}

    options = st.button("Click me to begin.")
    if options:
        st.write(exercise_to_do)
        main.start(exercise_to_do)

with col2:
    lottie_diagram_url = 'https://assets7.lottiefiles.com/packages/lf20_k17htwqs.json'
    lottie_diagram = load_lottieurl(lottie_diagram_url)
    st_lottie(lottie_diagram, key='diagram')
    annotated_text(
        "Hey! I'm your",
        ("Gym", "", '#DC6D23'),
        ("Buddy.", "", '#89CFF0'),
    )
    annotated_text(
        "Let's get started working out!",
        
    )



